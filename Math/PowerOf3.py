#Given an integer, write a function to determine if it is a power of three.

#Follow up:
#Could you do it without using any loop / recursion?


from math import log10
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        ##  Below solution do not word becuase log funciton 
        ## generates a float and becuase of that accuracy is 
        ## impacted
        
        # if n <= 0: 
        #     return False
        # return log(n,3) % 1 == 0.0
        
        if n <= 0:
            return False
        temp = log10(n)/log10(3)
        return temp % 1 == 0