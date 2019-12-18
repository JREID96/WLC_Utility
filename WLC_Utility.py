### Wireless LAN Controller Utility 2.0 - Jarred Reid
### Changelog:
### Version 1.0: Initial Release (5/20/2019)
### Version 1.6: Rewrote program. Ability to config individual controllers has been added.
### Version 2.0: Batch support has been added to the program. Use "wlc_config.ini" to add IPs and hostnames/MAC address.

import time, paramiko, os, sys
wlc_session = paramiko.SSHClient()
wlc_session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

### As initialized upon program startup, the first item of this list, path[0], is the directory containing the script that was used to invoke the Python interpreter
os.chdir(sys.path[0])


def get_Credential():

    credentials = ["username", "password"]
    
    credentials[0] = input("Enter the administrator's username: ")
    credentials[1] = input("Enter the administrator's password: ")

    return credentials

def get_WLC_Info():

    wlc = ["ip_addr", "port", "int"]

    wlc[0] =  input("Enter the WLC's IP address: ")
    wlc[1] =  input("Enter the WLC's port (leave blank for default port 22): ")
    wlc[2] =  input("Enter the WLC interface name: ")
    
    ### In order for the interface name to be parsed correctly by the CLI, spaces must be appended before and after the defined interface string. 
    wlc[2] = (" " + wlc[2] + " ")

    if wlc[1] == "":
        wlc[1] = "22"

    return wlc

def import_Config():
    
    from configparser import ConfigParser

    config_file = 'wlc_config.ini'

    parser = ConfigParser()
    parser.read(config_file)
    
    import_IP = parser.get('CONNECTION', 'ip',).split(',')
    import_Port = parser.get('CONNECTION', 'port').split(',')
    import_Int = parser.get('CONNECTION', 'interface').split(',')

    wlc = ["ip_addr", "port", "int"]

    ### Figure out how to parse the list entries 1,2 as strings and strip the list brackets and quotes so that all settings are configured from the ini
    wlc[0] = import_IP
    wlc[1] = "22"
    wlc[2] = "keynet"

    return wlc

def get_Device_Info():
    mac_addr = input("Please enter the MAC address: ")
    ### The MAC address will not be accepted by the CLI unless the hyphens are replaced by colons. 
    if "-" in mac_addr:
            mac_addr = mac_addr.replace('-', ':')
    dev_description = input("Enter the device's description: ")
   
    return mac_addr, dev_description

def set_Operation():
    
    print("""
    [1] Add device to whitelist
    [2] Remove device from whitelist
    """)

    set_op = int(input("Please make a selection: "))

    if set_op == 1:
        dev_operation = "add"

    if set_op == 2:
        dev_operation = "delete"

    elif set_op != 1 or 2:
        print("Please enter a valid selection from above: ")

    return dev_operation

def start_Operation():
    
    ### Initiate SSH tunnel to the WLC
    wlc_session.connect(wlc[0], port=wlc[1], username='null', password='null')

    ### Print the stdout to client terminal
    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(credentials[0] + '\n')
    time.sleep(0.1)
    wlc_ssh_class.send(credentials[1] + '\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Performing the requested operation on the WLC
    wlc_ssh_class.send('config macfilter ' + dev_operation + ' ' + mac_addr + ' 1 ' + wlc[2] + ' ' + dev_description + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    ### Saving the running config
    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

def auto_Operation(ip, wlc, credentials, dev_operation, mac_addr, dev_description):
    ### Initiate SSH tunnel to the WLC
    wlc_session.connect(ip, port=wlc[1], username='null', password='null')

    ### Print the stdout to client terminal
    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(credentials[0] + '\n')
    time.sleep(0.1)
    wlc_ssh_class.send(credentials[1] + '\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Performing the requested operation on the WLC

    if dev_operation == "add":
        wlc_ssh_class.send('config macfilter ' + dev_operation + ' ' + mac_addr + ' 1 ' + wlc[2] + ' ' + dev_description + '\n')

    if dev_operation == "remove":
        wlc_ssh_class.send('config macfilter ' + dev_operation + ' ' + mac_addr + '\n')

    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    ### Saving the running config
    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)


def start_Main():

    if prompt_Config == "1":
        use_Config = "TRUE"
        wlc = import_Config()
        mac_addr, dev_description = get_Device_Info()
        dev_operation = set_Operation()

        print(dev_description + " with MAC address: " + mac_addr + " will be " + dev_operation + "ed to/from the following controller IP(s): ")
        print(wlc[0])
        print()

        for ip in wlc[0]:
            print("Adding to Controller with IP: " + ip)
            print()
            print("Controller Output: ")
            auto_Operation(ip, wlc, credentials, dev_operation, mac_addr, dev_description)
            
    if prompt_Config == "2":
        use_Config = "FALSE"
        wlc = get_WLC_Info()
        mac_addr, dev_description = get_Device_Info()
        dev_operation = set_Operation()
        start_Operation()
            
print("""
    cisco Wireless LAN Controller Utility v2
    ----------------------------------------
    """)

credentials = get_Credential()

prompt_Config = input("Press [1] to import WLC info from configuration file, otherwise press enter: ")

while True:
    start_Main()

# get credentials
# get wireless controller information
# define operation
# get MAC info
# execute
# loop/exit
