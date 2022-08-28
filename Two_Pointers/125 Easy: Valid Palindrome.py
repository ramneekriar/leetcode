class Solution:
    def isPalindrome(self, s: str) -> bool:
            left, right = 0, len(s) - 1
            
            while left < right:
                while left < right and not self.alnum(s[left]):
                    left += 1
                while right > left and not self.alnum(s[right]):
                    right -= 1
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1
            return True
        
    def alnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

    def isPalindrome_2(self, s:str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left<right:
            if s[left].lower()==s[right].lower():
                left+=1
                right-=1
                continue
            
            elif not (65<=ord(s[left])<=90 or 97<=ord(s[left])<=122 or 48<= ord(s[left])<=57):
                left+=1
            elif  not (65<=ord(s[right])<=90 or 97<=ord(s[right])<=122 or 48<=ord(s[right])<=57):
                right-=1
            else:
                return False
        return True