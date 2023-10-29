import telnetlib

# Define Variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'
new_hostname = 'NewHostname'

#Establish Telnet Connection
telnet_connection = telnetlib.Telnet(ip_address)

#Login to the device
telnet_connection.read_until(b'Username: ')
telnet_connection.write(username.encode('ascii') + b'\n')
telnet_connection.read_until(b'Password:')
telnet_connection.write(password.encode('ascii') + b'\n')

#Enter Privileged EXEC Mode
telnet_connection.read_until(b'#')

def display_menu():
    print("\n-" *20)
    print(" Menu")
    print("-" * 20)
    print("1. Display Running Configuration")
    print("2. Change Hostname")
    print("3. Exit")
    print("-" *20)

while True:
    display_menu()
    choice = input ("Enter your choice: ")

    if choice == "1":
        # Send a command to the remote device to output the running configuration
        telnet_connection.write(b'show running-config\n')
        output = telnet_connection.read_until(b'end').decode('ascii')

        #Save the output to a file
        with open('running_config.txt', 'w') as file:
            file.write(output)
        
        print(f"\n Running configuration saved to: running_config.txt")

    elif choice == "2":
        new_hostname = input("Enter the new hostname: ")

        #Configure the device
        telnet_connection.write(b'configure terminal\n')
        telnet_connection.read_until(b'#')
        telnet_connection.write(f'hostname {new_hostname}\n'.encode('ascii'))
        telnet_connection.read_until(b'#')

        #Save the configuration
        telnet_connection.write(b'end\n')
        telnet_connection.read_until(b'#')
        telnet_connection.write(b'write memory\n')
        telnet_connection.read_until(b'#')

        print(f"\n Hostname changed to: {new_hostname}")
    elif choice == "3":
        break
    else:
        print("\n Invalid Choice! Please Try Again.")

# Close the Telnet Connection
telnet_connection.write(b'quit\n')

print("\n-"*50)
print(f" Success!\n Device IP: {ip_address}\n Username: {username}\n Password: {password}")
print("-"*50)


