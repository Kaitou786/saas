#!/usr/bin/python36

import subprocess as sp
from port import Port
class Container:
	def createContainer(self):
		port=Port()
		newPort=port.getNewPort()
		sp.getoutput("sudo docker run -dit -p {}:3333 --device /dev/snd -v /videos:/root/video  xpra_vlc:v4".format(newPort))
		return newPort
