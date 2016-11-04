# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 11:03:13 2016

@author: vaibhavsharma
"""

from collections import deque
class BinHeap(object):
    def __init__(self):
        self.heapLst = deque()
        self.heapLst.append(0)
        self.size = 0
    def insert(self,item):
        self.heapLst.append(item)
        self.size += 1
        self.swim(len(self.heapLst)-1)
    def swim(self,i):
        while i // 2 > 0:
            if self.heapLst[i] < self.heapLst[i//2]:
                self.heapLst[i],self.heapLst[i//2] = self.heapLst[i//2],self.heapLst[i]
                i = i // 2
            else:
                break
    def sink(self,i):
        #print self.heapLst, i,self.size,"in sink start"
        while i*2 <= self.size:
            if i*2 + 1 > self.size:
                index = 2*i
            elif self.heapLst[2*i] < self.heapLst[2*i+1]:
                index = 2*i
            else:
                index = 2 * i+1
            #print self.heapLst, self.size,index,"in sink"
            if self.heapLst[i] > self.heapLst[index]:
                self.heapLst[i],self.heapLst[index] = self.heapLst[index],self.heapLst[i]
            i = index
            #print self.heapLst, i,"in sink"
    def minVal(self):
        if self.size == 0:
            raise ValueError()
        self.heapLst[1],self.heapLst[len(self.heapLst)-1] = self.heapLst[len(self.heapLst)-1],self.heapLst[1]
        toRet = self.heapLst.pop()
        self.size -= 1
        self.sink(1)
        return toRet
        
    def __str__(self):
        return str(self.heapLst)
    def __repr__(self):
        return str(self.heapLst)
        
b = BinHeap()
b.insert(5)
print b
b.insert(10)
print b
b.insert(15)
print b
b.insert(1)       
print b
print b.minVal()
#print b
print b.minVal()
#print b
print b.minVal()
#print b
print b.minVal()
#print b            
        
    