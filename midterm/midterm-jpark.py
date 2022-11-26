#!/usr/bin/env python3
from ast import Continue


print("Name: Josh Patch")
#++++++++++++++++++++==initset==================================
password_database = {"username":"dnedry","password":"please"}
command_database = {"reboot":"OK. I will reboot all park systems.","shutdown":"OK. I will shut down all park systems","done":"I hate all this hacker stuff"}
white_rabbit_object = 0

counter = 0
input_user = input("user:")
input_password = input("password:")
#dnedry please

#===================begin loop=======================
while white_rabbit_object == 0:
    if input_user == password_database.get("username") and input_password == password_database.get("password"):
        white_rabbit_object = 1
        print("hi Dennis. You're still the best hacker in Jurassic Park.")
        print("enter a command")
        print(command_database.keys())
        cmd = input("?")
        if cmd == "reboot":
            print(command_database.get("reboot"))
        elif cmd == "shutdown":
            print(command_database.get("shutdown"))
        elif cmd == "done":
            print(command_database.get("done"))
        else:
            print("the lysine Contingency has been put into effect")
    else:
        counter = counter+1
        print(f"you didn't say the magic word. {counter}")
        input_user = input("user:")
        input_password = input("password:")
        if counter >= 2:
            ##badvar="you didn't say the magic word."
            for i in range(25):
                print("you didn't say the magic word.")
            break
        ####done!!!!!#####



