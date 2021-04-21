Difference between NP hard and NP complete problem



 **Prerequisite:** NP-Completeness

**NP Problem:**  
The NP problems set of problems whose solutions are hard to find but easy to
verify and are solved by Non-Deterministic Machine in polynomial time.

**NP-Hard Problem** **:**  
A Problem X is NP-Hard if there is an NP-Complete problem Y, such that Y is
reducible to X in polynomial time. NP-Hard problems are as hard as NP-Complete
problems. NP-Hard Problem need not be in NP class.

 **NP-Complete Problem** **:**

A problem X is NP-Complete if there is an NP problem Y, such that Y is
reducible to X in polynomial time. NP-Complete problems are as hard as NP
problems. A problem is NP-Complete if it is a part of both NP and NP-Hard
Problem. A non-deterministic Turing machine can solve NP-Complete problem in
polynomial time.

  

  

**_Difference between NP-Hard and NP-Complete_** : NP-hard| NP-Complete| NP-
Hard problems(say X) can be solved if and only if there is a NP-Complete
problem(say Y) that can be reducible into X in polynomial time.| NP-Complete
problems can be solved by a annon-deterministic Algorithm/Turing Machine in
polynomial time.| To solve this problem, do not have to be in NP .| To solve
this problem, it must be both NP and NP-hard problems.| Do not have to be a
Decision problem.| It is exclusively a Decision problem.| Example: Halting
problem, Vertex cover problem, Circuit-satisfiability problem, etc.| Example:
Determine whether a graph has a Hamiltonian cycle, Determine whether a Boolean
formula is satisfiable or not, etc.  
---|---  
  
Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

