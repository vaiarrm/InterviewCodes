#Given N and M find all stepping numbers in range N to M
#http://www.geeksforgeeks.org/stepping-numbers/

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        s = set()
        lst = []
        for i in xrange(0,10):
            self.helper(A,B,i,s,lst)
        lst.sort()
        return lst
    def helper(self,a,b,num,s,lst):
        if num > b or num in s:
            return
        elif a <= num <= b:
            lst.append(num)
        s.add(num)
            
        ul = ( num * 10 ) + ( num % 10 ) + 1
        ll = ( num * 10 ) + ( num % 10 ) - 1
        
        if num % 10 == 0:
            self.helper(a,b,ul,s,lst)
        elif num % 10  == 9:
            self.helper(a,b,ll,s,lst)
        else:
            self.helper(a,b,ll,s,lst)
            self.helper(a,b,ul,s,lst)
        
    def stepnumBadSoln(self, A, B):
        #Quadratic Time
        toRet = []
        for i in xrange(A,B+1):
            x = i
            if x < 10:
                toRet.append(x)
                continue
            
            nl = []
            while x != 0:
                nl.append(x % 10)
                x = x / 10
            noStep = False
            for j in range(1,len(nl)):
                if abs(nl[j-1] - nl[j]) == 1:
                    continue
                else:
                    noStep = True
                    break
            if not noStep:
                toRet.append(i)
        return toRet
            
                
