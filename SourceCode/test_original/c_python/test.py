import os
import re

f = os.popen("./test | grep Jong")
nameList = re.findall("\*\'\w+\'\*",f.read())
name = nameList[0][2:-2]

print "name = " + name
