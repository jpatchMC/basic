#!/usr/bin/env python3
def main():
    print("josh Patch")
    print("converting C to F")
    

def tempC2F(tempC):
    
    temp2 = int(tempC)
    ctemp = (temp2 * (9/5))+32
    print(ctemp)



if __name__ == "__main__":
    main()
    tempC = input("temperature in Celsius")
    tempC2F(tempC)