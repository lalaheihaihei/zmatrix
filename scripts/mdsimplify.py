#!/usr/bin/python
'''
script to repick xyz from cp2k-pos* for every 10 or 20 structure.
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

O = (count//N)/20
print O

Output = open('newpos.xyz','w')
for i in range(0,O):
    for j in range(1,N+1):
		print >> Output,(linecache.getline('cp2k-pos-1.xyz',i*20*N+j)).strip()
