import unittest
from Two_Pointers.validPalindrome import Solution 
sol = Solution()

class TestValidPalindrome(unittest.TestCase):
    def test_valid_palindrome(self):
        actual = sol.isPalindrome('A man, a plan, a canal: Panama')
        self.assertTrue(actual)
    
    def test_invalid_palindrome(self):
        actual = sol.isPalindrome('race a car')
        self.assertFalse(actual)

    def test_empty_string(self):
        actual = sol.isPalindrome(" ")
        self.assertTrue(actual)

if __name__ == '__main__':
    unittest.main()