import telnetlib

# Define Variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'
new_hostname = 'NewHostname'

def login_to_device():
    global telnet_connection
    telnet_connection = telnetlib.Telnet(ip_address) #Establish Telnet Connection
    telnet_connection.read_until(b'Username: ')
    telnet_connection.write(username.encode('ascii') + b'\n')
    telnet_connection.read_until(b'Password: ')
    telnet_connection.write(password.encode('ascii') + b'\n') 
    telnet_connection.read_until(b'#') # Entering into Privileged EXEC mode


def configure_device():
    telnet_connection.write(b'configure terminal\n')
    telnet_connection.read_until(b'#')
    telnet_connection.write(f'hostname {new_hostname}\n'.encode('ascii'))
    telnet_connection.read_until(b'#')

def save_configuration():
    telnet_connection.write(b'end\n')
    telnet_connection.read_until(b'#')
    telnet_connection.write(b'write memory\n')
    telnet_connection.read_until(b'#')

def execute_command():
    telnet_connection.write(b'show running-config\n')
    output = telnet_connection.read_until(b'end').decode('ascii')
    return output

def main():
    print('=' * 50)
    print(" Telnet Menu")
    print('=' * 50)
    print("1. Login")
    print("2. Configure the device")
    print("3. Save the configuration")
    print("4. Execute a command")
    print("5. Quit")
    print('=' * 50)

    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if choice == 1:
            login_to_device()
            print("Successfully Logged into the device.")
        
        elif choice == 2:
            configure_device()
            print("Successfully configured the device.")
        elif choice == 3:
            save_configuration()
            print("Successfully saved the configuration.")
        elif choice == 4:
            output = execute_command()
            with open('running_config.txt', 'w') as file:
                file.write(output)
            print("Running configuration saved to: running_config.txt")
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose an option from the menu.")

if __name__ == "__main__":
    main()
