import unittest


class DoesThisTest(unittest.TestCase):
	def test_something(self):
		assert sum([1, 2, 3]) == 6, "Should be 6"

	def test_something_else(self):
		self.assertEqual(True, True)


if __name__ == '__main__':
	unittest.main()
