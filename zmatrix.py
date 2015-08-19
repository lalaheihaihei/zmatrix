from atom import *
from vector import *
import numpy as np

with open("./practice_1/cartesian.gjf","r") as f:
    lines = f.readlines()
print lines

'''
read atom number.
set a Dist, in which every element represent a ...
'''
atomNumber = int(lines[0])
Dict = {}


'''
complete atoms import.
'''
for i in range(atomNumber):
    Dict[(i)] = atom()
    Dict[(i)].readCoordinate(lines[i+2].strip())
    print Dict[(i)].Atom, Dict[(i)].getCoordinate()


'''
complete vectors and import.
'''
for i in range(atomNumber):
    for j in range(i+1,atomNumber):
        Dict[(j,i)] = vector()
        Dict[(j,i)].readCoordinateForSecondAtom(lines[j+2].strip())
        Dict[(j,i)].readCoordinate(lines[i+2].strip())
#        print "vector of ", Dict[(j,i)].Atom, "->", Dict[(j,i)].secondAtom, "is", \
#            Dict[(j,i)].calculateVector()
#        print "distance between", Dict[(j,i)].Atom, "and", Dict[(j,i)].secondAtom, "is", \
#            Dict[(j,i)].calculateVectorLength()
        for k in range(j+1, atomNumber):
            Dict[(k,j,i)] = vector()
            Dict[(k,j,i)].readCoordinateForThirdAtom(lines[k+2].strip())
            Dict[(k,j,i)].readCoordinateForSecondAtom(lines[j+2].strip())
            Dict[(k,j,i)].readCoordinate(lines[i+2].strip())
            print "angle of", Dict[(k,j,i)].Atom,\
                Dict[(k,j,i)].secondAtom, Dict[(k,j,i)].thirdAtom, "is", Dict[(k,j,i)].calculateVectorAngle()
            print Dict[(k,j,i)].calculateNormalVector()

def dihedral(a,b):
    return 180-np.arccos((np.array(a).dot(np.array(b)))/np.sqrt(np.array(a).dot(np.array(a))*np.array(b).dot(np.array(b))))/(2*np.pi)*360

for i in range(3,atomNumber):
    print dihedral(Dict[(i-1,i-2,i-3)].calculateNormalVector(),Dict[(i,i-1,i-2)].calculateNormalVector())


