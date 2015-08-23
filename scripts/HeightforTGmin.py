#!/usr/bin/python

#use to calculate the distribution hight of surface clusters followed TGmin
#change the best number (35)/ kind of atom'Au '/atom number(162, 169)and(0, 6)/
#Last update 2015/03/06

import linecache
e=[]
h=0
for i in range(1,35):
 e=[]
 h=0
 tem='%d' %i
 best1=('best'+tem+'.xyz')
 for a in range(190, 196, 1):
   b=linecache.getline(best1,a)
   c=b.lstrip('Au ')
   c =c.split(' ')
   lst = [eval(x) for x in c]
   d = lst[2]
   e.append(d)
 for i in range(0,6):
   for f in range(0,6 ):
     g=e[i]-e[f]
     if g > h:
       h = g
 print h
