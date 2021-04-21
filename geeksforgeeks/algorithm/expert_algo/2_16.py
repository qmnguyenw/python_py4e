Minimize the cost of partitioning an array into K groups



Given an array **arr[]** and an integer **K** , the task is to partition the
array into **K** non-empty groups where each group is a subarray of the given
array and each element of the array is part of only one group. All the
elements in a given group must have the same value. You can perform the
following operation any number of times:  
Choose an element from the array and change it’s value to any value. Print the
minimum number of such operations required to partition the array.

 **Examples:**

>  **Input:** arr[] = {3, 1, 3, 3, 2, 1, 8, 5}, K = 3  
>  **Output:** 3  
> The array can be partitioned in {3, 3, 3, 3}, {2, 2} and {8, 8}  
> by changing the 2nd element to 3, the 6th  
> element to 2 and the last element to 8.
>
>  **Input:** arr[] = {3, 3, 9, 10}, K = 3  
>  **Output:** 0  
> Divide the array in groups {3, 3}, {9} and {10}  
> without performing any operations.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Observations:**

  

  

  * If **K = 1** then the group is the complete array itself. To minimize the number of operations needed the most intuitive thing to do is to change all the elements of the array and make them equal to the mode of the array (element with the highest frequency).
  * For **K** groups, the last element of the array will always belong to the **K th** group while the **1 st** element will belong to the **1 st** group.
  * If **K th** group has been found correctly then the problem will reduce to partitioning the remaining array into **K – 1** groups using minimum operations.

 **Approach:** This problem can be solved using dynamic programming.

  1. Let **DP(i, j)** represent the minimum operations needed to partition the **array[1..i]** into **j** groups.
  2. Now, the task is to find **DP(N, K)** which is the minimum operations needed to partition the **array[1..N]** into **K** groups.
  3. The base cases **DP(i, j)** where **j = 1** can be easily answered. Since the complete array **array[1..i]** needs to be partitioned into a single group only. From the observations, find the mode of the **array[1..i]** and change all the elements in **array[1..i]** to the mode. If the mode occurred **x** times then **i – x** elements will have to be changed i.e. **i – x** operations.
  4. Since, the **K th** group ends at the last element. However it may start at various possible positions. Suppose that the **K th** group starts at some index **it** then **array[it..N]** needs to be partitioned into a single group and **array[1..(it – 1)]** needs to be partitioned into **K – 1** groups. The cost of partitioning **array[1..(it – 1)]** into **K – 1** groups is **DP(it – 1, K – 1)** and the cost of partitioning **array[it..N]** in a single group can be calculated using the mode and it’s frequency observation.
  5. To find the frequency of the most occurring element in a range **[it..i]** we can use a hashmap and an integer variable. The integer variable represents the current highest frequency. The map stores all elements seen till now along with their frequencies. Whenever an element is seen it’s frequency is incremented in the map, if now the frequency of this element is higher than the current highest frequency we update the current highest frequency to the frequency of the just seen element. Refer this for the approach.
  6. Therefore **DP(i, j)** is the minimum of **DP(it – 1, j – 1) + cost of partitioning array[it..i] into 1 group** for all possible values of **it**.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the minimum number

// of operations needed to partition

// the array in k contiguous groups

// such that all elements of a

// given group are identical

int getMinimumOps(vector<int> ar, int k)

