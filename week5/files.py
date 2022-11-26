#!/usr/bin/env python3



hFile = open("/etc/passwd", "r")
strfileps = hFile.read()
###print(strfileps)###

print(f"the number of characters in this file string is {len(strfileps)}")
print("I'm using read because i want to count all the characters and generate as a string")
    
hFile.close()

hFile = open("/etc/passwd", "r")
###did i need to do this? couldn't i just put this all before closing the file?###
lstfileps = hFile.readlines()


print(f"the number of lines in this file list is {len(lstfileps)}")
print("I'm using readlines because i need my out to be a list and count the number of lines")

hFile.close()
print(f"the number of characters in this file string is {len(strfileps)}")
print("I'm using read because i want to count all the characters and generate as a string")
    
hFile.close()


hFile = open("/etc/passwd")
###did i need to do this? couldn't i just put this all before closing the file?###
lstfileps = hFile.readlines()


print(f"the number of lines in this file list is {len(lstfileps)}")
print("I'm using readlines because i need my out to be a list and count the number of lines")

hFile.close()

hFile = open("/etc/passwd", "r")

count = 0

for line in hFile:
    count = count + len(line)
print(f"the number of characters in this file list is {count}")
### print above is not indentes because i want my for loop to resolve before i print###

hFile.close()