Count unique subsequences of length K



Given an array of N numbers and an integer K. The task is to print the number
of unique subsequences possible of length K.  
Examples:

    
    
    Input : a[] = {1, 2, 3, 4}, k = 3 
    Output : 4. 
    Unique Subsequences are: 
    {1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}
    
    Input: a[] = {1, 1, 1, 2, 2, 2 }, k = 3
    Output : 4 
    Unique Subsequences are 
    {1, 1, 1}, {1, 1, 2}, {1, 2, 2}, {2, 2, 2} 
    
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** There is a well-known formula how many subsequences of fixed
length K can be chosen from N unique objects. But the problem here has several
differences. One among them is the order in subsequences is important and must
be preserved as in the original sequence. For such a problem there can be no
ready combinatorics formula because the results depend on the order of the
original array.  
The main idea is to deal recurrently by the length of the subsequence. On each
recurrent step, move from the end to the beginning and count the unique
combinations using the count of shorter unique combinations from the previous
step. More strictly on every step j we keep an array of length N and every
element in the place p means how many unique subsequences with length j we
found to the right of the element in place i, including i itself.  
Below is the implementation of the above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

// Function which returns the numbe of

// unique subsequences of length K

int solution(vector<int>& A, int k)

{

 // seiz of the vector

 // which does is constant

 const int N = A.size();

 // bases cases

 if (N < k || N < 1 || k < 1)

 return 0;

 if (N == k)

 return 1;

 // Prepare arrays for recursion

 vector<int> v1(N, 0);

 vector<int> v2(N, 0);

 vector<int> v3(N, 0);

 // initiate separately for k = 1

 // intiate the last element

 v2[N - 1] = 1;

 v3[A[N - 1] - 1] = 1;

 // initiate all other elements of k = 1

 for (int i = N - 2; i >= 0; i--) {

 // initialize the front element

 // to vector v2

 v2[i] = v2[i + 1];

 // if element v[a[i]-1] is 0

 // then increment it in vector v2

 if (v3[A[i] - 1] == 0) {

 v2[i]++;

 v3[A[i] - 1] = 1;

 }

 }

 // iterate for all possible values of K

 for (int j = 1; j < k; j++) {

 // fill the vectors with 0

 fill(v3.begin(), v3.end(), 0);

 // fill(v1.begin(), v1.end(), 0)

 // the last must be 0 as from last no unique

 // subarray can be formed

 v1[N - 1] = 0;

 // Iterate for all index from which unique

 // subsequences can be formed

 for (int i = N - 2; i >= 0; i--) {

 // add the number of subsequence formed

 // from the next index

 v1[i] = v1[i + 1];

 // start with combinations on the

 // next index

 v1[i] = v1[i] + v2[i + 1];

 // Remove the elements which have

 // already been counted

 v1[i] = v1[i] - v3[A[i] - 1];

 // Update the number used

 v3[A[i] - 1] = v2[i + 1];

 }

 // prepare the next iteration

 // by filling v2 in v1

 v2 = v1;

 }

 // last answer is stored in v2

 return v2[0];

}

// Function to push the vector into an array

// and print all the unique subarrays

void solve(int a[], int n, int k)

{

 vector<int> v;

 // fill the vector with a[]

 v.assign(a, a + n);

 // Function call to print the count

 // of unique susequences of size K

 cout << solution(v, k);

}

// Driver Code

int main()

