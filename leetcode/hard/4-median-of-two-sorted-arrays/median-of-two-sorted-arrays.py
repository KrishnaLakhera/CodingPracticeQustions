class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        temp = nums1 + nums2
        temp.sort()
        n = len(temp)
        if n % 2 == 0:
            median = (temp[n//2 -1] + temp[n//2]) / 2.0
        else:
            median = temp[n/2]
        return float(median)   
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        