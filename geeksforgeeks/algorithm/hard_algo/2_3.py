Sum of absolute difference of all pairs raised to power K



Given an array **arr[]** of **N** integers and a number **K** , the task is to
find the sum of absolute difference of all pairs raised to the power **K** in
a given array i.e., ![ \\sum_{i=1}^{N} \\sum_{j=1}^{N} \\
|arr\[i\]-arr\[j\]|^K](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-3aa326e33c90342dec977a8f82b8202f_l3.png).

 **Examples:**

>  **Input:** arr[] = {1, 2, 3}, K = 1  
>  **Output:** 8  
>  **Explanation:**  
>  Sum of |1-1|+|1-2|+|1-3|+|2-1|+|2-2|+|2-3|+|3-1|+|3-2|+|3-3| = 8
>
>  **Input:** arr[] = {1, 2, 3}, K = 3  
>  **Output:** 20  
>  **Explanation:**  
>  Sum of |1 – 1| 3 \+ |1 – 2| 3 \+ |1 – 3| 3 \+ |2 – 1| 3 \+ |2 – 2| 3 \+ |2
> – 3| 3 \+ |3 – 1| 3 \+ |3 – 2| 3 \+ |3 – 3| 3 = 20
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Naive Approach:** The idea is to generate all the possible pairs and find
the absolute difference of each pair raised to the power **K** and sum up them
together.

 **Time Complexity:** _O((log K)*N 2)_  
 **Auxiliary Space:** _O(1)_

 **Efficient Approach:** We can improve the time complexity of the naive
approach with the below calculations:  
For all possible pair, we have to find the value of

> ![ Sum = \\sum_{i=1}^{N} \\sum_{j=1}^{N} |arr\[i\] - arr\[j\]|^{K}
> ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-e2a3b8dd971582a570388a0770f37480_l3.png)

Since for pairs (arr[i], arr[j]) the value of
![|arr\[i\]-arr\[j\]|^{K}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d1ce59a39389dff5979a9c2d96e45f44_l3.png) is being
calcuated twice. So the above equation can also be written as:

> ![ Sum = 2 * \\sum_{i=1}^{N} \\sum_{j=1}^{i-1} |arr\[i\] - arr\[j\]|^{K}
> ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-70cba71a0f2ab8e23b0192907f3a3eb2_l3.png)

Writing ![|arr\[i\]-arr\[j\]|^{K}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-d1ce59a39389dff5979a9c2d96e45f44_l3.png) in
terms of Binomial Equation:

> ![ Sum = 2 * \\sum_{i=1}^{N} \\sum_{j=1}^{i-1} \\sum_{a=0}^{K}
> \\binom{K}{a}arr\[i\]^{K}*\(-arr\[j\]\)^{K - a}
> ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-19a04e7a0d41878192bc23c4b92fcb61_l3.png) (Equation 1)
>
>  
>
>
>  
>

Let Pre[i][a] = ![ \\sum_{j=1}^{i-1}\(-arr\[j\]\)^{K - a}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-4ae867592333b97f9fc26432bf591504_l3.png) (Equation 2)

From Equation 1 and Equation 2, we have

> ![ Sum = 2 * \\sum_{i=1}^{N} \\sum_{a=0}^{K}
> \\binom{K}{a}Pre\[i\]\[a\]*arr\[i\]^{K}](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-a9865410bd44f9c3d3d3d42b81272ae5_l3.png)

The value of **Pre[i][a]** can be calculated as:

> Pre[i][a] = {(-arr[1])K – a \+ (-arr[2])K – a … . . +(-arr[i – 1])K – a}.  
> So, Pre[i+1][a] = Pre[i][a]+(-arr[i])K – a

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above approach

 

#include <bits/stdc++.h>

#define ll long long

using namespace std;

 

class Solution {

 

public:

 // Since K can be 100 max

 ll ncr[101][101];

 int n, k;

 vector<ll> A;

 

 // Constructor

 Solution(int N, int K, vector<ll> B)

 {

 // Initializing with -1

 memset(ncr, -1, sizeof(ncr));

 

 n = N;

 k = K;

 A = B;

 

 // Making vector A as 1-Indexing

 A.insert(A.begin(), 0);

 }

 

 ll f(int N, int K);

 

 ll pairsPower();

};

 

// To Calulate the value nCk

ll Solution::f(int n, int k)

