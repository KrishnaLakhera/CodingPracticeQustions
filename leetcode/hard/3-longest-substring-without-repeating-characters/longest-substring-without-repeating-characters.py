class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0
        x=0
        l1=[]
        for i in s:
            if i in l1:
                x=max(x,len(l1))
                a=l1.index(i)
                l1=l1[a+1:]

           
            l1.append(i) 
        return max(x,len(l1))
        """
        :type s: str
        :rtype: int
        """
        