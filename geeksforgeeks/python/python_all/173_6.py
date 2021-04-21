Minimum Increment operations to make Array unique



Given an array A[] of integers. In one move you can choose any element A[i],
and increment it by 1. The task is to return the minimum number of moves
needed to make every value in the array A[] unique.  
 **Examples** :  

    
    
    **Input** : A[] = [3, 2, 1, 2, 1, 7]
    **Output** : 6
    **Explanation** :  After 6 moves, the array could be 
    [3, 4, 1, 2, 5, 7].
    It can be shown that it is impossible for the array 
    to have all unique values with 5 or less moves.
    
    **Input** : A[] = [1, 2, 2]
    **Output** : 1
    **Explanation** : After 1 move [2 -> 3], the array could be [1, 2, 3].
    
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

A simple solution to make each duplicate value unique is to keep incrementing
it repeatedly until it is not unique. However, we might do a lot of extra
work, if we have an array of all ones.  
So, what we can do instead is to evaluate what our increments should be. If
for example, we have [1, 1, 1, 3, 5], we don’t need to process all the
increments of duplicated 1’s. We could take two ones (taken = [1, 1]) and
continue processing. Whenever we find an empty(unused value) place like 2 or 4
we can then recover that our increment will be 2-1, 4-1 respectively.  
Thus, we first count the values and for each possible value X in the array:  

  * If there are 2 or more values X in A, save the extra duplicated values to increment later.
  * If there are 0 values X in A, then a saved value gets incremented to X.

Below is the implementation of the above approach:  

## CPP

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Implementation of above approach

#include <bits/stdc++.h>

using namespace std;

// function to find minimum increment required

int minIncrementForUnique(vector<int> A)

{

 // collect frequency of each element

 unordered_map<int, int> mpp;

 for(int i:A) mpp[i]++;

 // taken is to keep count

 // of duplicate items

 int taken=0, ans=0;

 for (int x = 0; x < 100000; x++)

 {

 

 // If number is present

 // multiple times

 if (mpp[x] >= 2){

 taken += mpp[x]-1;

 ans -= x*(mpp[x]-1);

 }

 

 // If there is no x in the array

 else if(taken > 0 and mpp[x] == 0)

 {

 ans += x;

 taken--;

 }

 }

 // return answer

 return ans;

}

// Driver code

int main()

{

 vector<int> A = {3, 2, 1, 2, 1, 7};

 

 // Function Call

 cout << minIncrementForUnique(A);

 

 return 0;

}

// This code is contributed by mohit kumar 29  
  
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

// Java Implementation of above approach

import java.util.*;

class GFG

{

// function to find minimum increment required

static int minIncrementForUnique(int []A)

{

 // collect frequency of each element

 HashMap<Integer,

 Integer> mpp = new HashMap<Integer,

 Integer>();

 for(int i:A)

 {

 if(mpp.containsKey(i))

 mpp.put(i, mpp.get(i) + 1);

 else

 mpp.put(i, 1);

 }

 // array of unique values taken

 Vector<Integer> taken =

 new Vector<Integer>();

 int ans = 0;

 for (int x = 0; x < 100000; x++)

 {

 

 // If number is present

 // multiple times

 if (mpp.containsKey(x) && mpp.get(x) >= 2)

 {

 taken.add(x * (mpp.get(x)- 1));

 }

 

 // If there is no x in the array

 else if(taken.size() > 0 &&

 ((mpp.containsKey(x) &&

 mpp.get(x) == 0)||!mpp.containsKey(x)))

 {

 ans += x - taken.get(taken.size() - 1);

 taken.remove(taken.size() - 1);

 }

 }

 // return answer

 return ans;

}

// Driver code

public static void main(String[] args)

{

 int []A = {3, 2, 1, 2, 1, 7};

 

 System.out.print(minIncrementForUnique(A));

}

}

// This code is contributed by Rajput-Ji  
  
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

# Python3 Implementation of above approach

import collections

# function to find minimum increment required

def minIncrementForUnique(A):

 # collect frequency of each element

 count = collections.Counter(A)

 # array of unique values taken

 taken = []

 ans = 0

 for x in range(100000):

 if count[x] >= 2:

 taken.extend([x] * (count[x] - 1))

 elif taken and count[x] == 0:

 ans += x - taken.pop()

 # return answer

 return ans

# Driver code

A = [3, 2, 1, 2, 1, 7]

print(minIncrementForUnique(A))  
  
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

// C# Implementation of above approach

using System;

using System.Collections.Generic;

class GFG

{

 

// function to find minimum increment required

static int minIncrementForUnique(int []A)

{

 

 // collect frequency of each element

 Dictionary<int,int> mpp = new Dictionary<int,int>();

 

 foreach(int i in A)

 {

 if(mpp.ContainsKey(i))

 mpp[i] = mpp[i] + 1;

 else

 mpp.Add(i, 1);

 }

 

 // array of unique values taken

 List<int> taken = new List<int>();

 

 int ans = 0;

 

 for (int x = 0; x < 100000; x++)

 {

 if (mpp.ContainsKey(x) && mpp[x] >= 2)

 taken.Add(x * (mpp[x] - 1));

 else if(taken.Count > 0 &&

 ((mpp.ContainsKey(x) &&

 mpp[x] == 0)||!mpp.ContainsKey(x)))

 {

 ans += x - taken[taken.Count - 1];

 taken.RemoveAt(taken.Count - 1);

 }

 }

 

 // return answer

 return ans;

}

 

// Driver code

public static void Main(String[] args)

{

 

 int []A = {3, 2, 1, 2, 1, 7};

 

 Console.Write(minIncrementForUnique(A));

}

}

// This code contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    
    
    

**Time Complexity:** O(N)  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

