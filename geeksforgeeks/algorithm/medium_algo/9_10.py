Maximum sub-array sum after dividing array into sub-arrays based on the given
queries



Given an array **arr[]** and an integer **k** , we can cut this array at **k**
different positions where **k[]** stores the positions of all the cuts
required. The task is to print maximum sum among all the cuts after every cut
made.  
Every cut is of the form of an integer **x** where **x** denotes a cut between
**arr[x]** and **arr[x + 1]**.

 **Examples:**

>  **Input:** arr[] = {4, 5, 6, 7, 8}, k[] = {0, 2, 3, 1}  
>  **Output:**  
>  26  
> 15  
> 11  
> 8  
>  **First cut - >** {4} and {5, 6, 7, 8}. Maximum possible sum is 5 + 6 + 7 +
> 8 = 26  
>  **Second cut - >** {4}, {5, 6} and {7, 8}. Maximum sum = 15  
>  **Third cut - >** {4}, {5, 6}, {7} and {8}. Maximum sum = 11  
>  **Fourth cut - >** {4}, {5}, {6}, {7} and {8}. Maximum sum = 8
>
>  **Input:** arr[] = {1, 2, 3}, k[] = {1}  
>  **Output:**  
>  3

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive approach:** Store the resulting pieces of the array in an ArrayList
and after every cut compute linearly the maximum possible sum. But this method
would require **O(n*k)** time to answer all the queries.

  

  

 **Efficient approach:** We can represent each resulting piece of the array as
a Piece object with data members **start** (start index of this piece),
**end** (end index of this piece) and **value** (sum value of this piece). We
can store these pieces in a TreeSet and **sort them by their sum values**.
Therefore, after every cut we can get the Piece with largest sum value in
O(log(n)).

  * We have to make a prefix sum array of the array values to get the sum between two indices in constant time.
  * We have to maintain another TreeSet with start indexes of all the current pieces so that we can find the exact piece to cut. For example, for a single piece:
    1. {1, 8} -> start = 1, end = 2, value = 9 and {6, 3, 9} -> start = 3, end = 5, value = 18.
    2. In order to cut index 4, we need to cut the second piece into two pieces as {6, 3} ans {9}. So we get the start index of which piece to cut from this TreeSet.

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

// Java implementation of the approach

import java.io.IOException;

import java.io.InputStream;

import java.util.*;

 

// Comparator to sort the Pieces

// based on their sum values

class MyComp implements Comparator<Piece> {

 public int compare(Piece p1, Piece p2)

 {

 if (p2.val != p1.val)

 return p2.val - p1.val;

 if (p1.start != p2.start)

 return p2.start - p1.start;

 return 0;

 }

}

class Piece {

 int start;

 int end;

 int val;

 

 // Constructor to initialize each Piece

 Piece(int s, int e, int v)

 {

 start = s;

 end = e;

 val = v;

 }

}

 

class GFG {

 

 // Function to perform the given queries on the array

 static void solve(int n, int k, int cuts[], int A[])

 {

 

 // Prefix sum array

 int sum[] = new int[n];

 sum[0] = A[0];

 for (int i = 1; i < n; i++)

 sum[i] = sum[i - 1] + A[i];

 

 // TreeSet storing all the starts

 TreeSet<Integer> t = new TreeSet<>();

 

 // TreeSet storing the actual pieces

 TreeSet<Piece> pq = new TreeSet<>(new MyComp());

 Piece temp[] = new Piece[n];

 temp[0] = new Piece(0, n - 1, sum[n - 1]);

 

 // Added the whole array or Piece of array

 // as there is no cuts yet

 pq.add(temp[0]);

 t.add(0);

 

 for (int i = 0; i < k; i++) {

 

 // curr is the piece to be cut

 int curr = t.floor(cuts[i]);

 pq.remove(temp[curr]);

 int end = temp[curr].end;

 

 // When a piece with start = s and end = e

 // is cut at index i, two pieces are created with

 // start = s, end = i and start = i + 1 and end = e

 // We remove the previous piece and add

 // this one to the TreeSet

 temp[curr]

 = new Piece(curr, cuts[i],

 sum[cuts[i]]

 - (curr == 0 ? 0 : sum[curr - 1]));

 pq.add(temp[curr]);

 

 temp[cuts[i] + 1]

 = new Piece(cuts[i] + 1,

 end, sum[end] - sum[cuts[i]]);

 pq.add(temp[cuts[i] + 1]);

 

 t.add(curr);

 t.add(cuts[i] + 1);

 

 System.out.println(pq.first().val);

 }

 }

 

 // Driver code

 public static void main(String[] args)

 {

 

 int A[] = { 4, 5, 6, 7, 8 };

 int n = A.length;

 int cuts[] = { 0, 2, 3, 1 };

 int k = cuts.length;

 

 solve(n, k, cuts, A);

 }

}  
  
---  
  
 __

 __

 **Output:**

    
    
    26
    15
    11
    8
    

Time Complexity O(n + k Log n)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

