Minimum increment/decrement to make array non-Increasing



Given an array a, your task is to convert it into a non-increasing form such
that we can either increment or decrement the array value by 1 in minimum
changes possible.

 **Examples :**

    
    
     **Input :** a[] = {3, 1, 2, 1}
    **Output :** 1
    **Explanation :**
    We can convert the array into 3 1 1 1 by
    changing 3rd element of array i.e. 2 
    into its previous integer 1 in one step
    hence only one step is required.
    
    **Input :** a[] = {3, 1, 5, 1}
    **Output :** 4
    We need to decrease 5 to 1 to make array sorted
    in non-increasing order.
    
    **Input :** a[] = {1, 5, 5, 5}
    **Output :** 4
    We need to increase 1 to 5.

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Brute-Force approach:** We consider both possibilities for every element
and find a minimum of two possibilities.

**Efficient Approach:** Calculate the sum of absolute differences between the
final array elements and the current array elements. Thus, the answer will be
the sum of the difference between the ith element and the smallest element
occurred until then. For this, we can maintain a min-heap to find the smallest
element encountered till then. In the min-priority queue, we will put the
elements and new elements are compared with the previous minimum. If new
minimum is found we will update it, this is done because each of the next
element which is coming should be smaller than the current minimum element
found till now. Here, we calculate the difference so that we can get how much
we have to change the current number so that it will be equal or less than
previous numbers encountered till. Lastly, the sum of all these differences
will be our answer as this will give the final value up to which we have to
change the elements.

Below is the implementation of the above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP code to count the change required to

// convert the array into non-increasing array

#include <bits/stdc++.h>

using namespace std;

int DecreasingArray(int a[], int n)

{

 int sum = 0, dif = 0;

 // min heap

 priority_queue<int, vector<int>, greater<int> > pq;

 // Here in the loop we will

 // check that whether the upcoming

 // element of array is less than top

 // of priority queue. If yes then we

 // calculate the difference. After

 // that we will remove that element

 // and push the current element in

 // queue. And the sum is incremented

 // by the value of difference

 for (int i = 0; i < n; i++) {

 if (!pq.empty() && pq.top() < a[i]) {

 dif = a[i] - pq.top();

 sum += dif;

 pq.pop();

 }

 pq.push(a[i]);

 }

 return sum;

}

// Driver Code

int main()

{

 int a[] = { 3, 1, 2, 1 };

 int n = sizeof(a) / sizeof(a[0]);

 cout << DecreasingArray(a, n);

 return 0;

}  
  
---  
  
 __

 __

## Java

 __

 __  
 __

 __

 __  
 __  
 __

// Java code to count the change required to

// convert the array into non-increasing array

import java.util.PriorityQueue;

class GFG

{

 public static int DecreasingArray(int a[], int n)

 {

 int sum = 0, dif = 0;

 PriorityQueue<Integer> pq = new PriorityQueue<>();

 // Here in the loop we will

 // check that whether the upcoming

 // element of array is less than top

 // of priority queue. If yes then we

 // calculate the difference. After

 // that we will remove that element

 // and push the current element in

 // queue. And the sum is incremented

 // by the value of difference

 for (int i = 0; i < n; i++)

 {

 if (!pq.isEmpty() && pq.element() < a[i])

 {

 dif = a[i] - pq.element();

 sum += dif;

 pq.remove();

 }

 pq.add(a[i]);

 }

 

 return sum;

 }

 // Driver Code

 public static void main(String[] args)

 {

 

 int[] a = {3, 1, 2, 1};

 

 int n = a.length;

 System.out.println(DecreasingArray(a, n));

 }

}

// This Code is contributed by sanjeev2552  
  
---  
  
 __

 __

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to count the change required to

# convert the array into non-increasing array

from queue import PriorityQueue

def DecreasingArray(a, n):

 

 ss, dif = (0,0)

 

 # min heap

 pq = PriorityQueue()

 # Here in the loop we will

 # check that whether the upcoming

 # element of array is less than top

 # of priority queue. If yes then we

 # calculate the difference. After

 # that we will remove that element

 # and push the current element in

 # queue. And the sum is incremented

 # by the value of difference

 for i in range(n):

 tmp = 0

 

 if not pq.empty():

 tmp = pq.get()

 pq.put(tmp)

 

 if not pq.empty() and tmp < a[i]:

 dif = a[i] - tmp

 ss += dif

 pq.get()

 

 pq.put(a[i])

 

 return ss

 

# Driver code 

if __name__=="__main__":

 

 a = [ 3, 1, 2, 1 ]

 n = len(a)

 

 print(DecreasingArray(a, n))

 

# This code is contributed by rutvik_56  
  
---  
  
 __

 __

## C#

 __

 __  
 __

 __

 __  
 __  
 __

// C# code to count the change required to

// convert the array into non-increasing array

using System;

using System.Collections.Generic;

class GFG

{

 static int DecreasingArray(int[] a, int n)

 {

 int sum = 0, dif = 0;

 

 // min heap

 List<int> pq = new List<int>();

 

 // Here in the loop we will

 // check that whether the upcoming

 // element of array is less than top

 // of priority queue. If yes then we

 // calculate the difference. After

 // that we will remove that element

 // and push the current element in

 // queue. And the sum is incremented

 // by the value of difference

 for (int i = 0; i < n; i++)

 {

 if (pq.Count > 0 && pq[0] < a[i])

 {

 dif = a[i] - pq[0];

 sum += dif;

 pq.RemoveAt(0);

 }

 pq.Add(a[i]);

 pq.Sort();

 }

 

 return sum;

 } 

 // Driver code

 static void Main()

 {

 int[] a = { 3, 1, 2, 1 };

 int n = a.Length;

 

 Console.Write(DecreasingArray(a, n));

 }

}

// This code is contributed by divyeshrabadiya07.  
  
---  
  
 __

 __

 **Output:**

    
    
    1

**Time Complexity: O(n log(n))**  
**Space Complexity:** **O(n)**  
Also see : Convert to strictly increasing array with minimum changes.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

