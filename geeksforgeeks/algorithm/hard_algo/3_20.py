XOR of pairwise sum of every unordered pairs in an array



Given an array **arr[]** of length **N** , the task is to find the XOR of
pairwise sum of every possible unordered pairs of the array. The unordered
pairs sum is defined as follows –  

    
    
    XOR of pairwise sum  = (A[0] + A[1]) ^
        (A[0] + A[2]) ^ ...(A[0] + A[N]) ^
        (A[1] + A[2]) ^ ...(A[1] + A[N]) ^
        .......
        (A[N-1] + A[N])
    
    Notice that after including A[0] and A[1] 
    as pairs, then A[1] and A[0] are not included.

 **Examples:**  

> **Input:** arr[] = {1, 2}  
> **Output:** 3  
> **Explanation:**  
> There is only one unordered pair. That is (1, 2)  
>  **Input:** arr[] = {1, 2, 3}  
> **Output:** 2  
> **Explanation:**  
> Unordered pairs of the numbers –  
> {(1, 2), (1, 3), (2, 3)}  
> XOR of unordered pairswise sum –  
> => (1 + 2) ^ (1 + 3) ^ (2 + 3)  
> => 3 ^ 4 ^ 5  
> => 2  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Naive Approach:** The idea is to find every possible unordered pair with
the help of the two loops and find the XOR of these pairs.  
Below is the implementation of the above approach:  

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find XOR of

// pairwise sum of every unordered

// pairs in an array

#include <bits/stdc++.h>

using namespace std;

// Function to find XOR of pairwise

// sum of every unordered pairs

int xorOfSum(int a[], int n)

{

 int answer = 0;

 

 // Loop to choose every possible

 // pairs in the array

 for (int i = 0; i < n; i++) {

 for (int j = i + 1; j < n; j++)

 answer ^= (a[i] + a[j]);

 }

 return answer;

}

// Driver Code

int main()

