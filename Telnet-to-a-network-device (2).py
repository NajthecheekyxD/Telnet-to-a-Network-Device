import telnetlib

def get_input(prompt):
    return input(prompt).lower()

def main():
    ip_address = '192.168.56.101'
    username = 'cisco'
    password = 'cisco123!'

    # Establish Telnet Connection
    telnet_connection = telnetlib.Telnet(ip_address)

    # Login to the device
    telnet_connection.read_until(b'Username: ')
    telnet_connection.write(username.encode('ascii') + b'\n')
    telnet_connection.read_until(b'Password: ')
    telnet_connection.write(password.encode('ascii') + b'\n')
     
    # Enter Privileged EXEC Mode
    telnet_connection.read_until(b'#')

    while True:
        print("\n---MENU---")
        print("1. Change Hostname")
        print("2. Save Running Configuration")
        print("3. Exit")
        choice = get_input("Enter your choice: ")

        if choice == '1':
            new_hostname = input("Enter the new hostname: ")
            # Configure the device
            telnet_connection.write(b'configure terminal\n')
            telnet_connection.read_until(b'#')
            telnet_connection.write(f'hostname {new_hostname}\n'.encode('ascii'))
            telnet_connection.read_until(b'#')

            # Save the configuration
            telnet_connection.write(b'end\n')
            telnet_connection.read_until(b'#')
            telnet_connection.write(b'write memory\n')
            telnet_connection.read_until(b'#')
            print(f"Success! Hostname changed to: {new_hostname}")

        elif choice == '2':
            # Send a command to the remote device to output the running configuration 
            telnet_connection.write(b'show running-config\n')
            output = telnet_connection.read_until(b'end').decode('ascii')
             
            # Save the output to a file
            with open('running_config.txt', 'w') as file:
                file.write(output)

            print(f"Success! Running configuration saved to: running_config.txt")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please enter a valid option!")

    # Close the Telnet Connection
    telnet_connection.write(b'quit\n')

    print('-' *50)
    print(f"Device IP: {ip_address}\nUsername: {username}\nPassword: {password}")
    print('-' *50)

if __name__ == "__main__":
    main()

