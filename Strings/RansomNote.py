# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 08:37:17 2016

@author: vaibhavsharma
"""
"""
Given an arbitrary ransom note string and another 
string containing letters from all the magazines, write a function that will return true 
if the ransom  note can be constructed from the magazines ; otherwise, it will return false. 

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true


"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) == 0:
            return True
        if len(ransomNote) > len(magazine):
            return False
        rdic = {}
        for char in ransomNote:
            rdic.setdefault(char,ransomNote.count(char))
        for key,value in rdic.iteritems():
            if not value <= magazine.count(key):
                return False
        return True