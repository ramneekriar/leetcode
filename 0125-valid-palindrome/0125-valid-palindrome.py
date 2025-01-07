from token import RIGHTSHIFTEQUAL


class Solution:
    def isPalindrone_1(self, s: str) -> bool:
        # This uses the built-in Python isalnum() function to check whether a char is alphanumeric
        left = 0
        right = len(s) - 1

        while left <= right:
            while left < len(s) and not s[left].isalnum():
                left += 1
            
            while right > -1 and not s[right].isalnum():
                right -= 1

            if left < len(s) and right > -1 and s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        
        return True

    def isPalindrome_2(self, s: str) -> bool:
        # This uses ASCII values to figure out whether a char is alphanumeric or not
        # lowercase: 97 to 122 (inclusive)
        # numeric: 48 to 57 (inclusive)
        left = 0
        right = len(s) - 1

        while left <= right:
            while left < len(s) and not ((97 <= ord(s[left].lower()) <= 122) or (48 <= ord(s[left].lower()) <= 57)):
                left += 1
            while right > -1 and not ((97 <= ord(s[right].lower()) <= 122) or (48 <= ord(s[right].lower()) <= 57)):
                right -= 1
            
            if left < len(s) and right > -1 and s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
    
# Time = O(n), Space = O(1)