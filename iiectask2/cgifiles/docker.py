#!/usr/bin/python3

print("content-type: text/html")
#print("location: http://192.168.0.105/index.html")
print()

import subprocess
import cgi

data = cgi.FieldStorage()
osname = data.getvalue("os")
volname = data.getvalue("vol")
volpath = data.getvalue("pathofvolume")
patting = data.getvalue("patting")
patting2 = data.getvalue("pattingpath")
imagename = data.getvalue("image")
container = "sudo docker run -dit --name {} -v {}:{} -p {}:{} {}".format(osname,volname,volpath,patting,patting2,imagename)
o4 = subprocess.getoutput(container)
print(o4)
voice = "sudo espeak -s 125 -v en+f5 'Your Container Launched'"
voiceback = subprocess.getoutput(voice)

