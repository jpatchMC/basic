#!/usr/bin/env python3

print("Name: Josh Patch")

midfile = open("slicing-file.txt","r")
midlist = midfile.readlines()
###now in list###
quote = ()
##append###
l1=(''.join(midlist[-3]))
l1= l1.replace('\n',' ')


l2=(''.join(midlist[2:5:1]))
#l2=(midlist[2:5:1])
l2= l2.replace('\n',' ')
l2=(''.join(l2))
l3=(''.join(midlist[-10:-15:-2]))
l3= l3.replace('\n',' ')
l4=(''.join(midlist[10:12:1]))
l4= l4.replace('\n',' ')
l5=(''.join(midlist[-19:-22:-1]))
l5= l5.replace('\n',' ')

#quote = quote.strip('\n')
quote = (l1,l2,l3,l4,l5)
#quote= quote.replace('\n',' ')
#quote = "<br />".join(quote.split("\n"))
quote= (''.join(quote))
print(quote)
midfile.close()