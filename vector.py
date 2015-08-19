from atom import *
import numpy as np

class vector(atom):
    """
    Define an vector
    """
    def __init__(self, secondAtom='H', x2=1, y2=1, z2=1, thirdAtom='H', x3=2, y3=2, z3=2):
        """
        Define an empty vector.
        """
        self.secondAtom = secondAtom
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.thirdAtom = thirdAtom
        self.x3 = x3
        self.y3 = y3
        self.z3 = z3


    def readCoordinateForSecondAtom(self, line):
        """
        read the second atom.
        """
        array = line.split()
        self.secondAtom = str(array[0])
        self.x2 = float(array[1])
        self.y2 = float(array[2])
        self.z2 = float(array[3])

    def readCoordinateForThirdAtom(self, line):
        '''
        This def for angle, just a temp code.
        '''
        array = line.split()
        self.thirdAtom = str(array[0])
        self.x3 = float(array[1])
        self.y3 = float(array[2])
        self.z3 = float(array[3])

    def calculateVector(self):
        vx = self.x2 - self.x
        vy = self.y2 - self.y
        vz = self.z2 - self.z
        return [vx,vy,vz]

    def calculateVector2(self):
        vx1 = self.x3 - self.x2
        vy1 = self.y3 - self.y2
        vz1 = self.z3 - self.z2
        return [vx1,vy1,vz1]

    def calculateVectorLength(self):
        return np.sqrt(np.array(self.calculateVector()).dot(np.array(self.calculateVector())))

    def calculateVectorLength2(self):
        return np.sqrt(np.array(self.calculateVector2()).dot(np.array(self.calculateVector2())))


    def calculateVectorAngle(self):
        return 180-(np.arccos(np.array(self.calculateVector()).dot(np.array(self.calculateVector2()))\
                   /(self.calculateVectorLength()*self.calculateVectorLength2())))/(2*np.pi) * 360

    def calculateNormalVector(self):
        list = [self.calculateVector()[-1],self.calculateVector()[-1]]
        a=self.calculateVector()
        b=self.calculateVector2()
        a.pop()
        b.pop()
        x = np.linalg.solve([a,b],list)
        return [x[0],x[1],1]
