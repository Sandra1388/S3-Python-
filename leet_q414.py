'''
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
'''
class Solution(object):
    def thirdMax(self, nums):

        nums = list(set(nums))
        nums.sort()
        if len(nums) >= 3:
            return nums[-3]  
        else:
            return nums[-1]
