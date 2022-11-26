#!/usr/bin/env python3

import subprocess
#myProc = open('outputfile.txt','a')
#hStdErr = open('error.txt','a') 
#res = subprocess.run(['ps','-axco','command'],stdout=myProc,stderr=hStdErr)

myProc = subprocess.run(['ps','-axco','command'],stdout=subprocess.PIPE)
myProcString = myProc.stdout.decode()
myProcList= myProcString.split('\n')
#print(myProcString)
#print(myProcList)
for line in myProcList:
    print(line)
print(len(myProcList))