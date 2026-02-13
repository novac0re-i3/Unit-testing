import unittest 
import cal2

class test_cal(unittest.TestCase):
    def test_add(self): 
        result1=cal2.add(1,2)
        self.assertEqual(result1, 3)
        result2=cal2.add(-1,2)
        self.assertEqual(result2, 1)
        result3=cal2.add(-1,-2)
        self.assertEqual(result3, -3)
        
    def test_subtract(self): 
        result4=cal2.subtract(1,2)
        self.assertEqual(result4, -1)
        result5=cal2.subtract(-1,2)
        self.assertEqual(result5, -3)
        result6=cal2.subtract(-1,-2)
        self.assertEqual(result6, 1)
        
    def test_multiply(self): 
        result7=cal2.multiply(1,2)
        self.assertEqual(result7, 2)
        result8=cal2.multiply(-1,2)
        self.assertEqual(result8, -2)
        result9=cal2.multiply(-1,-2)
        self.assertEqual(result9, 2)
        
    def test_divide(self): 
        result10=cal2.divide(1,2)
        self.assertEqual(result10, 0.5)
        result11=cal2.divide(-1,2)
        self.assertEqual(result11, -0.5)
        result12=cal2.divide(-1,-2)
        self.assertEqual(result12, 0.5)
        
        
        
if __name__ == "__main__":
    unittest.main()