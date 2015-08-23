#!/usr/bin/python
'''
find directions from dimervirbration.
'''
import sys,math,linecache
inp1 = open('last.xyz', "r")
inp2 = open('NEWMODECAR', "r")

out = open('newmodepos.xyz','w')
for i in range(-3,3):
    e=[]
    g=[]
    element=[]
    print >> out,("207")
    print >> out,("i")
    for j in range(3,210):
                b=linecache.getline('last.xyz',j)
                c =b.split(' ')
                element.append(c[0])
                c.pop(0)
                lst = [eval(x) for x in c]
                e.append(lst)
                print len(e)
    for k in range(1,208):
                f=linecache.getline('NEWMODECAR',k)
                f=f.strip()
                f=f.split('\t')
                lst = [eval(x) for x in f] 
                g.append(lst)
                print len(g)
    for h in range(0,207):
                print >> out,("%3s\t%12.8f\t%12.8f\t%12.8f" %(element[h],e[h][0]+g[h][0]*i/3,e[h][1]+g[h][1]*i/3,e[h][2]+g[h][2]*i/3))

out.close()
inp1.close()
inp2.close()


