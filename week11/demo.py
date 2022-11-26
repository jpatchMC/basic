#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="make base argument")

parser.add_argument('-f',dest='firstname',default="bob",type=str, help="first name here")
parser.add_argument('-l',dest='lname',default="dole",type=str, help="last name here")
parser.add_argument('-p','--your-PIN',dest='PIN', required=True,type=int,help="numvber to unlock")
##type=int or str or float for bool action="store_true"
parser.add_argument('-m', '--status', action='store_true' , help="you married?")#if -m then it will store as true and if no -m then false#
parser.add_argument('-s', '--salary',dest="money", type=float, help="how much chedda you git?" ,required=False ,default='15.75', metavar="[an hourly amount]")
#list are differnet the + is so it adds to list nargs can spec a # too, a ? makes none or more + is one or more, * all similare to + #
parser.add_argument('-c',dest='children', nargs='+' , default="NONE" , help="enter kids names here")
parser.add_argument('-a', dest='pets', action='append', help="pets names here")
if parser.parse_args().status:
    print(f"you are not single")
if parser.parse_args().money > 20:
    print(f"can i borrow $40?")
if parser.parse_args().children == "NONE":
    print(f"can i borrow $40?")
print(type(parser))
print(parser.parse_args())