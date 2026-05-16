class Solution(object):
    def twoSum(self, nums, target):
        a= len(nums)
        for i in range (0,a) :
            for j in range (i+1,a):
                if nums[i]+nums[j]==target :
                    l1=[i,j]
                    return l1

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
