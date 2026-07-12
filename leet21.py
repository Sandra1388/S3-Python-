'''
Given an array nums of n integers where nums[i] is in the range [1, n], return an array
of all the integers in the range [1, n] that do not appear in nums.
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):

        num_set = set(nums)
        ans = []

        for i in range(1, len(nums)+1):
            if i not in num_set:
                ans.append(i)

        return ans
