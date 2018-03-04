import unittest

import script

class TestMyFunc(unittest.TestCase):


    def setUp(self):
        pass

    def test_double_value_1(self):
        self.assertEqual( script.double_number(1), 2)

    def test_increment_one_1(self):
        self.assertEqual( script.increment_by_one(0), 1)

if __name__ == '__main__':
    unittest.main()
