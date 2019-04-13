#!/usr/bin/python36
import cgi
import cgitb
import time
cgitb.enable()
#print("content-type:text/html")
#print("\n")

from container import Container
from port import Port
import subprocess as sp


class URL:
	def __init__(self):
		url=""
	def getUrl(self):
		test=Container()
		newPort=test.createContainer()
		#print(newPort)
		self.url="http://192.168.56.101:"+str(newPort)
		return self.url

#req=URL()
#test.getUrl()
#time.sleep(4)
#print("location:{}".format(req.getUrl()))
#print("\n")
#print("hi")
