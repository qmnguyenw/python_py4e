Shortest Superstring Problem | Set 2 (Using Set Cover)



Given a set of n strings S, find the smallest string that contains each string
in the given set as substring. We may assume that no string in arr[] is
substring of another string.

Examples:

    
    
    Input:  S = {"001", "01101", "010"}
    Output: 0011010  
    
    Input:  S = {"geeks", "quiz", "for"}
    Output: geeksquizfor
    
    Input:  S = {"catg", "ctaagt", "gcta", "ttca", "atgcatc"}
    Output: gctaagttcatgcatc

In the previous post, we have discussed a solution that is proved to be 4
approximate (conjectured as 2 approximate).  
In this post, a solution is discussed that can be proved as 2Hn approximate.
where Hn = 1 + 1/2 + 1/3 + … 1/n. The idea is to transform Shortest
Superstring problem into Set Cover problem (The Set cover problem is given
some subsets of a universe and every give subset has an associated cost. The
task is to find the lowest cost set of given subsets such that all elements of
universe are covered). For a Set Cover problem, we need to have a universe and
subsets of universe with their associated costs.

Below are steps to transform Shortest Superstring into Set Cover.

    
    
    1) Let S be the set of given strings.
       S = {s1, s2, ... sn}
    
    2) Universe for Set Cover problem is S (We need
       to find a superstring that has every string
       as substring)
    
    3) Let us initialize subsets to be considered for universe as
         Subsets =  {{s1}, {s2}, ... {sn}}
       Cost of every subset is length of string in it.
    
    3) For all pairs of strings si and sj in S,
         If si and sj overlap
          a) Construct a string rijk where k is
             the maximum overlap between the two.
          b) Add the set represented by rijk to Subsets,
               i.e., Subsets = Subsets U Set(rijk)
             The set represented by rijk is the set 
             of all strings which are substring of it.
             Cost of the subset is length of rijk.
    
    4) Now problem is transformed to Set Cover, we can 
       run Greedy Set Cover approximate algorithm to find
       set cover of S using Subsets.  Cost of every element in
       Subsets is length of string in it.
    

**Example:**

  

  

    
    
    S = {s1, s2, s3}.
    s1 = "001"
    s2 = "01101"
    s3 = "010"
    
    [Combination of s1 and s2 with 2 overlapping characters]
    r122 = 001101 
    
    [Combination of s1 and s3 with 2 overlapping characters]
    r132 = 0010 
    
    Similarly,
    r232 = 011010
    r311 = 01001
    r321 = 0101101
    
    **Now set cover problem becomes as following:**
    
    **Universe** to cover is {s1, s2, s3}
    
    **Subsets of the universe and their costs :**
    
    {s1}, cost 3 (length of s1)
    {s2}, cost 5 (length of s2)
    {s3}, cost 5 (length of s3)
    
    set(r122), cost 6 (length of r122)
    The set r122 represents all strings which are
    substrings of r122. 
    Therefore set(r122) = {s1, s2}
    
    set(r132), cost 3 (length of r132)
    The subset r132 represents all strings which are
    substrings of r132
    Therefore set(r132) = {s1, s3}
    
    Similarly there are more subsets for set(r232), 
    set(r311), and set(r321).
    
    So we have a set cover problem with universe and subsets
    of universe with costs associated with every subset.
    

We have discussed that an instance of Shortest Superstring problem can be
transformed into an instance of Set Cover problem in polynomial time.

Refer this for proof of the fact that Set Cover based algorithm is 2Hn
approximate.

 **Reference:**  
http://www.cs.dartmouth.edu/~ac/Teach/CS105-Winter05/Notes/wan-ba-notes.pdf  
http://fileadmin.cs.lth.se/cs/Personal/Andrzej_Lingas/superstring.pdf  
http://math.mit.edu/~goemans/18434S06/superstring-lele.pdf

This article is contributed **Dheeraj Gupta**. Please write comments if you
find anything incorrect, or you want to share more information about the topic
discussed above

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

