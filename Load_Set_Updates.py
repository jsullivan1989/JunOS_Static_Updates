from netmiko import ConnectHandler
from paramiko import *
from netmiko.exceptions import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.exceptions import AuthenticationException

from HostFile import *

''' Simple Python script to make standard set command updates on any JunOS device.  The comma separated list given in
set_commands would be the equivalent to a list that would be copy/pasted with the load set terminal command for "n" number
of set commands. 

HostFile represents the hostfile with a list of <hostname>:<IP_addresses> in key:value pair.

An additional check by checking the location of the configuration hierarchy and matching on a keyword specified to see if the configuration
has been updated.  If so, pass to the next device in the list.

Used default SSH port of 22.  Update port number if nonstandard port is being used instead.'''

set_commands = ['<set command 1>',
                       '<set command 2>',
               .
               .
               .
              '<set command n>']


passwd = getpass.getpass('Please enter the JunOS password for your account: ')

for k in HostFile:
    try:
        Hostname = k
        IP_Address = HostFile[k]
        Host = {
            'device_type': 'juniper',
            'host': IP_Address,
            'username': '<username>',
            'password': passwd,
            'port': 22,
            }
        net_connect = ConnectHandler(**Host)
        command_output = net_connect.send_command('show configuration <hierarchy> | match <keyword> | display set')
        if '<keyword>' in command_output:
            print('Configuration is updated on ' + Hostname)
        if '<keyword>' not in command_output:
            print(Hostname + ' needs updated Configuration...updating now')
            set_command_update = net_connect.send_config_set(set_commands, exit_config_mode=False)
            print(set_command_update)
            command_output = net_connect.commit(and_quit=True, comment="<Commit comment string of your choice>")
            print(command_output) # validate that the changes are being implemented
    except(AuthenticationException):
        print('Authentication Failure for ' + Hostname)
    except(NetMikoTimeoutException):
        print('Timeout to device: ' + Hostname)
    except(SSHException):
        print('SSH may not be enabled on ' + Hostname + '.  Check the configuration again.')
    


