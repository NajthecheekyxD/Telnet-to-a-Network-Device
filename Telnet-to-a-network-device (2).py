import telnetlib

# Define Variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'
new_hostname = 'NewHostname'

def connect_to_device():
    global telnet_connection
    telnet_connection = telnetlib.Telnet(ip_address)
    telnet_connection.read_until(b'Username: ')
    telnet_connection.write(username.encode('ascii') + b'\n')
    telnet_connection.read_until(b'Password: ')
    telnet_connection.write(password.encode('ascii') + b'\n') 
    telnet_connection.read_until(b'#')

def enter_privileged_exec_mode():
    telnet_connection.read_until(b'#')

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
    print("1. Connect to device")
    print("2. Enter Privileged EXEC Mode")
    print("3. Configure the device")
    print("4. Save the configuration")
    print("5. Execute a command")
    print("6. Quit")
    print('=' * 50)

    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if choice == 1:
            connect_to_device()
            print("Successfully connected to the device.")
        elif choice == 2:
            enter_privileged_exec_mode()
            print("Successfully entered Privileged EXEC Mode.")
        elif choice == 3:
            configure_device()
            print("Successfully configured the device.")
        elif choice == 4:
            save_configuration()
            print("Successfully saved the configuration.")
        elif choice == 5:
            output = execute_command()
            with open('running_config.txt', 'w') as file:
                file.write(output)
            print("Running configuration saved to: running_config.txt")
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose an option from the menu.")

if __name__ == "__main__":
    main()
