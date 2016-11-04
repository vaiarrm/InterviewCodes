# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:09:21 2016

@author: vaibhavsharma
"""
# GRAPH API

class GraphNode(object):
    """
        Utility Class for saving data    
    """
    def __init__(self,key,value=None):
        self.key = key
        self.value = value

class Graph(object):
    """
        Graph API
    """    
    
    def __init__(self,vertices=None,diGraph=False):
        """
            Creates a Graph/DiGraph
        """        

        self.Graph = {}
        self.diGraph = diGraph
        if vertices:
            for v in vertices:
                self.Graph[v] = set()
    def addVertex(self,v):
        """
            Add Vertex
        """   
        if v not in self.Graph:
            self.Graph[v] = set()
            
    def addEdge(self,v1,v2):
        """
            Add Edge
        """        
        if v1 not in self.Graph:
            raise ValueError("{} not in graph".format(v1))
        if v2 not in self.Graph:
            raise ValueError("{} not in graph".format(v2))
        
        self.Graph[v1].add(v2)
        if not self.diGraph:
             self.Graph[v2].add(v1)   
    def prettyPrint(self):
        """
            Pretty Print the Graph
        """        
        for vertex in self.Graph:
            adjLst = self.Graph[vertex]
            print "{} -> ".format(vertex), 
            for item in adjLst:
                print "{} ".format(item),
            print 
    def connectedComponents(self):
        """
            Counts Connected Components
            Returns count and dictionary representing to which connected 
            component specific vertex lies
        """        
        marked = {}
        belongsTo = {}
        for key in self.Graph:
            marked[key] = False
            belongsTo[key] = None
        count = 0
        for key in self.Graph:
            if not   marked[key]:          
                count+=1
                self.__dfsCC(key,marked,count,belongsTo)
        return count,belongsTo

    def __dfsCC(self,vertex,marked,count,belongsTo):
        """
            Private method for connected components
        """        
        marked[vertex] = True
        belongsTo[vertex] = count
        for v in self.Graph[vertex]:
            if not marked[v]:
                self.__dfsCC(v,marked,count,belongsTo)
    
