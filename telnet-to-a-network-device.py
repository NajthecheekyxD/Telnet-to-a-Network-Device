import telnetlib
import getpass
import argparse

def establish_telnet_connection(ip, username, password):
    try:
        connection = telnetlib.Telnet(ip)
        write_line(connection, username)
        write_line(connection, password)
        connection.read_until(b'#', timeout=5)  # Adjust the timeout as needed
        print(f"Telnet connection established to {ip}")
        return connection
    except Exception as e:
        print(f"Failed to establish telnet connection: {e}")
        raise

def write_line(connection, data):
    connection.write(data.encode('ascii') + b'\n')

def execute_command(telnet_connection, command):
    write_line(telnet_connection, command)
    output = telnet_connection.read_until(b'#', timeout=5).decode('ascii')  # Adjust the timeout as needed
    return output

def menu(telnet_connection):
    while True:
        print("\n---Telnet Menu---")
        print("1. Change Hostname")
        print("2. Save Running Configuration")
        print("3. Exit")
        choice = input("Enter your choice: ").lower()

        if choice == '1':
            new_hostname = input("Enter the new hostname: ")
            change_hostname(telnet_connection, new_hostname)

        elif choice == '2':
            save_running_config(telnet_connection)

        elif choice == '3':
            print("Exit")
            break

        else:
            print("Invalid choice. Please enter a valid option!")

def change_hostname(telnet_connection, new_hostname):
    commands = [
        'configure terminal',
        f'hostname {new_hostname}',
        'end',
        'write memory'
    ]
    for command in commands:
        output = execute_command(telnet_connection, command)
        print(output)  # Print the output after each command
    print(f"Success! Hostname changed to: {new_hostname}")

def save_running_config(telnet_connection):
    output = execute_command(telnet_connection, 'show running-config')
    with open('running_config.txt', 'w') as file:
        file.write(output)
    print(output)  # Print the output after the 'show running-config' command
    print("Success! Running configuration saved to: running_config.txt")

def main():
    # Argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="Device IP address")
    parser.add_argument("--username", help="Username")
    parser.add_argument("--password", help="Password")
    args = parser.parse_args()

    ip_address = args.ip or '192.168.56.101'
    username = args.username or input("Enter your username: ")
    password = args.password or getpass.getpass(prompt="Enter your password: ")

    # Telnet Connection
    telnet_connection = establish_telnet_connection(ip_address, username, password)

    menu(telnet_connection)

    # Close the Telnet Connection
    telnet_connection.write(b'quit\n')
    print("Telnet connection closed.")

if __name__ == "__main__":
    main()
