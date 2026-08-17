#125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.lower()
        result = ""
        for char in st:
            if char.isalnum():
                result +=char 
        if result == result[::-1]:
            return True
        else:
            return False
