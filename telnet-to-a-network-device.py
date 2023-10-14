import pexpect

# Define Variables
ip_address = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'
new_hostname = 'NewHostname'

# Create telnet session
session = pexpect.spawn('telnet ' + ip_address, encoding= 'utf-8', timeout=20)

result = session.expect(['Username:', pexpect.TIMEOUT])

# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! creating session for: ', ip_address)
    exit()

# Session is expecting username, enter details
session.sendline(username)
result = session.expect(['Password:', pexpect.TIMEOUT])

# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering username:' , username)
    exit()

# Session is expecting password, enter details
session.sendline(password)
result = session.expect(['#', pexpect.TIMEOUT])

# Check for error, if exists then display error and exit
if result != 0:
    print('--- FAILURE! entering password:', password)
    exit()

# Display a success message if it works
print('-------------------------------------------------')    
print('')
print('--- Success! connecting to:', ip_address)
print('---               Username:', username)
print('---               Password:', password)
print('')
print('---------------------------------')

# Modify the device hostname
session.sendline('configure terminal')
session.expect('#')
session.sendline('hostname ' + new_hostname)
session.expect('#')

# Save the configuration
session.sendline('end')
session.expect('#')
session.sendline('write memory')
session.expect('#')

#Terminate telnet to device and close session
session.sendline('quit')
session.close()
