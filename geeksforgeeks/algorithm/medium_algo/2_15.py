Check if an array can be formed by merging 2 non-empty permutations



Given an array **arr[]** of length **N** , the task is to check if it can be
formed by merging two permutations of the same or different lengths. Print
**YES** if such merging is possible. Otherwise, print **NO**.

> Permutations of length 3 are {1, 2, 3}, {2, 3, 1}, {1, 3, 2}, {3, 1, 2}, {3,
> 2, 1}, {2, 1, 3}.

**Examples:**

> **Input:** arr = [1, 3, 2, 4, 3, 1, 2]  
> **Output:** YES  
> **Explanation:**  
> The given array can be formed by merging a permutation of length 4 [1, 3, 2,
> 4] and permutation of length 3 [3, 1, 2]
>
>  **Input:** arr = [1, 2, 3, 2, 3, 2, 1]  
> **Output:** NO  
>
>
>  
>
>
>  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach :**  
We can observe that the minimum excludant (MEX) of a permutation of length
**N** is **N+1**.  
So, if the length of the first permutation is **l** , then MEX of the prefix
**arr [0 …… l-1]** is **l+1** and the MEX of the suffix **a[l …… n]** will be
**N – l + 1**.  
So, we can calculate MEX of prefix and suffixes and if the above condition is
satisfied, the answer will be **“YES”**. Otherwise, the answer will be
**“NO”**.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the

// above approach

#include<bits/stdc++.h>

using namespace std;

void if_merged_permutations(int a[],

 int n)

{

 int pre_mex[n];

 // Calculate the mex of the

 // array a[0...i]

 int freq[n + 1];

 

 memset(freq, 0, sizeof(freq));

 

 for(int i = 0; i < n; i++)

 {

 pre_mex[i] = 1;

 }

 // Mex of empty

 // array is 1

 int mex = 1;

 // Calculating the frequency

 // of array elements

 for(int i = 0; i < n; i++)

 {

 freq[a[i]]++;

 if(freq[a[i]] > 1)

 {

 // In a permutation

 // each element is

 // present one time,

 // So there is no chance

 // of getting permutations

 // for the prefix of

 // length greater than i

 break;

 }

 // The current element

 // is the mex

 if(a[i] == mex)

 {

 // While mex is present

 // in the array

 while(freq[mex] != 0)

 {

 mex++;

 }

 }

 pre_mex[i] = mex;

 }

 

 int suf_mex[n];

 

 for(int i = 0; i < n; i++)

 {

 suf_mex[i] = 1;

 }

 

 // Calculate the mex of the

 // array a[i..n]

 memset(freq, 0, sizeof(freq));

 // Mex of empty

 // array is 1

 mex = 1;

 // Calculating the frequency

 // of array elements

 for(int i = n - 1; i > -1; i--)

 {

 freq[a[i]]++;

 if(freq[a[i]] > 1)

 {

 // In a permutation each

 // element is present

 // one time, So there is

 // no chance of getting

 // permutations for the

 // suffix of length lesser

 // than i

 continue;

 }

 

 // The current element is

 // the mex

 if(a[i] == mex)

 {

 // While mex is present

 // in the array

 while(freq[mex] != 0)

 {

 mex++;

 }

 }

 suf_mex[i] = mex;

 }

 // Now check if there is atleast

 // one index i such that mex of

 // the prefix a[0..i]= i +

 // 2(0 based indexing) and mex

 // of the suffix a[i + 1..n]= n-i

 for(int i = 0; i < n - 1; i++)

 {

 if(pre_mex[i] == i + 2 &&

 suf_mex[i + 1] == n - i)

 {

 cout << "YES" << endl;

 return;

 }

 }

 cout << "NO" << endl;

}

// Driver code

int main()

{

 int a[] = {1, 3, 2,

 4, 3, 1, 2};

 int n = sizeof(a)/ sizeof(a[0]);

 if_merged_permutations(a, n); 

}

//This code is contributed by avanitrachhadiya2155  
  
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

// Java program for above approach

import java.util.*;

import java.lang.*;

import java.io.*;

class GFG{

static void if_merged_permutations(int a[],

 int n)

{

 int[] pre_mex = new int[n];

 // Calculate the mex of the

 // array a[0...i]

 int[] freq = new int[n + 1];

 

 for(int i = 0; i < n; i++)

 {

 pre_mex[i] = 1;

 }

 // Mex of empty

 // array is 1

 int mex = 1;

 // Calculating the frequency

 // of array elements

 for(int i = 0; i < n; i++)

 {

 freq[a[i]]++;

 

 if (freq[a[i]] > 1)

 {

 

 // In a permutation

 // each element is

 // present one time,

 // So there is no chance

 // of getting permutations

 // for the prefix of

 // length greater than i

 break;

 }

 // The current element

 // is the mex

 if (a[i] == mex)

 {

 

 // While mex is present

 // in the array

 while (freq[mex] != 0)

 {

 mex++;

 }

 }

 pre_mex[i] = mex;

 }

 

 int[] suf_mex = new int[n];

 

 for(int i = 0; i < n; i++)

 {

 suf_mex[i] = 1;

 }

 

 // Calculate the mex of the

 // array a[i..n]

 Arrays.fill(freq, 0);

 // Mex of empty

 // array is 1

 mex = 1;

 // Calculating the frequency

 // of array elements

 for(int i = n - 1; i > -1; i--)

 {

 freq[a[i]]++;

 

 if (freq[a[i]] > 1)

 {

 

 // In a permutation each

 // element is present

 // one time, So there is

 // no chance of getting

 // permutations for the

 // suffix of length lesser

 // than i

 continue;

 }

 

 // The current element is

 // the mex

 if (a[i] == mex)

 {

 

 // While mex is present

 // in the array

 while (freq[mex] != 0)

 {

 mex++;

 }

 }

 suf_mex[i] = mex;

 }

 // Now check if there is atleast

 // one index i such that mex of

 // the prefix a[0..i]= i +

 // 2(0 based indexing) and mex

 // of the suffix a[i + 1..n]= n-i

 for(int i = 0; i < n - 1; i++)

 {

 if (pre_mex[i] == i + 2 &&

 suf_mex[i + 1] == n - i)

 {

 System.out.println("YES");

 return;

 }

 }

 System.out.println("NO");

}

 

// Driver code

public static void main(String[] args)

{

 int a[] = { 1, 3, 2, 4, 3, 1, 2 };

 int n = a.length;

 

 if_merged_permutations(a, n); 

}

}

