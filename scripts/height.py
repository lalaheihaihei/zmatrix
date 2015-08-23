#!/usr/bin/python
'''
script to find height and energy  fluctuation during MD trajectory.
'''
import sys,math,linecache


inp = open('coord.inc', "r")
lines = inp.readlines()
N = len(lines) + 2
print N
inp.close

count = -1
for count, line in enumerate(open('cp2k-pos-1.xyz', 'rU')):
    pass
count += 1
print count

O = (count//N)/10
print O

Output = open('HeightDistribution.txt','w')
for i in range(0,O):
    e=[]
    g=0
    h=0
    for j in range(N-6,N+1):
		b=linecache.getline('cp2k-pos-1.xyz',i*10*N+j)
                print b
		c=b.lstrip('Au ')
		c =c.split(' ')
                while '' in c:
                       c.remove('')
		lst = [eval(x) for x in c]
		d = lst[2]
		e.append(d)
    for k in range(0,7):
	    for f in range(0,7):
		   g=e[k]-e[f]
		   if g > h:
		      h = g
    energyline=linecache.getline('cp2k-pos-1.xyz',i*10*N+2)
    print energyline
    energyline = energyline.split(' ')
    energy  = energyline[-1]
    print energy
    initial = linecache.getline('cp2k-pos-1.xyz',2)
    initial = initial.split(' ')
    energyinitial = initial[-1]
    eV = 27.2*(float(energy) - float(energyinitial))
    print eV
    print h
    print >> Output,h,eV
