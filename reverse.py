"""
Leetcode #7 Reverse Integer

"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        flag = False
        if x<0:
            sign = "-"
            x = x*-1
            flag = True 
        while x!=0:
            rev = rev*10 + x%10
            x = int(x/10)
            if rev > (pow(2,31)-1):
                return 0
        if flag:
            rev = rev*(-1)
        return rev
