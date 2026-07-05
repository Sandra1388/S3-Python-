'''
Given an integer array nums and an integer k,
return true if there are two distinct indices i
and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    val = j-i
                    if val == k:
                        return True
        return False        
