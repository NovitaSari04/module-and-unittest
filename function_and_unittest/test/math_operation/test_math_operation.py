import os
import sys
import unittest

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(current_dir + "/../../src/service"))

from math_operation import function

class MathOperationTest(unittest.TestCase):
    def test_math_operation(self):
        plus1_actual_output = function(2,10,"plus1")
        print(plus1_actual_output)
        plus1_expected_output = [2, 3, 4, 5, 6, 7, 8, 9, 10]

        fibonaci_actual_output = function(2,10,"fibonaci")
        print(fibonaci_actual_output)
        fibonaci_expected_output = [2, 3, 5, 8]

        kuadrat_actual_output = function(2,10,"kuadrat")
        print(kuadrat_actual_output)
        kuadrat_expected_output = [2, 4, 8]

        self.assertEqual(plus1_actual_output, plus1_expected_output)
        self.assertEqual(fibonaci_actual_output, fibonaci_expected_output)
        self.assertEqual(kuadrat_actual_output, kuadrat_expected_output)

if __name__ == '__main__':
    unittest.main()