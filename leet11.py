'''
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
'''
class Solution(object):
    def containsDuplicate(self, nums):
        
        num = set()

        for n in nums:
            if n in num:
                return True
            num.add(n)
        return False
