import telnetlib

# Define Variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'
new_hostname = 'NewHostname'

# Establish Telnet Connection
telnet_connection = telnetlib.Telnet(ip_address)


# Login to the device
telnet_connection.read_until(b'Username: ')
telnet_connection.write(username.encode('ascii') + b'\n')
telnet_connection.read_until(b'Password: ')
telnet_connection.write(password.encode('ascii') + b'\n')
 

# Enter Privileged EXEC Mode
telnet_connection.read_until(b'#')
 

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
 

# Send a command to the remote device to output the running configuration 
telnet_connection.write(b'show running-config\n')
output = telnet_connection.read_until(b'end').decode('ascii')
 

# Save the output to a file
with open('running_config.txt', 'w') as file:
    file.write(output)

# Close the Telnet Connection
telnet_connection.write(b'quit\n')
  
print('-' *50)
print(f" Success!\n Device IP: {ip_address}\n Username: {username}\n Password: {password}")
print(f" Running configuration saved to: running_config.txt\n Hostname changed to: {new_hostname}")
print('-' *50)

