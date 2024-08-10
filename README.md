# JunOS Static Updates
Repository for Python scripting involving static updates to list of host devices specified in HostFile.py.  All code was built using Python3.

The HostFile.py represents a dictionary of hostnames and IP addresses in key:value format.  

The python scripts in this repository will work on any device running JunOS, and has been tested on:

  - MX routers
  - EX switches
  - SRX Firewalls
  - QFX Switches

Netmiko and Paramiko are both required to run the scripts and are good practices to have anyway for networking based automation.

They can be installed with the 'pip3 install' commands listed below.
```
pip3 install netmiko

pip3 install paramiko
```
![](https://media.istockphoto.com/id/521975241/photo/colorful-tulip-fields-in-front-of-a-traditional-dutch-windmill.jpg?s=612x612&w=0&k=20&c=te6Ae47s1keeozF19orusEX5nJew4ZwfaYWWf7yuALo=)
