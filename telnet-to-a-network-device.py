import telnetlib

# Define Variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'
new_hostname = 'NewHostname'

# Establish Telnet Connection
telnet_connection = telnetlib.Telnet(ip_address)
print('11')  # Indicate that the Telnet connection is being established

# Login to the device
telnet_connection.read_until(b'Username: ')
telnet_connection.write(username.encode('ascii') + b'\n')
telnet_connection.read_until(b'Password: ')
telnet_connection.write(password.encode('ascii') + b'\n')
print('17')  # Indicate successful login

# Enter Privileged EXEC Mode
telnet_connection.read_until(b'#')
print('23')  # Indicate entry into privileged exec mode

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
print("35")  # Indicate successful configuration and save this file locally

# Send a command to the remote device to output the running configuration 
telnet_connection.write(b'show running-config\n')
output = telnet_connection.read_until(b'end').decode('ascii')
print("38") # Print the output of the running configuration

# Save the output to a file
with open('running_config.txt', 'w') as file:
    file.write(output)

# Close the Telnet Connection
telnet_connection.write(b'quit\n')
print("42")  # Indicate the closure of the Telnet connection


