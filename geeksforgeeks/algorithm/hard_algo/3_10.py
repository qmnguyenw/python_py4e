Maximum sum such that exactly half of the elements are selected and no two
adjacent



Given an array A containing N integers. Find the maximum sum possible such
that exactly floor(N/2) elements are selected and no two selected elements are
adjacent to each other. (if N = 5, then exactly 2 elements should be selected
as floor(5/2) = 2)  
For a simpler version of this problem check out this.  
 **Examples:**

>  **Input:** A = [1, 2, 3, 4, 5, 6]  
> **Output:** 12  
> **Explanation:**  
>  Select 2, 4 and 6 making the sum 12.  
>  **Input :** A = [-1000, -100, -10, 0, 10]  
> **Output :** 0  
> **Explanation:**  
>  Select -10 and 10 making the sum 0.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**

  * We will use the concept of dynamic programming. Following is how the dp states are defined :

>  **dp[i][j]** = maximum sum till index i such that j elements are selected

  * Since no two adjacent elements can be selected :

>  **dp[i][j]** = max(a[i] + dp[i-2][j-1], dp[i-1][j])
>
>  
>
>
>  
>

Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find maximum sum possible

// such that exactly floor(N/2) elements

// are selected and no two selected

// elements are adjacent to each other

#include <bits/stdc++.h>

using namespace std;

// Function return the maximum sum

// possible under given condition

int MaximumSum(int a[], int n)

{

 int dp[n + 1][n + 1];

 // Intitialising the dp table

 for (int i = 0; i < n + 1; i++)

 {

 for (int j = 0; j < n + 1; j++)

 dp[i][j] = INT_MIN;

 }

 // Base case

 for (int i = 0; i < n + 1; i++)

 dp[i][0] = 0;

 for (int i = 1; i <= n; i++)

 {

 for (int j = 1; j <= i; j++)

 {

 int val = INT_MIN;

 // Condition to select the current

 // element

 if ((i - 2 >= 0

 && dp[i - 2][j - 1] != INT_MIN)

 || i - 2 < 0)

 {

 val = a[i - 1] +

 (i - 2 >= 0 ?

 dp[i - 2][j - 1] : 0);

 }

 

 // Condition to not select the

 // current element if possible

 if (i - 1 >= j)

 {

 val = max(val, dp[i - 1][j]);

 }

 dp[i][j] = val;

 }

 }

 return dp[n][n / 2];

}

//Driver code

int main()

{

 

 int A[] = {1, 2, 3, 4, 5, 6};

 

 int N = sizeof(A) / sizeof(A[0]);

 cout << MaximumSum(A, N);

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

// Java program to find maximum sum possible

// such that exactly Math.floor(N/2) elements

// are selected and no two selected

// elements are adjacent to each other

class GFG{

// Function return the maximum sum

// possible under given condition

static int MaximumSum(int a[], int n)

{

 int [][]dp = new int[n + 1][n + 1];

 // Intitialising the dp table

 for(int i = 0; i < n + 1; i++)

 {

 for(int j = 0; j < n + 1; j++)

 dp[i][j] = Integer.MIN_VALUE;

 }

 // Base case

 for(int i = 0; i < n + 1; i++)

 dp[i][0] = 0;

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= i; j++)

 {

 int val = Integer.MIN_VALUE;

 

 // Condition to select the current

 // element

 if ((i - 2 >= 0 &&

 dp[i - 2][j - 1] != Integer.MIN_VALUE) ||

 i - 2 < 0)

 {

 val = a[i - 1] + (i - 2 >= 0 ?

 dp[i - 2][j - 1] : 0);

 }

 

 // Condition to not select the

 // current element if possible

 if (i - 1 >= j)

 {

 val = Math.max(val, dp[i - 1][j]);

 }

 dp[i][j] = val;

 }

 }

 return dp[n][n / 2];

}

// Driver code

public static void main(String[] args)

