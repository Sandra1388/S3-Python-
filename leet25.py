#680. Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s == s[::-1]:
            return True
        else:
            left = 0
            right = len(s)-1
            while(left < right):
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    skip_left = s[left+1:right+1]
                    skip_right = s[left:right]
                    if skip_left == skip_left[::-1] or skip_right == skip_right[::-1]:
                        return True
                    else:
                        return False
