### This is the syntax for adding a MAC address: config macfilter add <MAC address> <WLAN ID> [interface name] [description] [client IP address]
### Be sure to add spaces between the concatentated strings so they are parsed correctly by the Cisco CLI

### Changelog:
### Version 1.0: Initial Release (5/20/2019)
### Jarred Reid 

import time, paramiko
wlc_session = paramiko.SSHClient()
wlc_session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("---------------------------")
print("WLC Utility 1.0 - Add or delete MAC address")
print("---------------------------")

user1 = input("Enter the administrator username: ")
pass1 = input("Enter the administrator password: ")

operation = int(input("Do you want to add [1] or remove [2] a device?: "))

def AddTo_WLC():
    mac_addr = input("Enter the MAC address to be added" )
    if "-" in mac_addr:
            mac_addr = mac_addr.replace('-', ':')
    description = input("Enter the device description: ")
    int_name = " keynet "


    ### Initiate SSH Connection to WLC #1
    wlc_session.connect('192.168.1.1', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter add ' + mac_addr + ' 1 ' + int_name + description + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    ### Initiate SSH Connection to WLC #2
    wlc_session.connect('192.168.1.2', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter add ' + mac_addr + ' 1 ' + int_name + description + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

        ### Initiate SSH Connection to WLC #3
    wlc_session.connect('192.168.2.1', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter add ' + mac_addr + ' 2 ' + int_name + description + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)
    
    ### Initiate SSH Connection to WLC #4
    wlc_session.connect('192.168.2.2', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter add ' + mac_addr + ' 2 ' + int_name + description + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    ### Initiate SSH Connection to WLC #1
    wlc_session.connect('192.168.3.1', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter add ' + mac_addr + ' 1 ' + int_name + description + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    ### Initiate SSH Connection to WLC #2
    wlc_session.connect('192.168.3.2', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter add ' + mac_addr + ' 1 ' + int_name + description + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

def RemoveFrom_WLC():
    mac_addr = input("Enter the MAC address to be removed: " )
    if "-" in mac_addr:
            mac_addr = mac_addr.replace('-', ':')

    ### Initiate SSH Connection to WLC #1
    wlc_session.connect('192.168.1.1', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter delete '+ mac_addr + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

     ### Initiate SSH Connection to WLC #2
    wlc_session.connect('192.168.1.2', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter delete '+ mac_addr + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    ### Initiate SSH Connection to WLC #3
    wlc_session.connect('192.168.2.1', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter delete '+ mac_addr + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    ### Initiate SSH Connection to WLC #4
    wlc_session.connect('192.168.2.2', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter delete '+ mac_addr + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    ### Initiate SSH Connection to WLC #1
    wlc_session.connect('192.168.3.1', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter delete '+ mac_addr + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    ### Initiate SSH Connection to WLC #2
    wlc_session.connect('192.168.3.2', port='22', username='null', password='null')

    ### Pass the CLI to Python Terminal

    wlc_ssh_class = wlc_session.invoke_shell()
    time.sleep(0.1)
    wlc_ssh_class.send(user1 +'\n')
    time.sleep(0.1)
    wlc_ssh_class.send(pass1 +'\n')
    time.sleep(0.1)

    ### Disable paging to display properly
    wlc_ssh_class.send('config paging disable'+'\n')
    time.sleep(0.1)
    strip_login_text = wlc_ssh_class.recv(1024).decode('utf-8')

    ### Here you can pass the commands to the WLC
    wlc_ssh_class.send('config macfilter delete '+ mac_addr + '\n')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

    wlc_ssh_class.send('save config')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    wlc_ssh_class.send('y')
    time.sleep(0.1)
    output = wlc_ssh_class.recv(2048).decode('utf-8', 'backslashreplace')
    print(output)

def Main():  
    if operation == 1:
        AddTo_WLC()
    elif operation == 2:
        RemoveFrom_WLC()
    else:
        print("Please select from options Add [1] or Delete [2]")

Main()
