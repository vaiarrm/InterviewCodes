# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 14:23:10 2016

@author: vaibhavsharma
"""
"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""
class Solution(object):
    def swap(self, people,i,j):
        temp = people[j]
        people[j] = people[i]
        people[i] = temp
        
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        people.sort() #O(NLgN)
        people.reverse() #O(N)
        print "after reverse"
        print people
        for i in range(1,len(people)): #(N^2)
            self.swap(people,i,0)
            count = 0
            for j in range(i):
                ht = people[i][0]
                num = people[i][1]
                if ht <= people[j][0]:
                    count += 1
                if count > num:
                    if j == len(people) - 1:
                        continue
                    self.swap(people,i,j)
                    self.swap(people,j,j+1)
                    count = 0
                if count == num:
                    if j == len(people) - 1:
                        continue  
                    self.swap(people,i,j)
                    self.swap(people,j,j+1)
                    count = 0
            print 
            print people

        return people
p = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
s = Solution()
s.reconstructQueue(p)                
                    
                
        