{

 if (k == 0)

 return 1LL;

 

 if (n == k)

 return 1LL;

 

 if (n < k)

 return 0;

 

 if (ncr[n][k] != -1)

 return ncr[n][k];

 

 // Since nCj = (n-1)Cj + (n-1)C(j-1);

 return ncr[n][k] = f(n - 1, k)

 + f(n - 1, k - 1);

}

 

// Function that summation of absolute

// differences of all pairs raised

// to the power k

ll Solution::pairsPower()

{

 ll pre[n + 1][k + 1];

 ll ans = 0;

 

 // Sort the given array

 sort(A.begin() + 1, A.end());

 

 // Precomputation part, O(n*k)

 for (int i = 1; i <= n; ++i) {

 pre[i][0] = 1LL;

 

 for (int j = 1; j <= k; j++) {

 pre[i][j] = A[i]

 * pre[i][j - 1];

 }

 

 if (i != 1) {

 for (int j = 0; j <= k; ++j)

 pre[i][j] = pre[i][j]

 + pre[i - 1][j];

 }

 }

 

 // Traverse the array arr[]

 for (int i = n; i >= 2; --i) {

 

 // For each K

 for (int j = 0; j <= k; j++) {

 

 ll val = f(k, j);

 

 ll val1 = pow(A[i], k - j)

 * pre[i - 1][j];

 

 val = val * val1;

 

 if (j % 2 == 0)

 ans = (ans + val);

 

 else

 ans = (ans - val);

 }

 }

 

 ans = 2LL * ans;

 

 // Return the final answer

 return ans;

}

 

// Driver Code

int main()

{

 // Given N and K

 int N = 3;

 int K = 3;

 

 // Given array

 vector<ll> arr = { 1, 2, 3 };

 

 // Creation of Object of class

 Solution obj(N, K, arr);

 

 // Function Call

 cout << obj.pairsPower() << endl;

 return 0;

}  
  
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

# Python3 program for the above approach

class Solution:

 

 def __init__(self, N, K, B):

 

 self.ncr = []

 

 # Since K can be 100 max

 for i in range(101):

 temp = []

 for j in range(101):

 

 # Initializing with -1

 temp.append(-1)

 

 self.ncr.append(temp)

 

 self.n = N

 self.k = K

 

 # Making vector A as 1-Indexing

 self.A = [0] + B

 

 # To Calulate the value nCk

 def f(self, n, k):

 

 if k == 0:

 return 1

 if n == k:

 return 1

 if n < k:

 return 0

 

 if self.ncr[n][k] != -1:

 return self.ncr[n][k]

 

 # Since nCj = (n-1)Cj + (n-1)C(j-1);

 self.ncr[n][k] = (self.f(n - 1, k) +

 self.f(n - 1, k - 1))

 

 return self.ncr[n][k]

 

 # Function that summation of absolute

 # differences of all pairs raised

 # to the power k

 def pairsPower(self):

 

 pre = []

 

 for i in range(self.n + 1):

 temp = []

 for j in range(self.k + 1):

 temp.append(0)

 

 pre.append(temp)

 

 ans = 0

 

 # Sort the given array

 self.A.sort()

 

 # Precomputation part, O(n*k)

 for i in range(1, self.n + 1):

 pre[i][0] = 1

 

 for j in range(1, self.k + 1):

 pre[i][j] = (self.A[i] *

 pre[i][j - 1])

 

 if i != 1:

 for j in range(self.k + 1):

 pre[i][j] = (pre[i][j] +

 pre[i - 1][j])

 

 # Traverse the array arr[]

 for i in range(self.n, 1, -1):

 

 # For each K

 for j in range(self.k + 1):

 val = self.f(self.k, j)

 val1 = (pow(self.A[i], 

 self.k - j) *

 pre[i - 1][j])

 

 val = val * val1

 

 if j % 2 == 0:

 ans = ans + val

 else:

 ans = ans - val

 

 ans = 2 * ans

 

 # Return the final answer

 return ans

 

# Driver code

if __name__ == '__main__':

 

 # Given N and K

 N = 3

 K = 3

 

 # Given array

 arr = [ 1, 2, 3 ]

 

 # Creation of object of class

 obj = Solution(N, K, arr)

 

 # Function call

 print(obj.pairsPower())

 

# This code is contributed by Shivam Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    20
    

**Time Complexity:** _O(N*K)_  
 **Auxiliary Space:** _O(N*K)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

