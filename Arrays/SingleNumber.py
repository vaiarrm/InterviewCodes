# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 18:23:26 2016

@author: vaibhavsharma
"""
"""
Given an array of integers, every element appears twice except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return None
        val = 0
        for num in nums:
            val ^= num
        return val