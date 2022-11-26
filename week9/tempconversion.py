#!/usr/bin/env python3

print("josh patch")
print("to ask what you want to convert and then convert it")

what = input("what are you trying to convert celsius or Fahrenheit? enter F or C:")
what = what.upper()
if what == "F":
    import f2c
    
    tempF = input("temperature?: ")
    f2c.tempF2C(tempF)
    #print(ctemp)
    
#break
if what == "C":
    import c2f
    tempC = input("temperature?: ")
    c2f.tempC2F(tempC)
#break