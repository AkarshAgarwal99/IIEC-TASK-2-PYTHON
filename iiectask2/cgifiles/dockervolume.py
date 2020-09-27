#!/usr/bin/python3

print("content-type: text/html")
#print("location: http://192.168.0.105/index.html")
print()

import subprocess
import cgi

data = cgi.FieldStorage()
osname = data.getvalue("dockervolume")
container = "sudo docker volume create {}".format(osname)
o4 = subprocess.getoutput(container)
voice = "sudo espeak -s 125 -v en+f5 'docker volume created'"
voiceback = subprocess.getoutput(voice)

print(o4)