{

 // n is the size of the array

 int n = ar.size();

 

 // dp(i, j) represents the minimum cost for

 // partitioning the array[0..i] into j groups

 int dp[n][k + 1];

 

 // Base case, cost is 0 for parititoning the

 // array[0..0] into 1 group

 dp[0][1] = 0;

 

 // Fill dp(i, j) and the answer will

 // be stored at dp(n-1, k)

 for (int i = 1; i < n; i++) {

 

 // The maximum groups that the segment 0..i can

 // be divided in is represented by maxGroups

 int maxGroups = min(k, i + 1);

 

 for (int j = 1; j <= maxGroups; j++) {

 

 // Initialize dp(i, j) to infinity

 dp[i][j] = INT_MAX;

 

 // Divide segment 0..i in 1 group

 if (j == 1) {

 

 // map and freqOfMode are together used to

 // keep track of the frequency of the most

 // occurring element in [0..i]

 unordered_map<int, int> freq;

 int freqOfMode = 0;

 for (int it = 0; it <= i; it++) {

 freq[ar[it]]++;

 int newElementFreq = freq[ar[it]];

 if (newElementFreq > freqOfMode)

 freqOfMode = newElementFreq;

 }

 

 // Change all the elements in the range

 // 0..i to the most frequent element

 // in this range

 dp[i][1] = (i + 1) - freqOfMode;

 }

 else {

 unordered_map<int, int> freq;

 int freqOfMode = 0;

 

 // If the jth group is the segment from

 // it..i, we change all the elements in this

 // range to this range's most occurring element

 for (int it = i; it >= j - 1; it--) {

 freq[ar[it]]++;

 int newElementFreq = freq[ar[it]];

 if (newElementFreq > freqOfMode)

 freqOfMode = newElementFreq;

 

 // Number of elements we need to change

 // in the jth group i.e. the range it..i

 int elementsToChange = i - it + 1;

 elementsToChange -= freqOfMode;

 

 // For all the possible sizes of the jth

 // group that end at the ith element

 // we pick the size that gives us the minimum

 // cost for dp(i, j)

 // elementsToChange is the cost of making

 // all the elements in the jth group identical

 // and we make use of dp(it - 1, j - 1) to

 // find the overall minimal cost

 dp[i][j] = min(dp[it - 1][j - 1]

 + elementsToChange,

 dp[i][j]);

 }

 }

 }

 }

 

 // Return the minimum cost for

 // partitioning array[0..n-1]

 // into k groups which is

 // stored at dp(n-1, k)

 return dp[n - 1][k];

}

 

// Driver code

int main()

