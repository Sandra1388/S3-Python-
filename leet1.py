'''
sample i/p and o/p
Input: nums = [3,2,4], target = 6
Output: [1,2]
'''

class Solution(object):
    def twoSum(self, nums, target):
       for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return[i,j]                
