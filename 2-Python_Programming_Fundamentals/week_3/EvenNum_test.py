import unittest
import EvenNum

class TestEven(unittest.TestCase):
    
    def test_EvenNum(self):
        result = EvenNum.EvenNum(10)
        self.assertEqual(result, True)
        self.assertEqual(EvenNum.EvenNum(0), True)
        self.assertEqual(EvenNum.EvenNum(9), False)
        self.assertEqual(EvenNum.EvenNum(-12), True)
                        
if __name__ == '__main__':
    unittest.main()
