"""
All the coordinates shall be stored in a list. 
Each element of the list is still a list. For example,
C   -0.44938997   -0.77759385    0.00000000
C    1.06571603   -0.77759385    0.00000000
correponds to:
[
	['C', -0.44938997, -0.77759385, 0.00000000], 
	['C',  1.06571603, -0.77759385, 0.00000000],	
]

The internal coordinates are saved with the same way:
C  3    1.51543497    2  111.24127560    1   55.25714299    0
correponds to:
[
	[C, 3, 1.51543497, 2, 111.24127560, 1, 55.25714299, 0],
]

Be aware to the index! In python, the index starts from 0 but not 1!

"""



def readCartesianCoordinatesFromFile(filename):
	cartesian = []
	return cartesian		


def readInternalCoordinatesFromFile(filename):
	internal = []
	return internal


def convertInternalCoordinatesToCartesian(internal):
	cartesian = []
	return cartesian


