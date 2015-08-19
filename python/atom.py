import numpy as np

class atom(object):
    """
    Define an atom
    """
    def __init__(self, Atom="H", x=0, y=0, z=0):
        """
        Define an empty atom.
        """
        self.Atom = Atom
        self.x = x
        self.y = y
        self.z = z

    def readCoordinate(self, line):
        """
        Read atoms from line. Example:
        """
        array = line.split()
        self.Atom = str(array[0])
        self.x = float(array[1])
        self.y = float(array[2])
        self.z = float(array[3])

    def getCoordinate(self):
        """
        return atom coordinate as a list.
        """
        return np.array([self.x, self.y, self.z])