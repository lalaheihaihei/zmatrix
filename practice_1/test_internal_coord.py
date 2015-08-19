from nose.tools import *
from internal_coord import *


class TestInternalCoord(object):

	def setup(self):
		self.internal_file = "z-matrix.gjf"
		self.cartesian_file = "cartesian.gjf"

	def test_internalToCartesian(self):
		internal = readInternalCoordinatesFromFile(self.internal_file)
		cartesian = readCartesianCoordinatesFromFile(self.cartesian_file)
		converted = convertInternalCoordinatesToCartesian(internal)

		assert_greater(len(internal), 0)
		assert_greater(len(cartesian), 0)
		assert_greater(len(converted), 0)

		assert_equal(len(internal), len(cartesian))
		assert_equal(len(cartesian), len(converted))

		for i in xrange(len(cartesian)):
			diff = map(lambda x,y : x-y, cartesian[i][1:], converted[i][1:])
			norm = sum(map(lambda x : x*x, diff))
			assert_less(norm, 0.000001)


	def teardown(self):
		pass