// This code is contributed by offbeat  
  
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

# Python3 program for above approach

def if_merged_permutations(a, n):

 pre_mex =[1 for i in range(n)]

 

 # Calculate the mex of the

 # array a[0...i]

 freq =[0 for i in range(n + 1)]

 

 # Mex of empty array is 1

 mex = 1

 

 # Calculating the frequency

 # of array elements

 for i in range(n):

 freq[a[i]]+= 1

 if freq[a[i]]>1:

 # In a permutation

 # each element is

 # present one time,

 # So there is no chance

 # of getting permutations

 # for the prefix of

 # length greater than i

 break

 

 # The current element

 # is the mex 

 if a[i]== mex:

 

 # While mex is present

 # in the array

 while freq[mex]!= 0 :

 mex+= 1

 pre_mex[i]= mex

 

 suf_mex =[1 for i in range(n)]

 

 # Calculate the mex of the

 # array a[i..n]

 freq =[0 for i in range(n + 1)]

 

 # Mex of empty array is 1

 mex = 1

 

 # Calculating the frequency

 # of array elements

 for i in range(n-1, -1, -1):

 freq[a[i]]+= 1

 if freq[a[i]]>1:

 # In a permutation each

 # element is present

 # one time, So there is

 # no chance of getting

 # permutations for the

 # suffix of length lesser

 # than i

 break

 # The current element is

 # the mex

 if a[i]== mex:

 # While mex is present

 # in the array

 while freq[mex]!= 0 :

 mex+= 1

 suf_mex[i]= mex

 # Now check if there is atleast

 # one index i such that mex of

 # the prefix a[0..i]= i +

 # 2(0 based indexing) and mex

 # of the suffix a[i + 1..n]= n-i

 for i in range(n-1):

 if pre_mex[i]== i + 2 and suf_mex[i + 1]==
n-i:

 print("YES")

 return

 print("NO")

 

a =[1, 3, 2, 4, 3, 1, 2] 

n = len(a) 

if_merged_permutations(a, n)  
  
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

// C# program for above approach

using System;

class GFG{

 

static void if_merged_permutations(int[] a,

 int n)

{

 int[] pre_mex = new int[n];

 

 // Calculate the mex of the

 // array a[0...i]

 int[] freq = new int[n + 1];

 

 for(int i = 0; i < n; i++)

 {

 pre_mex[i] = 1;

 }

 

 // Mex of empty

 // array is 1

 int mex = 1;

 

 // Calculating the frequency

 // of array elements

 for(int i = 0; i < n; i++)

 {

 freq[a[i]]++;

 

 if (freq[a[i]] > 1)

 {

 

 // In a permutation

 // each element is

 // present one time,

 // So there is no chance

 // of getting permutations

 // for the prefix of

 // length greater than i

 break;

 }

 

 // The current element

 // is the mex

 if (a[i] == mex)

 {

 

 // While mex is present

 // in the array

 while (freq[mex] != 0)

 {

 mex++;

 }

 }

 pre_mex[i] = mex;

 }

 

 int[] suf_mex = new int[n];

 

 for(int i = 0; i < n; i++)

 {

 suf_mex[i] = 1;

 }

 

 // Calculate the mex of the

 // array a[i..n]

 Array.Fill(freq, 0);

 

 // Mex of empty

 // array is 1

 mex = 1;

 

 // Calculating the frequency

 // of array elements

 for(int i = n - 1; i > -1; i--)

 {

 freq[a[i]]++;

 

 if (freq[a[i]] > 1)

 {

 

 // In a permutation each

 // element is present

 // one time, So there is

 // no chance of getting

 // permutations for the

 // suffix of length lesser

 // than i

 continue;

 }

 

 // The current element is

 // the mex

 if (a[i] == mex)

 {

 

 // While mex is present

 // in the array

 while (freq[mex] != 0)

 {

 mex++;

 }

 }

 suf_mex[i] = mex;

 }

 

 // Now check if there is atleast

 // one index i such that mex of

 // the prefix a[0..i]= i +

 // 2(0 based indexing) and mex

 // of the suffix a[i + 1..n]= n-i

 for(int i = 0; i < n - 1; i++)

 {

 if (pre_mex[i] == i + 2 &&

 suf_mex[i + 1] == n - i)

 {

 Console.WriteLine("YES");

 return;

 }

 }

 Console.WriteLine("NO");

}

// Driver Code

static void Main()

{

 int[] a = { 1, 3, 2, 4, 3, 1, 2 };

 int n = a.Length;

 

 if_merged_permutations(a, n);

}

}

// This code is contributed by divyeshrabadiya07  
  
---  
  
 __

 __

 **Output:**

    
    
    YES

**Time Complexity:** _O(N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

