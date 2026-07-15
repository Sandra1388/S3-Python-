'''
Given a string s, find the first non-repeating character
in it and return its index. If it does not exist, return -1.

 
Example 1:

Input: s = "leetcode"

Output: 0
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        answer = None
        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        
        for i in range(0,len(s)):
            if count[s[i]] == 1:
                return i
            
        return -1

        
