Difference between Backtracking and Branch-N-Bound technique



Algorithms are the methodical sequence of steps which are defined to solve
complex problems.

In this article, we will see the difference between two such algorithms which
are backtracking and branch and bound technique.

Before getting into the differences, lets first understand each of these
algorithms.

**Backtracking:** Backtracking is a general algorithm for finding all the
solutions to some computational problems, notably constraint satisfaction
problems, that incrementally builds possible candidates to the solutions and
abandons a candidate as soon as it determines that the candidate cannot
possibly be completed to finally become a valid solution. It is an
algorithmic-technique for solving problems recursively by trying to build a
solution incrementally, one piece at a time, removing those solutions that
fail to satisfy the constraints of the problem at any point of time (by time,
here, is referred to the time elapsed till reaching any level of the search
tree).

**Branch and Bound:** Branch and bound is an algorithm design paradigm for
discrete and combinatoric optimisation problems, as well as mathematical
optimisation. A branch-and-bound algorithm consists of a systematic
enumeration of candidate solutions. That is, the set of candidate solutions is
thought of as forming a rooted tree with the full set at the root. The
algorithm explores branches of this tree, which represent the subsets of the
solution set. Before enumerating the candidate solutions of a branch, the
branch is checked against upper and lower estimated bounds on the optimal
solution and is discarded if it cannot produce a better solution than the best
one found so far by the algorithm.

  

  

The following table explains the difference between both the algorithms:

****  
  
**Parameter**|  **Backtracking**|  **Branch and Bound**

