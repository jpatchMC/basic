#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="This is Josh script")

parser.add_argument('-m',dest='basic',type=str, help="Enter some text")
parser.add_argument('-i','--integer', dest='integer',required=True , help="Enter a simple Integer" , type=int , metavar="[an integer]")
parser.add_argument('-d','--float',dest='float',metavar="[a float]",help="Enter a simple float", type=float)
parser.add_argument('-s','--string',dest='string', help="Enter a simple string", type=str, metavar="[a string]")
parser.add_argument('-l',metavar="[strings]", nargs='+', default=[],help="Enter a list of strings (space delimited)",dest='liststring')
parser.add_argument('-t','--set-true', action='store_true', help="Toggle from default False to True")
parser.add_argument('-f','--setfalse',action='store_false', help="Toggle from default True to False")
parser.add_argument('-v','--version',help="show program's version number and exit",action='version', version='%(prog)s 1.0')
#print(type(parser))
args = parser.parse_args()
print(args.integer)
print(args.string)
print(args.basic)
print(args.float)
print(args.liststring)