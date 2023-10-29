import telnetlib

# Define Variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'
new_hostname = 'NewHostname'

# Establish Telnet Connection
telnet_connection = telnetlib.Telnet(ip_address)

def main_menu():
    while True:
        print("Telnet Menu:")
        print("1. Login to the device")
        print("2. Change device hostname")
        print("3. Save configuration")
        print("4. Show running configuration")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            login()
        elif choice == '2':
            change_hostname()
        elif choice == '3':
            save_configuration()
        elif choice == '4':
            show_running_config()
        elif choice == '5':
            quit_telnet()
            break
        else:
            print("Invalid choice. Please select a valid option.")

def login():
    # Code to log in to the device
    telnet_connection.read_until(b'Username: ')
    telnet_connection.write(username.encode('ascii') + b'\n')
    telnet_connection.read_until(b'Password: ')
    telnet_connection.write(password.encode('ascii') + b'\n')
    telnet_connection.read_until(b'#')
    print('17') # Indicate successful login

def change_hostname():
    # Code to change the device's hostname
    telnet_connection.write(b'configure terminal\n')
    telnet_connection.read_until(b'#')
    telnet_connection.write(f'hostname {new_hostname}\n'.encode('ascii'))
    telnet_connection.read_until(b'#')
    print('23') # Indicate hostname change

def save_configuration():
    # Code to save the configuration
    telnet_connection.write(b'end\n')
    telnet_connection.read_until(b'#')
    telnet_connection.write(b'write memory\n')
    telnet_connection.read_until(b'#')
    print("35") # Indicate successful configuration saving

def show_running_config():
    # Code to display the running configuration
    telnet_connection.write(b'show running-config\n')
    output = telnet_connection.read_until(b'end').decode('ascii')
    print("38") # Indicate successful running configuration output
    return output

def quit_telnet():
    # Code to close the Telnet connection
    telnet_connection.write(b'quit\n')
    print("42") # Indicate the closure of the Telnet connection

if __name__ == "__main__":
    main_menu()
