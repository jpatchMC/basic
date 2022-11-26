#!/usr/bin/env python3

def main():
    print("josh Patch")
    print("converting F to C")
    

def tempF2C(tempF):
    
    temp2 = int(tempF)
    ctemp = (temp2 -32) * (5/9)
    print(ctemp)


if __name__ == "__main__":
    main()
    tempF = input("temperature in Fahrenheit")
    tempF2C(tempF)
    