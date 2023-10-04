#!/usr/bin/python3
#Albie Snyder
#10/4/2023

import subprocess

def bash_command(cmd):
	#Runs the command, converts output to string, and strips whitespace
	return subprocess.check_output(cmd, shell=True).decode().strip()

#clear terminal
subprocess.run("clear", shell=True)

#Get data

#Date
date = bash_command("date")

#Get hostname and domain name
hostname = bash_command("hostname")
domainName = bash_command("domainname")

#Get Network Information
ip = bash_command("ip -o -4 route show to default | awk '{print $9}'")
netInterface = bash_command("ip link show| grep 'state UP' | awk '{print $2}' | cut -d ':' -f 1")
mask = bash_command("/sbin/ifconfig " + netInterface + " | grep 'netmask' | awk '{print $4}'")
gateway = bash_command("ip -o -4 route show to default | awk '{print $3}'")
dns1, dns2 = bash_command("cat /etc/resolv.conf | grep 'nameserver' | awk '{print $2}'").split()


#Get OS Information
os = bash_command("lsb_release -a | grep 'Description' | awk '{print $2, $3}'")
osVersion = bash_command("lsb_release -a | grep 'Release' | awk '{print $2}'")
kernelVersion = bash_command("uname -r")

print(os)
print(osVersion)
print(kernelVersion)


