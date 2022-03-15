# MIS-python
MIS ( Maximal independent set ) Algorithm in python using netwokx and numpy

An independent set of a graph is some subset of the vertices where no vertex in the subset is connected to another vertex in the subset. For example, in the graph shown below, the set of vertices (0, 2, 4) is an independent set, as is (1, 3, 5).
A wheel graph on 7 vertices showing an independent set
The Maximimum Independent Set (MIS) problem is to find an independent set with the greatest cardinality in a graph. The problem is NP-complete, but a greedy algorithm gives a good approximation.

### The algorithm is:

1. Start with the set of vertices of the graph, V and an empty set for the MIS, S

2. While V≠∅:

3.Find a vertex of minimum degree v∈V

4.Add it to S

5.Remove it and its neighbours from V
