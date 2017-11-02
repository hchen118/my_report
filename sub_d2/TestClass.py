import unittest


def FuncAddNumber(first, second):
	result = first + second
	return result
	

class addTestCase(unittest.TestCase):

 	def test_add_func1(self):
 		result = FuncAddNumber(3,5)
 		self.assertEqual(result, 8)

	def test_add_func1(self):
 		result = FuncAddNumber(6,7)
 		self.assertEqual(result, 13)

unittest.main()