{

 int a[] = { 1, 2, 3, 4 };

 int n = sizeof(a) / sizeof(a[0]);

 int k = 3;

 solve(a, n, k);

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

import java.util.*;

class GFG{

// Function which returns the numbe of

// unique subsequences of length K

static int solution(int[] A, int N, int k)

{

 // Bases cases

 if (N < k || N < 1 || k < 1)

 return 0;

 if (N == k)

 return 1;

 // Prepare arrays for recursion

 int[] v1 = new int[N];

 int[] v2 = new int[N];

 int[] v3 = new int[N];

 // Initiate separately for k = 1

 // intiate the last element

 v2[N - 1] = 1;

 v3[A[N - 1] - 1] = 1;

 // Initiate all other elements of k = 1

 for(int i = N - 2; i >= 0; i--)

 {

 // Initialize the front element

 // to vector v2

 v2[i] = v2[i + 1];

 // If element v[a[i]-1] is 0

 // then increment it in vector v2

 if (v3[A[i] - 1] == 0)

 {

 v2[i]++;

 v3[A[i] - 1] = 1;

 }

 }

 // Iterate for all possible values of K

 for(int j = 1; j < k; j++)

 {

 // Fill the vectors with 0

 Arrays.fill(v3, 0);

 // Fill(v1.begin(), v1.end(), 0)

 // the last must be 0 as from last

 // no unique subarray can be formed

 v1[N - 1] = 0;

 // Iterate for all index from which

 // unique subsequences can be formed

 for(int i = N - 2; i >= 0; i--)

 {

 // Add the number of subsequence

 // formed from the next index

 v1[i] = v1[i + 1];

 // Start with combinations on the

 // next index

 v1[i] = v1[i] + v2[i + 1];

 // Remove the elements which have

 // already been counted

 v1[i] = v1[i] - v3[A[i] - 1];

 // Update the number used

 v3[A[i] - 1] = v2[i + 1];

 }

 }

 // Last answer is stored in v2

 return v2[0];

}

// Driver Code

public static void main(String[] args)

{

 int a[] = { 1, 2, 3, 4 };

 int n = a.length;

 int k = 3;

 

 System.out.print(solution(a, n, k));

}

}

// This code is contributed by amal kumar choubey  
  
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

# Function which returns the numbe of

# unique subsequences of length K

def solution( A, k):

 # seiz of the vector

 # which does is constant

 N = len(A)

 # bases cases

 if (N < k or N < 1 or k < 1):

 return 0

 if (N == k):

 return 1

 # Prepare arrays for recursion

 v1 = [0]*(N)

 v2 = [0]*N

 v3 = [0]*N

 # initiate separately for k = 1

 # intiate the last element

 v2[N - 1] = 1

 v3[A[N - 1] - 1] = 1

 # initiate all other elements of k = 1

 for i in range(N - 2,-1,-1):

 # initialize the front element

 # to vector v2

 v2[i] = v2[i + 1]

 # if element v[a[i]-1] is 0

 # then increment it in vector v2

 if (v3[A[i] - 1] == 0):

 v2[i] += 1

 v3[A[i] - 1] = 1

 

 # iterate for all possible values of K

 for j in range( 1, k) :

 # fill the vectors with 0

 v3 = [0]*N

 # fill(v1.begin(), v1.end(), 0)

 # the last must be 0 as from last no unique

 # subarray can be formed

 v1[N - 1] = 0

 # Iterate for all index from which unique

 # subsequences can be formed

 for i in range( N - 2, -1, -1) :

 # add the number of subsequence formed

 # from the next index

 v1[i] = v1[i + 1]

 # start with combinations on the

 # next index

 v1[i] = v1[i] + v2[i + 1]

 # Remove the elements which have

 # already been counted

 v1[i] = v1[i] - v3[A[i] - 1]

 # Update the number used

 v3[A[i] - 1] = v2[i + 1]

 

 # prepare the next iteration

 # by filling v2 in v1

 for i in range(len(v1)):

 v2[i] = v1[i]

 

 # last answer is stored in v2

 return v2[0]

# Function to push the vector into an array

# and print all the unique subarrays

def solve(a, n, k):

 # fill the vector with a[]

 v = a

 # Function call to print the count

 # of unique susequences of size K

 print( solution(v, k))

# Driver Code

if __name__ == "__main__":

 a = [ 1, 2, 3, 4 ]

 n = len(a)

 k = 3

 solve(a, n, k)

# This code is contributed by chitranayal  
  
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

using System;

class GFG{

// Function which returns the numbe of

// unique subsequences of length K

static int solution(int[] A, int N, int k)

{

 // Bases cases

 if (N < k || N < 1 || k < 1)

 return 0;

 if (N == k)

 return 1;

 // Prepare arrays for recursion

 int[] v1 = new int[N];

 int[] v2 = new int[N];

 int[] v3 = new int[N];

 // Initiate separately for k = 1

 // intiate the last element

 v2[N - 1] = 1;

 v3[A[N - 1] - 1] = 1;

 // Initiate all other elements of k = 1

 for(int i = N - 2; i >= 0; i--)

 {

 // Initialize the front element

 // to vector v2

 v2[i] = v2[i + 1];

 // If element v[a[i]-1] is 0

 // then increment it in vector v2

 if (v3[A[i] - 1] == 0)

 {

 v2[i]++;

 v3[A[i] - 1] = 1;

 }

 }

 // Iterate for all possible values of K

 for(int j = 1; j < k; j++)

 {

 // Fill the vectors with 0

 for(int i = 0; i < v3.GetLength(0); i++)

 v3[i] = 0;

 // Fill(v1.begin(), v1.end(), 0)

 // the last must be 0 as from last

 // no unique subarray can be formed

 v1[N - 1] = 0;

 // Iterate for all index from which

 // unique subsequences can be formed

 for(int i = N - 2; i >= 0; i--)

 {

 // Add the number of subsequence

 // formed from the next index

 v1[i] = v1[i + 1];

 // Start with combinations on the

 // next index

 v1[i] = v1[i] + v2[i + 1];

 // Remove the elements which have

 // already been counted

 v1[i] = v1[i] - v3[A[i] - 1];

 // Update the number used

 v3[A[i] - 1] = v2[i + 1];

 }

 }

 // Last answer is stored in v2

 return v2[0];

}

// Driver Code

public static void Main(String[] args)

{

 int []a = { 1, 2, 3, 4 };

 int n = a.Length;

 int k = 3;

 

 Console.Write(solution(a, n, k));

}

}

// This code is contributed by Rohit_ranjan  
  
---  
  
 __

 __

 **Output:**

    
    
    4
    
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

