#!/usr/bin/python3

print("content-type: text/html")
#print("location: http://192.168.0.107/index.html")
print()

import subprocess
import cgi
import webbrowser
import pyttsx3
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
#newVoiceRate = 145
#engine.setProperty('voice', voices[1].id)
#engine.setProperty('rate',newVoiceRate)
#new = "Can you tell me your requirements which software you want to open ?"
#print(new)
#engine.setProperty('rate',newVoiceRate)
#engine.say(new)
#engine.runAndWait()
data = cgi.FieldStorage()
output = data.getvalue("q")

#print(output)
if(("date" in output)):
    centos = 'date'
    voice = "sudo espeak -s 125 -v en+f5 'Today Date'"
    #subprocess.getoutput("espeak-ng Hello")
    #subprocess.getoutput("curl")
    o = subprocess.getoutput(centos)
    voiceback = subprocess.getoutput(voice)
    print(o)
if(("cal" in output) ):
    centos = 'cal'
    #subprocess.getoutput("espeak-ng Hello")
    #subprocess.getoutput("curl")
    voice = "sudo espeak -s 125 -v en+f5 'Calender Opened'"
    voiceback = subprocess.getoutput(voice)
    o = subprocess.getoutput(centos)
    print(o)
if(("launch" in output) or ("new" in output)):
    voice = "sudo espeak -s 125 -v en+f5 'You want to launch Docker container let me go to main page'"
    voiceback = subprocess.getoutput(voice)
    centos = 'curl -s http://192.168.99.104/docker.html'
    o = subprocess.getoutput(centos)
    print(o)
if(("stop" in output) or ("container stop" in output)):
    voice = "sudo espeak -s 125 -v en+f5 'You want to Stop Docker container let me do for you'"
    voiceback = subprocess.getoutput(voice)
    centos = 'curl -s http://192.168.99.104/dockerstop.html'
    o = subprocess.getoutput(centos)
    print(o)
if(("start" in output)):
    centos = 'curl -s http://192.168.99.104/dockerstart.html'
    voice = "sudo espeak -s 125 -v en+f5 'You want to Start docker container let me do for you'"
    voiceback = subprocess.getoutput(voice)
    o = subprocess.getoutput(centos)
    print(o)
if(("volume" in output)):
    centos = 'curl -s http://192.168.99.104/dockervolume.html'
    voice = "sudo espeak -s 125 -v en+f5 'You want to create volume for docker let me do for you'"
    voiceback = subprocess.getoutput(voice)
    o = subprocess.getoutput(centos)
    print(o)
if(("network" in output)):
    centos = 'curl -s http://192.168.99.104/dockernetwork.html'
    voice = "sudo espeak -s 125 -v en+f5 'You want to create network let me create for you'"
    voiceback = subprocess.getoutput(voice)
    o = subprocess.getoutput(centos)
    print(o)
if("voice" in output):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say("I will speak this text")
    engine.runAndWait()
     

