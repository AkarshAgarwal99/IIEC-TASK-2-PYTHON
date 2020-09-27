#!/usr/bin/python3

print("content-type: text/html")
#print("location: http://192.168.0.105/index.html")
print()

import subprocess
import cgi

data = cgi.FieldStorage()
drivername = data.getvalue("drivername")
networkname = data.getvalue("networkname")
container = "sudo docker network create --driver {} {}".format(drivername , networkname)
o4 = subprocess.getoutput(container)
voice = "sudo espeak -s 125 -v en+f5 'Docker Network Created'"
voiceback = subprocess.getoutput(voice)

print(o4)