{

 int n = 3;

 int A[n] = { 1, 2, 3 };

 cout << xorOfSum(A, n);

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

// Java implementation to find XOR of

// pairwise sum of every unordered

// pairs in an array

class GFG{

 

// Function to find XOR of pairwise

// sum of every unordered pairs

static int xorOfSum(int a[], int n)

{

 int answer = 0;

 

 // Loop to choose every possible

 // pairs in the array

 for (int i = 0; i < n; i++) {

 for (int j = i + 1; j < n; j++)

 answer ^= (a[i] + a[j]);

 }

 

 return answer;

}

 

// Driver Code

public static void main(String[] args)

{

 int n = 3;

 int A[] = { 1, 2, 3 };

 

 System.out.print(xorOfSum(A, n));

}

}

// This code is contributed by PrinciRaj1992  
  
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

# Python3 implementation to find XOR of

# pairwise sum of every unordered

# pairs in an array

# Function to find XOR of pairwise

# sum of every unordered pairs

def xorOfSum(a, n):

 answer = 0

 # Loop to choose every possible

 # pairs in the array

 for i in range(n):

 for j in range(i + 1, n):

 answer ^= (a[i] + a[j])

 return answer

# Driver Code

if __name__ == '__main__':

 n = 3

 A=[1, 2, 3]

 print(xorOfSum(A, n))

# This code is contributed by mohit kumar 29  
  
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

// C# implementation to find XOR of

// pairwise sum of every unordered

// pairs in an array

using System;

using System.Collections.Generic;

class GFG{

 

// Function to find XOR of pairwise

// sum of every unordered pairs

static int xorOfSum(int []a, int n)

{

 int answer = 0;

 

 // Loop to choose every possible

 // pairs in the array

 for (int i = 0; i < n; i++) {

 for (int j = i + 1; j < n; j++)

 answer ^= (a[i] + a[j]);

 }

 

 return answer;

}

 

// Driver Code

public static void Main(String[] args)

{

 int n = 3;

 int []A = { 1, 2, 3 };

 

 Console.Write(xorOfSum(A, n));

}

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// JavaScript implementation to find XOR of

// pairwise sum of every unordered

// pairs in an array

// Function to find XOR of pairwise

// sum of every unordered pairs

function xorOfSum(a, n)

{

 let answer = 0;

 

 // Loop to choose every possible

 // pairs in the array

 for (let i = 0; i < n; i++) {

 for (let j = i + 1; j < n; j++)

 answer ^= (a[i] + a[j]);

 }

 return answer;

}

// Driver Code

 let n = 3;

 let A = [ 1, 2, 3 ];

 document.write(xorOfSum(A, n));

// This code is contributed by Surbhi Tyagi

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    2

**Efficient Approach:**  

  * For obtaining Kth bit of the final xor value we see in all the pair-sums, that kth bit of them is set or not. If there are even a number of pairs that have the Kth bit set, then for the Kth bit, their xor is zero else one.   

  * For finding count of pair sums having Kth bit set, we notice that we can mod all array elements by 2(K+1). This is because X and Y belong to input array and **Sum = X + Y**. Then X + Y can add up to have their Kth bit set which means Sum >= 2K. It can also be observed that they can have a carryover from addition which makes numbers in the range [2(K+1), 2(K+1) \+ 2K) have their Kth bit not set. So we only care about the Kth and (K+1)th bit of all the numbers to check the XOR of Kth bit.   

  * After the mod operation is performed, for sum to have kth bit set, its value will be in range – [2K, 2(K+1) ) U [2(K+1) \+ 2K, Max-Value-Sum-Can-Take ].   

  * To find the numbers in the said range, make another array B containing modded array elements of arr[], and sort them. Then Sum can be assumed as Sum = Bi \+ Bj. Finally, find the maximum bound of j using binary search (built-in lower_bound in C++). Fix i and since the array is sorted find the last j that satisfies the given condition and all the numbers in the range of indices can be added to the count to check the xor.   

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to find XOR of

// pairwise sum of every unordered

// pairs in an array

#include <bits/stdc++.h>

using namespace std;

// Function to find XOR of pairwise

// sum of every unordered pairs

int xorOfSum(int a[], int n)

{

 int i, j, k;

 

 // Sort the array

 sort(a, a + n);

 int ans = 0;

 // Array elements are not greater

 // than 1e7 so 27 bits are suffice

 for (k = 0; k < 27; ++k) {

 

 // Modded elements of array

 vector<int> b(n);

 

 // Loop to find the modded

 // elements of array

 for (i = 0; i < n; i++)

 b[i] = a[i] % (1 << (k + 1));

 // Sort the modded array

 sort(b.begin(), b.end());

 int cnt = 0;

 for (i = 0; i < n; i++) {

 // finding the bound for j

 // for given i using binary search

 int l = lower_bound(b.begin() +

 i + 1, b.end(),

 (1 << k) - b[i]) - b.begin();

 int r = lower_bound(b.begin() +

 i + 1, b.end(), (1 << (k + 1)) -

 b[i]) - b.begin();

 // All the numbers in the range

 // of indices can be added to the

 // count to check the xor.

 cnt += r - l;

 l = lower_bound(b.begin() + i + 1,

 b.end(), (1 << (k + 1)) +

 (1 << k) - b[i]) - b.begin();

 cnt += n - l;

 }

 // Remainder of cnt * kth power

 // of 2 added to the xor value

 ans += (cnt % 2) * 1LL * (1 << k);

 }

 return ans;

}

// Driver Code

int main()

{

 int n = 3;

 int A[n] = { 1, 2, 3 };

 cout << xorOfSum(A, n);

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    2

**Performance Analysis:**  

  * **Time complexity :** O(N * log(max(A))*log(N)

Outermost loop runs for log(max(A)) times and for each loop we create and sort
array b ,which consists of **N** elements ,hence complexity is
**O(N*log(N)*log(max(A)))**  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

