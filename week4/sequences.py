#!/usr/bin/env python3
varString = "Here is a nice string to slice"
varList = [ "Here", "is", "a", "nice", "list", "to", "slice" ]

print(varString[4::1])
print(varString[0:3:1])
print(varString[4:12:1])
print(varString[0::2])
print(varString[::-1])

print(varList[::-1])
print(varList[3:0:-1])

print(varList[0::3])
print(varList[2:4:1])
print(varList[1::1])

for char in varString:
    print(char)

for word in varList:
    print(word)


"""this ok?"""