import unittest
from Two_Pointers.validPalindrome import isPalindrome

class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        actual = isPalindrome('A man, a plan, a canal: Panama')
        expected = True
        self.assertEqual(actual, expected)
    
    def test_invalid_palindrome(self):
        actual = isPalindrome('race a car')
        expected = False
        self.assertEqual(actual, expected)

    def test_empty_string(self):
        actual = isPalindrome(" ")
        expected = True
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()