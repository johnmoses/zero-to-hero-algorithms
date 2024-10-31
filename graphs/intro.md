# Graphs

A graph is a set of objects called `vertices`, together with a collection of pairwise connections between them called `edges`. It is a way or representing relationships between pairs of objects.

The vertices are also called nodes while the edges are also called arcs. The edges can be described as `directed` if they are ordered and `undirected` if they are not ordered, and `unidirected` if all edges are undirected.

The vertices and edges may also be labeled or unlabeled. When the edges are labeled with numbers, the numbers can be viewed as weights, and the graph is said to be a weighted
graph.

Paths are a sequence of nodes for moving around the graph. They can also be described as a sequence of edges that allows
one vertex to be reached from another vertex in a graph.

A graph is said to be connected if there is a path from
each vertex to every other vertex.

A graph is also said to be complete if there is an edge from each vertex to every other vertex

Practical examples of graphs are city maps, airline routes, electrical wiring mappings, link between web pages, relationship between students and courses, communication network diagram

## Graph Representation

How do we represent a graph in the computer? Some of the most commonly used representations of graphs are the adjacency
matrix, adjacency list, dictionary.

## Starting with a simple directed graph

```python
G = (
    {1,2,3,4},
    {(1,2), (1,3), (1,4)},
)
```

The graph G has 4 vertices v and 3 edges e. It is represented pictorially as 4 labeled circles (vertices) with 3 lines (edges)