import unittest
from mystatlib import stat
from unittest import mock

arr = [1, 2, 3]
class TestStatMethods(unittest.TestCase):
    def test_mean(self):
        mean = stat.mean(arr)
        self.assertEqual(mean, 2)

    def test_variance_int(self):
        variance = stat.variance(arr)
        self.assertEqual(variance, 2/3)

    def test_variance_unit(self):
        with mock.patch('mystatlib.stat.mean') as mocked_mean:
            mocked_mean.side_effect = [2, 2/3]
            variance = stat.variance(arr)
            mocked_mean.assert_called_with([1, 0, 1]) #checks last call
            self.assertEqual(variance, 2/3)
        
if '__name__' == '__main__':
    unittest.main()

