#!/usr/bin/python36
print("content-type: text/html")
print("\n")
import cgi
import cgitb
cgitb.enable()
import subprocess as sp
from container import Container
print("hi")
ports=sp.getoutput("netstat -tunlep | grep LISTEN | awk '{print $4}' ")
ports =ports.split("\n")
#print(ports)
usedPorts=[]
for i in ports:
		usedPorts.append(int(i.split(":")[-1]))		
#print(usedPorts)
for i in range(1024,65535):
		if i not in usedPorts:
			newPort=i
			print(newPort)
			break
		i=i+1

print(sp.getstatusoutput("sudo docker run -dit -p {}:3333  xpra_vlc:v4".format(newPort)))
