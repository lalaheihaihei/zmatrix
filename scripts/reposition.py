#!/usr/bin/env python
"""
put the out-cell-atoms into cell
"""
import sys,re,linecache
bestFileName = sys.argv[1]
Inp= open(bestFileName,"r")
Outp= open("reposition.xyz","w")
count = 1
for line in Inp.readlines():
    if count % 191 == 1 or count % 191 == 2:
        Outp.write(line)
        count = count + 1
        continue
    count = count + 1
    line = line.split(' ')
    while '' in line:
       line.remove('')
#    if line[0] == 'H' or line[0] == 'O' or line[0] == 'Al' or line[0] == 'Au':
    if float(line[1]) - float(line[2])/1.73 > 15:
         line[1] = float(line[1])-14.2798
#        if float(line[2]) > 5:
#            line[2] = float(line[2])-12.36666
#            line[1] = float(line[1])-7.1399
    Outp.write(line[0]+' '+str(line[1])+' '+str(line[2])+' '+str(line[3]))


Outp.close()
Inp.close()
