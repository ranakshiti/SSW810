import unittest
import os
from FinalProgramming_KshitiRana1 import readr,deftodic
from prettytable import PrettyTable
class TestAll(unittest.TestCase):
    dir = 'C:/Users/kshit/Documents/Stevens/Semester 2/SSW 810 - Special Topics - Python/HW/final/datafile/IOT_test'
    obj = readr()
    d = obj.read_iot(dir)
    l = deftodic(d)
    obj.sumary(l)
    
    def test1(self):
        self.assertEqual(self.l['light'],{'Mon': ['156', '482', '429', '542'], 'Sun': ['861']})
        self.assertEqual(self.l['rainfall'],{'Mon': ['568'], 'Sun': ['800', '259', '652']})

        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)