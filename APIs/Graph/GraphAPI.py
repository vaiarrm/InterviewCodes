# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:09:21 2016

@author: vaibhavsharma
"""
# GRAPH API

class GraphNode(object):
    def __init__(self,key,value=None):
        self.key = key
        self.value = value

class Graph(object):
    def __init__(self,vertices=None,diGraph=False):
        self.Graph = {}
        self.diGraph = diGraph
        if vertices:
            for v in vertices:
                self.Graph[v] = []
    def addVertex(self,v):
        if v not in self.Graph:
            self.Graph[v] = []
            
    def addEdge(self,v1,v2):
        if v1 not in self.Graph:
            raise ValueError("{} not in graph".format(v1))
        if v2 not in self.Graph:
            raise ValueError("{} not in graph".format(v2))
        
        self.Graph[v1].append(v2)
        if not self.diGraph:
             self.Graph[v2].append(v1)   
    def prettyPrint(self):
        for vertex in self.Graph:
            adjLst = self.Graph[vertex]
            print "{} -> ".format(vertex), 
            for item in adjLst:
                print "{} ".format(item),
            print 
    def connectedComponents(self):
        marked = {}
        belongsTo = {}
        for key in self.Graph:
            marked[key] = False
            belongsTo[key] = None
        count = 0
        for key in self.Graph:
            count+=1
            self.dfsCC(key,marked)
        return count

    def __dfsCC(self,vertex,marked,count,belongsTo):
        marked[vertex] = True
        belongsTo[vertex] = count
        for v in self.Graph[vertex]:
            if not marked[v]:
                self.dfsCC(v,marked,count,belongsTo)
