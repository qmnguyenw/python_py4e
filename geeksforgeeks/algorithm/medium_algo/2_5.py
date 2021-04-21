Proof that Hamiltonian Cycle is NP-Complete



 **Prerequisite:** NP-Completeness, Hamiltonian cycle.

 **Hamiltonian Cycle:** A cycle in an undirected graph G =(V, E) which
traverses every vertex exactly once.

 **Problem Statement:** Given a graph G(V, E), the problem is to determine if
the graph contains a Hamiltonian cycle consisting of all the vertices
belonging to V.  
 **Explanation –**  
An instance of the problem is an input specified to the problem. An instance
of the Independent Set problem is a graph G (V, E), and the problem is to
check whether the graph can have a Hamiltonian Cycle in G.  
Since an NP-Complete problem, by definition, is a problem which is both in NP
and NP-hard, the proof for the statement that a problem is NP-Complete
consists of two parts:

>   1. The problem itself is in NP class.
>   2. All other problems in NP class can be polynomial-time reducible to
> that.  
> (B is polynomial-time reducible to C is denoted as
> ![B$\\leqslant_P$C](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-450c648e7aee9c7e4c0b63041286f868_l3.png))
>

If the 2nd condition is only satisfied then the problem is called **NP-Hard**.

But it is not possible to reduce every NP problem into another NP problem to
show its NP-Completeness all the time. That is why if we want to show a
problem is NP-Complete, we just show that the problem is in **NP** and if any
**NP-Complete** problem is reducible to that, then we are done, i.e. if B is
NP-Complete and ![B$\\leqslant_P$C](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-450c648e7aee9c7e4c0b63041286f868_l3.png) for C
in NP, then C is NP-Complete.

  

  

  1.  **Hamiltonian Cycle is in NP**  
If any problem is in NP, then, given a _‘certificate’_ , which is a solution
to the problem and an instance of the problem (a graph G and a positive
integer k, in this case), we will be able to verify (check whether the
solution given is correct or not) the certificate in polynomial time.  
The certificate is a sequence of vertices forming Hamiltonian Cycle in the
graph. We can validate this solution by verifying that all the vertices belong
to the graph and each pair of vertices belonging to the solution are adjacent.
This can be done in polynomial time, that is **O(V +E)** using the following
strategy for graph G(V, E):

    
    
    flag=true
    For every pair {u, v} in the subset V’:
        Check that these two have an edge between them
        If there is no edge, set flag to false and break
    If flag is true:
        Solution is correct
    Else:
        Solution is incorrect
    

  2. **Hamiltonian Cycle is NP Hard**  
In order to prove the Hamiltonian Cycle is NP-Hard, we will have to reduce a
known NP-Hard problem to this problem. We will carry out a reduction from the
Hamiltonian Path problem to the Hamiltonian Cycle problem.  
Every instance of the Hamiltonian Path problem consisting of a graph **G =(V,
E)** as the input can be converted to Hamiltonian Cycle problem consisting of
graph **G’ = (V’, E’)**. We will construct the graph G’ in the following way:

    *  **V’** = Add vertices V of the original graph G and add an additional vertex **V new** such that all the vertices connected of the graph are connected to this vertex. The number of vertices increases by 1, **V’ =V+1**.
    *  **E’** = Add edges E of the original graph G and add new edges between the newly added vertex and the original vertices of the graph. The number of edges increases by the number of vertices V, that is, **E’=E+V**.

The new graph G’ can be obtained in polynomial time, by adding new edges to
the new vertex, that requires O(V) time. This reduction can be proved by the
following two claims:

    * Let us assume that the graph G contains a hamiltonian path covering the **V** vertices of the graph starting at a random vertex say **V start** and ending at Vend, now since we connected all the vertices to an arbitrary new vertex **V new** in G’.  
We extend the original Hamiltonian Path to a Hamiltonian Cycle by using the
edges **V end **to **V new** and Vnew to Vstart respectively. The graph **G’**
now contains the closed cycle traversing all vertices once.

    * We assume that the graph **G’** has a _Hamiltonian Cycle_ passing through all the vertices, inclusive of **V new**. Now to convert it to a _Hamiltonian Path_ , we remove the edges corresponding to the vertex **V new** in the cycle. The resultant path will cover the vertices V of the graph and will cover them exactly once.

![](https://media.geeksforgeeks.org/wp-content/uploads/20200514160443/Copy-of-
Untitled-Diagram-3-1.jpg)

Thus we can say that the graph **G’** contains a _Hamiltonian Cycle_ iff graph
**G** contains a _Hamiltonian Path_. Therefore, any instance of the
_Hamiltonian Cycle_ problem can be reduced to an instance of the _Hamiltonian
Path_ problem. Thus, the _Hamiltonian Cycle_ is **NP-Hard**.

 **Conclusion:** Since, the _Hamiltonian Cycle_ is both, a **NP-Problem** and
**NP-Hard**. Therefore, it is a **NP-Complete** problem.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

