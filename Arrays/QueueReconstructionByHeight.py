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
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        people.sort(key = lambda x: x[1])
        
        for i in range(1,len(people)):
            count = people[i][1]
            curr
            for j in range(i):
                if people[j][0] >= people[i][0]:
                    curr += 1
                if curr == count:
                    break
            if i == j+1:
                pass
                
        