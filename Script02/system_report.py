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

#Get Disk Information
diskCapacity = bash_command("df -h | grep '/dev/mapper' | awk '{print $2}'")
availableSpace = bash_command("df -h | grep '/dev/mapper' | awk '{print $4}'")

#Get Processor Information
cpuModel = bash_command("lscpu | grep 'Model name:' | awk '{print $3, $4, $5, $6}'")
numProcessors = bash_command("lscpu | grep 'Socket(s):' | awk '{print $2}'")
numCores = bash_command("lscpu | grep 'Core(s) per socket:' | awk '{print $4}'")


#Get Memory Information
totalRAM = bash_command("free -m -h | grep 'Mem:' | awk '{print $2}'")
availableRAM = bash_command("free -m -h | grep 'Mem:' | awk '{print $4}'")


#Generate Output Strings
header = "System Report - " + date + "\n"
deviceInfo = "Device Information \n Hostname: " + hostname + "\n Domain: " + domainName
networkInfo = "Network Information \n IP Address: " + ip + "\n Gateway: " + gateway + "\n Network Mask: " + mask + "\n DNS1: " + dns1 + "\n DNS2: " + dns2 
osInfo = "OS Information \n Operating System: " + os + "\n Operating Version: " + osVersion + "\n Kernel Version: " + kernelVersion
storageInfo = "Storage Information \n Hard Drive Capacity: " +  diskCapacity + "\n Available Space: " + availableSpace
processorInfo = "Processor Information \n CPU Model: " + cpuModel + "\n Number of Processors: " + numProcessors + "\n Number of cores: " + numCores
memInfo = "Memory Information \n Total RAM: " + totalRAM + "\n Available RAM: " + availableRAM

output = header + "\n\n" + deviceInfo + "\n\n" + networkInfo + "\n\n" + osInfo + "\n\n" + storageInfo + "\n\n" + processorInfo + "\n\n" + memInfo


#Display Output
print(output)

#Output report to file
file = open(hostname + "_system_report.log", "w")
file.write(output)
file.close()