{

 int k = 3;

 vector<int> ar = { 3, 1, 3, 3, 2, 1, 8, 5 };

 

 cout << getMinimumOps(ar, k);

 

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

// Java implementation of above approach

class GFG

{

 

// Function to return the minimum number

// of operations needed to partition

// the array in k contiguous groups

// such that all elements of a

// given group are identical

static int getMinimumOps(int ar[], int k)

{

 // n is the size of the array

 int n = ar.length;

 

 // dp(i, j) represents the minimum cost for

 // partitioning the array[0..i] into j groups

 int dp[][] = new int[n][k + 1];

 

 // Base case, cost is 0 for parititoning the

 // array[0..0] into 1 group

 dp[0][1] = 0;

 

 // Fill dp(i, j) and the answer will

 // be stored at dp(n-1, k)

 for (int i = 1; i < n; i++)

 {

 

 // The maximum groups that the segment 0..i can

 // be divided in is represented by maxGroups

 int maxGroups = Math.min(k, i + 1);

 

 for (int j = 1; j <= maxGroups; j++) 

 {

 

 // Initialize dp(i, j) to infinity

 dp[i][j] = Integer.MAX_VALUE;

 

 // Divide segment 0..i in 1 group

 if (j == 1) 

 {

 

 // map and freqOfMode are together used to

 // keep track of the frequency of the most

 // occurring element in [0..i]

 int freq[] = new int[100000];

 int freqOfMode = 0;

 for (int it = 0; it <= i; it++) 

 {

 freq[ar[it]]++;

 int newElementFreq = freq[ar[it]];

 if (newElementFreq > freqOfMode)

 freqOfMode = newElementFreq;

 }

 

 // Change all the elements in the range

 // 0..i to the most frequent element

 // in this range

 dp[i][1] = (i + 1) - freqOfMode;

 }

 else

 {

 int freq[] = new int[100000];

 int freqOfMode = 0;

 

 // If the jth group is the segment from

 // it..i, we change all the elements in this

 // range to this range's most occurring element

 for (int it = i; it >= j - 1; it--) 

 {

 freq[ar[it]]++;

 int newElementFreq = freq[ar[it]];

 if (newElementFreq > freqOfMode)

 freqOfMode = newElementFreq;

 

 // Number of elements we need to change

 // in the jth group i.e. the range it..i

 int elementsToChange = i - it + 1;

 elementsToChange -= freqOfMode;

 

 // For all the possible sizes of the jth

 // group that end at the ith element

 // we pick the size that gives us the minimum

 // cost for dp(i, j)

 // elementsToChange is the cost of making

 // all the elements in the jth group identical

 // and we make use of dp(it - 1, j - 1) to

 // find the overall minimal cost

 dp[i][j] = Math.min(dp[it - 1][j - 1] +

 elementsToChange, dp[i][j]);

 }

 }

 }

 }

 

 // Return the minimum cost for

 // partitioning array[0..n-1]

 // into k groups which is

 // stored at dp(n-1, k)

 return dp[n - 1][k];

}

 

// Driver code

public static void main(String args[])

{

 int k = 3;

 int ar[] = { 3, 1, 3, 3, 2, 1, 8, 5 };

 

 System.out.println(getMinimumOps(ar, k));

}

}

 

// This code is contributed by Arnab Kundu  
  
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

# Python3 implementation of the approach

 

# Function to return the minimum number

# of operations needed to partition

# the array in k contiguous groups

# such that all elements of a

# given group are identical

def getMinimumOps(ar, k):

 

 # n is the size of the array

 n = len(ar)

 

 # dp(i, j) represents the minimum cost for

 # partitioning the array[0..i] into j groups

 dp = [[ 0 for i in range(k + 1)] 

 for i in range(n)]

 

 # Base case, cost is 0 for parititoning the

 # array[0..0] into 1 group

 dp[0][1] = 0

 

 # Fill dp(i, j) and the answer will

 # be stored at dp(n-1, k)

 for i in range(1, n):

 

 # The maximum groups that the segment 0..i can

 # be divided in is represented by maxGroups

 maxGroups = min(k, i + 1)

 

 for j in range(1, maxGroups + 1):

 

 # Initialize dp(i, j) to infinity

 dp[i][j] = 10**9

 

 # Divide segment 0..i in 1 group

 if (j == 1):

 

 # map and freqOfMode are together used to

 # keep track of the frequency of the most

 # occurring element in [0..i]

 freq1 = dict()

 freqOfMode = 0

 for it in range(0, i + 1):

 

 freq1[ar[it]] = freq1.get(ar[it], 0) + 1

 newElementFreq = freq1[ar[it]]

 if (newElementFreq > freqOfMode):

 freqOfMode = newElementFreq

 

 # Change all the elements in the range

 # 0..i to the most frequent element

 # in this range

 dp[i][1] = (i + 1) - freqOfMode

 

 else:

 freq = dict()

 freqOfMode = 0

 

 # If the jth group is the segment from

 # it..i, we change all the elements in this

 # range to this range's most occurring element

 for it in range(i, j - 2, -1):

 

 #print(i,j,it)

 freq[ar[it]] = freq.get(ar[it], 0) + 1

 newElementFreq = freq[ar[it]]

 if (newElementFreq > freqOfMode):

 freqOfMode = newElementFreq

 

 # Number of elements we need to change

 # in the jth group i.e. the range it..i

 elementsToChange = i - it + 1

 elementsToChange -= freqOfMode

 

 # For all the possible sizes of the jth

 # group that end at the ith element

 # we pick the size that gives us the minimum

 # cost for dp(i, j)

 # elementsToChange is the cost of making

 # all the elements in the jth group identical

 # and we make use of dp(it - 1, j - 1) to

 # find the overall minimal cost

 dp[i][j] = min(dp[it - 1][j - 1] +

 elementsToChange, dp[i][j])

 

 # Return the minimum cost for

 # partitioning array[0..n-1]

 # into k groups which is

 # stored at dp(n-1, k)

 return dp[n - 1][k]

 

# Driver code

k = 3

ar =[3, 1, 3, 3, 2, 1, 8, 5]

 

print(getMinimumOps(ar, k))

 

# This code is contributed by Mohit Kumar  
  
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

// C# implementation of above approach

using System;

 

class GFG 

{ 

 

// Function to return the minimum number 

// of operations needed to partition 

// the array in k contiguous groups 

// such that all elements of a 

// given group are identical 

static int getMinimumOps(int []ar, int k) 

{ 

 // n is the size of the array 

 int n = ar.Length; 

 

 // dp(i, j) represents the minimum cost for 

 // partitioning the array[0..i] into j groups 

 int [,]dp = new int[n, k + 1]; 

 

 // Base case, cost is 0 for parititoning the 

 // array[0..0] into 1 group 

 dp[0, 1] = 0; 

 

 // Fill dp(i, j) and the answer will 

 // be stored at dp(n-1, k) 

 for (int i = 1; i < n; i++) 

 { 

 

 // The maximum groups that the segment 0..i can 

 // be divided in is represented by maxGroups 

 int maxGroups = Math.Min(k, i + 1); 

 

 for (int j = 1; j <= maxGroups; j++) 

 { 

 

 // Initialize dp(i, j) to infinity 

 dp[i, j] = int.MaxValue; 

 

 // Divide segment 0..i in 1 group 

 if (j == 1) 

 { 

 

 // map and freqOfMode are together used to 

 // keep track of the frequency of the most 

 // occurring element in [0..i] 

 int []freq = new int[100000]; 

 int freqOfMode = 0; 

 for (int it = 0; it <= i; it++) 

 { 

 freq[ar[it]]++; 

 int newElementFreq = freq[ar[it]]; 

 if (newElementFreq > freqOfMode) 

 freqOfMode = newElementFreq; 

 } 

 

 // Change all the elements in the range 

 // 0..i to the most frequent element 

 // in this range 

 dp[i, 1] = (i + 1) - freqOfMode; 

 } 

 else

 { 

 int []freq = new int[100000]; 

 int freqOfMode = 0; 

 

 // If the jth group is the segment from 

 // it..i, we change all the elements in this 

 // range to this range's most occurring element 

 for (int it = i; it >= j - 1; it--) 

 { 

 freq[ar[it]]++; 

 int newElementFreq = freq[ar[it]]; 

 if (newElementFreq > freqOfMode) 

 freqOfMode = newElementFreq; 

 

 // Number of elements we need to change 

 // in the jth group i.e. the range it..i 

 int elementsToChange = i - it + 1; 

 elementsToChange -= freqOfMode; 

 

 // For all the possible sizes of the jth 

 // group that end at the ith element 

 // we pick the size that gives us the minimum 

 // cost for dp(i, j) 

 // elementsToChange is the cost of making 

 // all the elements in the jth group identical 

 // and we make use of dp(it - 1, j - 1) to 

 // find the overall minimal cost 

 dp[i, j] = Math.Min(dp[it - 1, j - 1] + 

 elementsToChange, dp[i, j]); 

 } 

 } 

 } 

 } 

 

 // Return the minimum cost for 

 // partitioning array[0..n-1] 

 // into k groups which is 

 // stored at dp(n-1, k) 

 return dp[n - 1, k]; 

} 

 

// Driver code 

public static void Main(String []args) 

{ 

 int k = 3; 

 int []ar = {3, 1, 3, 3, 2, 1, 8, 5}; 

 

 Console.WriteLine(getMinimumOps(ar, k)); 

} 

} 

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    3
    

**Time Complexity:** O(N * N * K) where N is the size of the array and K is
the number of groups the array should be partitioned into.  
 **Space Complexity:** O(N * K)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

