#!/usr/bin/env python3



print("Name: Josh Patch")
line = []
count = 0
total = 0
wdlist = ["gmeach18@ed.gov","248.253.63.149","Whiteland","80.222.19.190","Kayley","dcassyqw@microsoft.com"]
with open(r'Midterm-if.txt','r')as hfile:
    line = hfile.readlines()
    for ln in line:
        #print(ln)
        for word in wdlist:
            if word in ln:
                sln=ln.split(',')
                count=(int(sln[0]))
                #print(count)
            
            #tcount= count
            #print(count)
                total += (count)
print(f"the total is:{total}")