import time, paramiko
wlc_session = paramiko.SSHClient()
wlc_session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def cred_input():

    credentials = ["username", "password"]
    
    credentials[0] = input("Enter the administrator's password: ")
    credentials[1] = input("Enter the administrator's password: ")

    return credentials

operation = int(input("Would you like to add [1] or remove [2] a device?: "))

def dev_add_mac():
    dev_mac_addr = input("Please enter the MAC address: ")
    ### The MAC address will not be accepted by the CLI unless the hyphens are replaced by colons. 
    if "-" in dev_mac_addr:
            dev_mac_addr = dev_mac_addr.replace('-', ':')
    dev_descript = input("Enter the device's description: ")
    int_name =  input("Enter the WLC interface name: ")
    ### In order for the interface name to be parsed correctly by the CLI, spaces must be appended before and after the defined interface string. 
    int_name = (" " + int_name + " ")

    return dev_mac_addr, dev_descript, int_name

def add_wlc_info():

    wlc_info = ["ip_addr", "port"]

    wlc_info[0] =  input("Enter the WLC's IP address: ")
    wlc_info[1] =  input("Enter the WLC's port (leave blank for default port 22): ")
    if wlc_info[1] == "":
        wlc_info[1] = "22"

def op_add_mac(dev_add_mac,add_wlc_info, cred_input):
    op_mac_addr = dev_mac_addr
    op_ip_info = wlc_info
    op_login = credentials


    wlc_session.connect(op_ip_info[0], port=op_ip_info[1], username='null', password='null')

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(op_login[0] + '\n')
    time.sleep(0.1)
    wlc_ssh_class.send(op_login[1] + '\n')
    time.sleep(0.1)
