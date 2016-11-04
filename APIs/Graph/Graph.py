# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 20:09:21 2016

@author: vaibhavsharma
"""
# GRAPH API

from collections import deque

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

        self.__Graph = {}
        self.__diGraph = diGraph
        self.__V = 0
        self.__E = 0
        if vertices:
            for v in vertices:
                self.__Graph[v] = deque()
            self.__V = len(vertices)
    def addVertex(self,v):
        """
            Add Vertex
        """   
        if v not in self.__Graph:
            self.__Graph[v] = deque()
            self.__V += 1
            
    def addEdge(self,v1,v2):
        """
            Add Edge
        """        
        if v1 not in self.__Graph:
            raise ValueError("{} not in graph".format(v1))
        if v2 not in self.__Graph:
            raise ValueError("{} not in graph".format(v2))
        
        self.__Graph[v1].append(v2)
        if not self.__diGraph:
             self.__Graph[v2].append(v1)  
        self.__E += 1
        
    def getNumVertices(self):
        """
            Returns Number of Vertices
        """        
        return self.__V

    def getNumEdges(self):
        """
            Returns Number of Edges
        """        
        return self.__E
            
    def getGraph(self):
        """
            Returns Graph
        """        
        return self.__Graph

    def prettyPrint(self):
        """
            Pretty Print the Graph
        """        
        for vertex in self.__Graph:
            adjLst = self.__Graph[vertex]
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
        for key in self.__Graph:
            marked[key] = False
            belongsTo[key] = None
        count = 0
        for key in self.__Graph:
            if not   marked[key]:          
                count+=1
                self.__dfsCC(key,marked,count,belongsTo)
        return count,belongsTo

    def hasCycle(self):
        """
            Detects cycle
            Returns true if cycle is present else False
        """        
        if not self.__diGraph and self.hasParallelEdges():    
            return True
        elif self.hasSelfLoop():
            return True
        elif self.__diGraph:
            return self.__hasCycleForDiGraph()
        elif not self.__diGraph:
            return self.__hasCycleForUnDiGraph()
    

    
    def hasSelfLoop(self):
        """
            Detects self loop
            Returns true if self loop is present else False
        """        
        for key in self.__Graph:
            adjLst = self.__Graph[key]
            for item in adjLst:
                if item == key:
                    return True
        return False

    def hasParallelEdges(self):
        """
            Detects Parallel Edges
            Returns true if parallel edges is present else False
        """        
        if self.__diGraph:
            raise 
        for key in self.__Graph:
            temp = set()
            adjLst = self.__Graph[key]
            for item in adjLst:
                if item in temp:
                    return True
        return False

    def topologicalSort(self):
        """
            Implementation of topological sort for Directed Graph
        """
        pass

    def __dfsCC(self,vertex,marked,count,belongsTo):
        """
            Private method for connected components
        """        
        marked[vertex] = True
        belongsTo[vertex] = count
        for v in self.__Graph[vertex]:
            if not marked[v]:
                self.__dfsCC(v,marked,count,belongsTo)
    
    def __hasCycleForUnDiGraph(self):
        """
            Private method for finding cycle in undirected graph
        """        
        marked = {}
        edgeTo = {}
        for key in self.__Graph:
            marked[key] = False
            edgeTo[key] = -1
        for key in self.__Graph:
            if not marked[key]:
                if self.__dfsHCFUG(key,marked,edgeTo):
                    return True
        return False
            
    def __dfsHCFUG(self,v,marked,edgeTo):
        """
            Private method for finding cycle in undirected graph
        """
        marked[v] = True
        for w in self.__Graph[v]:
            if not marked[w]:
                edgeTo[w] = v
                if self.__dfsHCFUG(w,marked,edgeTo):
                    return True
            else:
                if edgeTo[v] != w:
                    return True
        return False
     
    def __hasCycleForDiGraph(self):
        """
            Private method for finding cycle in directed graph
        """        
        marked = {}
        edgeTo = {}
        onStack ={}
        for key in self.__Graph:
            marked[key] = False
            onStack[key] = False            
            edgeTo[key] = -1
        for key in self.__Graph:
            if not marked[key]:
                if self.__dfsHCFDG(key,marked,edgeTo,onStack):
                    return True
        return False    

    def __dfsHCFDG(self,v,marked,edgeTo,onStack):
        """
            Private method for finding cycle in directed graph
        """            
        marked[v] = True
        onStack[v] = True
        for w in self.__Graph[v]:
            if onStack[w]:
                return True
            if not marked[w]:
                edgeTo[w] = v
                if self.__dfsHCFDG(w,marked,edgeTo,onStack):
                    return True
        onStack[v] = False
        return False
        
        
        
        
        
        
        
        
        
        
        
        

            