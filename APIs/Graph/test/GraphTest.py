# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 21:25:50 2016

@author: vaibhavsharma
"""



def UndirectedGraphTest():
    G = Graph(vertices = range(10))
    G.addEdge(1,9)
    G.addEdge(1,9)
    G.addEdge(1,8)
    G.addEdge(2,5)
    G.addEdge(3,9)
    G.addEdge(2,9)
    G.addEdge(1,9)
    G.addEdge(1,5)
    G.addEdge(3,6)
    G.addEdge(7,6)
    
    G.prettyPrint()
    print G.connectedComponents()[0]

def DirectedGraphTest():
    G = Graph(vertices = range(6),diGraph=True)
    G.addEdge(1,2)
    G.addEdge(2,3)
    G.addEdge(4,3)
    G.addEdge(1,5)
    #G.addEdge(4,1)
    G.addEdge(5,4)
    
    G.prettyPrint()
    print G.connectedComponents()[0]
    print G.hasCycle()
