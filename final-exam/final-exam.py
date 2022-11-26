#!/usr/bin/env python3
import argparse
from multiprocessing import Value


#setup#
parser = argparse.ArgumentParser(description= 'parser for final')
parser.add_argument('-i','--ipaddress',dest='ipadd',help='Enter IP address',type=str,required=True,default='172.31.29.252')
parser.add_argument('-f','--function',dest='fun',help='enter a number 1-5 to pick which function',required=True,type=str,default=1)
args = parser.parse_args()
URL=(f"http://{args.ipadd}/q{args.fun}")
IP=args.ipadd
print(URL)
print("Name : Josh Patch")
func = (args.fun)
#this is a FUN 1, get it?#

import requests
def get_response():
    response = requests.get(URL)
    #if response.ok:
    body = response.text
    return (f"ANSWER: {body}")
#fun too.....get it? eh?#
import bs4
def parse_string():
    bsele = requests.get(URL)
    bsele.raise_for_status
    wpage = bs4.BeautifulSoup(bsele.text,features="html.parser")
    h3 = str(wpage.h3)
    #print(h3)
    return (f"{h3[8:25:2]} Josh")
#function 3#
def parse_header():
    head = requests.get(URL)
    #print(f"Headers: {head.headers}")
    for key,value in head.headers.items():
        if key == "MATC-HEADER":
            return (f"ANSWER: {value}")
#function 4#
import json
def parse_json():
    book = requests.get(URL)
    booksearch =(json.loads(book.text))
    spcbook=(booksearch['Music And Books'][3])
    #bsrch = (json.dumps(booksearch, indent=2))
    #print(spcbook)
    for key in spcbook:
        return(f"ANSWER: {spcbook['publish_info']['publisher']}")
import socket
def socket_client():
        #print(IP)
        RHOST = IP
        RPORTS = range(5000 , 6000)
        SND_DATA = b"secret"
        RCV_DATA = ""
        for RPORT in RPORTS:
            C_SOCK =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #C_SOCK.settimeout(time)
            try:
                C_SOCK.connect((RHOST,RPORT))
                use = RPORT
                #print(use)
                C_SOCK.send(SND_DATA)
                RCV_DATA = C_SOCK.recv(1024)
                C_SOCK.close()
                #return
            except socket.error as E:
                nouse = RPORT
        return (f"ANSWER: {RCV_DATA.decode()}")

#my if/elif/else responses#
if func == "1" :
    print(get_response())
elif func == "2":
    print(parse_string())
elif func == "3":
    print(parse_header())
elif func == "4":
    print(parse_json())
elif func == "5":
    print(socket_client())
else:
    print("computer says no")