{

 int A[] = { 1, 2, 3, 4, 5, 6 };

 int N = A.length;

 System.out.print(MaximumSum(A, N));

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

# Python3 program to find maximum sum possible

# such that exactly floor(N/2) elements

# are selected and no two selected

# elements are adjacent to each other

import sys

# Function return the maximum sum

# possible under given condition

def MaximumSum(a,n):

 dp = [[0 for i in range(n+1)] for j in
range(n+1)]

 # Intitialising the dp table

 for i in range(n + 1):

 for j in range(n + 1):

 dp[i][j] = -sys.maxsize-1

 # Base case

 for i in range(n+1):

 dp[i][0] = 0

 for i in range(1,n+1,1):

 for j in range(1,i+1,1):

 val = -sys.maxsize-1

 # Condition to select the current

 # element

 if ((i - 2 >= 0 and dp[i - 2][j - 1] !=
-sys.maxsize-1) or i - 2 < 0):

 if (i - 2 >= 0):

 val = a[i - 1] + dp[i - 2][j - 1]

 else:

 val = a[i - 1]

 

 # Condition to not select the

 # current element if possible

 if (i - 1 >= j):

 val = max(val, dp[i - 1][j])

 

 dp[i][j] = val

 return dp[n][n // 2]

#Driver code

if __name__ == '__main__':

 A = [1, 2, 3, 4, 5, 6]

 

 N = len(A)

 print(MaximumSum(A,N))

# This code is contributed by Bhupendra_Singh  
  
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

// C# program to find maximum sum possible

// such that exactly Math.floor(N/2) elements

// are selected and no two selected

// elements are adjacent to each other

using System;

class GFG{

// Function return the maximum sum

// possible under given condition

static int MaximumSum(int []a, int n)

{

 int [,]dp = new int[n + 1, n + 1];

 // Intitialising the dp table

 for(int i = 0; i < n + 1; i++)

 {

 for(int j = 0; j < n + 1; j++)

 dp[i, j] = Int32.MinValue;

 }

 // Base case

 for(int i = 0; i < n + 1; i++)

 dp[i, 0] = 0;

 for(int i = 1; i <= n; i++)

 {

 for(int j = 1; j <= i; j++)

 {

 int val = Int32.MinValue;

 

 // Condition to select the current

 // element

 if ((i - 2 >= 0 &&

 dp[i - 2, j - 1] != Int32.MinValue) ||

 i - 2 < 0)

 {

 val = a[i - 1] + (i - 2 >= 0 ?

 dp[i - 2, j - 1] : 0);

 }

 

 // Condition to not select the

 // current element if possible

 if (i - 1 >= j)

 {

 val = Math.Max(val, dp[i - 1, j]);

 }

 dp[i, j] = val;

 }

 }

 return dp[n, n / 2];

}

// Driver code

public static void Main()

{

 int []A = { 1, 2, 3, 4, 5, 6 };

 int N = A.Length;

 Console.Write(MaximumSum(A, N));

}

}

// This code is contributed by Nidhi_biet  
  
---  
  
 __

 __

 **Output:**

    
    
    12
    
    
    
    

**Time Complexity :** O(N2)  
 **Efficient Approach**

  * We will use dynamic programming but with slightly modified states. Storing both the index and number of elements taken till now are futile since we always need to take exactly floor(i/2) elements, so at i’th position for the dp storage we will assume floor(i/2) elements in the subset till now. 
  * Following are the dp table states :

>  **dp[i][1]** = maximum sum till i’th index, picking element a[i], with
> floor(i/2) elements, none adjacent to each other.  
> **dp[i][0]** = maximum sum till i’th index, not picking element a[i], with
> floor(i/2) elements, none adjacent to each other.

  * We have two cases : 
    * **When i is odd** : If we to pick a[i], then we can’t pick a[i-1], so only option left are (i – 2)th and (i – 3) rd state (because floor((i – 2)/2) = floor((i – 3)/2) = floor(i/2) – 1, and since we pick a[i], total picked elements will be floor(i/2) ). If we don’t pick a[i], then sum will be formed by taking a[i-1] and using states i – 1, i – 2 and i – 3 or a[i – 2] using state i – 3 as these only will give the total of floor(i/2).

>  **dp[i][1]** = arr[i] + max({dp[i – 3][1], dp[i – 3][0], dp[i – 2][1], dp[i
> – 2][0]})  
> **dp[i][0]** = max({arr[i – 1] + dp[i – 2][0], arr[i – 1] + dp[i – 3][1],
> arr[i – 1] + dp[i – 3][0],  
> arr[i – 2] + dp[i – 3][0]})  
>

  * **When i is even** : If we pick a[i], then using states i – 1 and i – 2, else picking a[i – 1] and using state i – 2.   

> **dp[i][1]** = arr[i] + max({dp[i – 2][1], dp[i – 2][0], dp[i – 1][0]})  
> **dp[i][0]** = arr[i – 1] + dp[i – 2][0]

Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find maximum sum possible

// such that exactly floor(N/2) elements

// are selected and no two selected

// elements are adjacent to each other

#include <bits/stdc++.h>

using namespace std;

// Function return the maximum sum

// possible under given condition

int MaximumSum(int a[], int n)

{

 int dp[n + 1][2];

 

 // Intitialising the dp table

 memset(dp, 0, sizeof(dp));

 // Base case

 dp[2][1] = a[1];

 dp[2][0] = a[0];

 for (int i = 3; i < n + 1; i++) {

 // When i is odd

 if (i & 1) {

 int temp = max({ dp[i - 3][1],

 dp[i - 3][0],

 dp[i - 2][1],

 dp[i - 2][0] });

 

 dp[i][1] = a[i - 1] + temp;

 dp[i][0] = max({ a[i - 2] + dp[i - 2][0],

 a[i - 2] + dp[i - 3][1],

 a[i - 2] + dp[i - 3][0],

 a[i - 3] + dp[i - 3][0] });

 }

 // When i is even

 else {

 dp[i][1] = a[i - 1] + max({ dp[i - 2][1],

 dp[i - 2][0],

 dp[i - 1][0] });

 

 dp[i][0] = a[i - 2] + dp[i - 2][0];

 }

 }

 // Maximum of if we pick last element or not

 return max(dp[n][1], dp[n][0]);

}

// Driver code

int main()

{

 int A[] = {1, 2, 3, 4, 5, 6};

 

 int N = sizeof(A) / sizeof(A[0]);

 cout << MaximumSum(A, N);

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

// Java program to find maximum sum possible

// such that exactly Math.floor(N/2) elements

// are selected and no two selected

// elements are adjacent to each other

import java.util.*;

class GFG{

// Function return the maximum sum

// possible under given condition

static int MaximumSum(int a[], int n)

{

 int [][]dp = new int[n + 1][2];

 // Base case

 dp[2][1] = a[1];

 dp[2][0] = a[0];

 for(int i = 3; i < n + 1; i++)

 {

 

 // When i is odd

 if (i % 2 == 1)

 {

 int temp = Math.max((Math.max(dp[i - 3][1],

 dp[i - 3][0])),

 Math.max(dp[i - 2][1],

 dp[i - 2][0]));

 dp[i][1] = a[i - 1] + temp;

 dp[i][0] = Math.max((Math.max(a[i - 2] +

 dp[i - 2][0],

 a[i - 2] +

 dp[i - 3][1])),

 Math.max(a[i - 2] +

 dp[i - 3][0],

 a[i - 3] +

 dp[i - 3][0]));

 }

 

 // When i is even

 else

 {

 dp[i][1] = a[i - 1] + (Math.max((

 Math.max(dp[i - 2][1],

 dp[i - 2][0])),

 dp[i - 1][0]));

 dp[i][0] = a[i - 2] + dp[i - 2][0];

 }

 }

 

 // Maximum of if we pick last element or not

 return Math.max(dp[n][1], dp[n][0]);

}

static int max(int []arr)

{

 return 1;

}

// Driver code

public static void main(String[] args)

{

 int A[] = {1, 2, 3, 4, 5, 6};

 int N = A.length;

 System.out.print(MaximumSum(A, N));

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

# Python3 program to find maximum sum possible

# such that exactly floor(N/2) elements

# are selected and no two selected

# elements are adjacent to each other

# Function return the maximum sum

# possible under given condition

def MaximumSum(a, n):

 dp = [[0 for x in range (2)]

 for y in range(n + 1)]

 

 # Base case

 dp[2][1] = a[1]

 dp[2][0] = a[0]

 for i in range (3, n + 1):

 

 # When i is odd

 if (i & 1):

 temp = max([dp[i - 3][1],

 dp[i - 3][0],

 dp[i - 2][1],

 dp[i - 2][0]])

 

 dp[i][1] = a[i - 1] + temp

 dp[i][0] = max([a[i - 2] + dp[i - 2][0],

 a[i - 2] + dp[i - 3][1],

 a[i - 2] + dp[i - 3][0],

 a[i - 3] + dp[i - 3][0]])

 # When i is even

 else:

 dp[i][1] = (a[i - 1] + max([dp[i - 2][1],

 dp[i - 2][0],

 dp[i - 1][0]]))

 

 dp[i][0] = a[i - 2] + dp[i - 2][0]

 

 # Maximum of if we pick last

 # element or not

 return max(dp[n][1], dp[n][0])

# Driver code

if __name__ == "__main__": 

 

 A = [1, 2, 3, 4, 5, 6] 

 N = len(A)

 print(MaximumSum(A, N))

# This code is contributed by Chitranayal  
  
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

// C# program to find maximum sum possible

// such that exactly Math.Floor(N/2) elements

// are selected and no two selected

// elements are adjacent to each other

using System;

class GFG{

// Function return the maximum sum

// possible under given condition

static int MaximumSum(int []a, int n)

{

 int [,]dp = new int[n + 1, 2];

 // Base case

 dp[2, 1] = a[1];

 dp[2, 0] = a[0];

 for(int i = 3; i < n + 1; i++)

 {

 // When i is odd

 if (i % 2 == 1)

 {

 int temp = Math.Max((Math.Max(dp[i - 3, 1],

 dp[i - 3, 0])),

 Math.Max(dp[i - 2, 1],

 dp[i - 2, 0]));

 dp[i, 1] = a[i - 1] + temp;

 dp[i, 0] = Math.Max((Math.Max(a[i - 2] +

 dp[i - 2, 0],

 a[i - 2] +

 dp[i - 3, 1])),

 Math.Max(a[i - 2] +

 dp[i - 3, 0],

 a[i - 3] +

 dp[i - 3, 0]));

 }

 

 // When i is even

 else

 {

 dp[i, 1] = a[i - 1] + (Math.Max((

 Math.Max(dp[i - 2, 1],

 dp[i - 2, 0])),

 dp[i - 1, 0]));

 dp[i, 0] = a[i - 2] + dp[i - 2, 0];

 }

 }

 

 // Maximum of if we pick last element or not

 return Math.Max(dp[n, 1], dp[n, 0]);

}

static int max(int []arr)

{

 return 1;

}

// Driver code

public static void Main(String[] args)

{

 int []A = { 1, 2, 3, 4, 5, 6 };

 int N = A.Length;

 Console.Write(MaximumSum(A, N));

}

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    12
    
    
    
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

