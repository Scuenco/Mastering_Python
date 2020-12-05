import unittest
import unit_test_main

class TestMain(unittest.TestCase):
  def test_correct_guess(self):
    result = unit_test_main.random_guess(10, 10)
    self.assertTrue(result)

  def test_wrong_guess(self):
    result = unit_test_main.random_guess(1, 10)
    self.assertFalse(result)
  
  def test_wrong_number(self):
    result = unit_test_main.random_guess(5, 15)
    self.assertFalse(result)
  
  def test_wrong_type(self):
    result = unit_test_main.random_guess(5, '10')
    self.assertFalse(result)

if __name__ == "__main__":
  unittest.main()