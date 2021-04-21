Minimum increment or decrement operations required to make the array sorted



Given an array **arr[]** of **N** integers, the task is to sort the array in
non-decreasing order by performing the minimum number of operations. In a
single operation, an element of the array can either be incremented or
decremented by **1**. Print the minimum number of operations required.

 **Examples:**

>  **Input:** arr[] = {1, 2, 1, 4, 3}  
>  **Output:** 2  
> Add 1 to the 3rd element(1) and subtract 1 from  
> the 4th element(4) to get {1, 2, 2, 3, 3}
>
>  **Input:** arr[] = {1, 2, 2, 100}  
>  **Output:** 0  
> Given array is already sorted.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Observation:** Since we would like to minimize the number of operations
needed to sort the array the following should hold:

  

  

  * A number will never be decreased to value lesser than the minimum of the initial array.
  * A number will never be increased to a value greater than the maximum of the initial array.
  * The number of operations required to change a number from X to Y is abs(X – Y).

 **Approach :** Based on the above observation, this problem can be solved
using dynamic programming.

  1. Let **DP(i, j)** represent the minimum operations needed to make the **1 st i** elements of the array sorted in non-decreasing order when the **i th** element is equal to **j**.
  2. Now **DP(N, j)** needs to be calculated for all possible values of **j** where **N** is the size of the array. According to the observations, **j ≥ smallest element of the initial array** and **j ≤ the largest element of the initial array**.
  3. The base cases in the **DP(i, j)** where **i = 1** can be easily answered. What are the minimum operations needes to sort the **1 st** element in non-decreasing order such that the **1 st** element is equal to **j**?. **DP(1, j) = abs( array[1] – j)**.
  4. Now consider **DP(i, j)** for **i > 1**. If **i th** element is set to **j** then the **1 st** **i – 1** elements need to be sorted and the **(i – 1) th** element has to be **≤ j** i.e. **DP(i, j) = (minimum of DP(i – 1, k)** where **k** goes from **1** to **j** ) **\+ abs(array[i] – j)**
  5. Using the above recurrence relation and the base cases, the result can be easily calculated.

Below is the implementation of the above aprpoach:  

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

// of given operations required

// to sort the array

int getMinimumOps(vector<int> ar)

{

 // Number of elements in the array

 int n = ar.size();

 

 // Smallest element in the array

 int small = *min_element(ar.begin(), ar.end());

 

 // Largest element in the array

 int large = *max_element(ar.begin(), ar.end());

 

 /*

 dp(i, j) represents the minimum number

 of operations needed to make the 

 array[0 .. i] sorted in non-decreasing

 order given that ith element is j

 */

 int dp[n][large + 1];

 

 // Fill the dp[]][ array for base cases

 for (int j = small; j <= large; j++) {

 dp[0][j] = abs(ar[0] - j);

 }

 

 /*

 Using results for the first (i - 1) 

 elements, calculate the result 

 for the ith element

 */

 for (int i = 1; i < n; i++) {

 int minimum = INT_MAX;

 for (int j = small; j <= large; j++) {

 

 /*

 If the ith element is j then we can have

 any value from small to j for the i-1 th

 element

 We choose the one that requires the 

 minimum operations

 */

 minimum = min(minimum, dp[i - 1][j]);

 dp[i][j] = minimum + abs(ar[i] - j);

 }

 }

 

 /*

 If we made the (n - 1)th element equal to j

 we required dp(n-1, j) operations

 We choose the minimum among all possible 

 dp(n-1, j) where j goes from small to large

 */

 int ans = INT_MAX;

 for (int j = small; j <= large; j++) {

 ans = min(ans, dp[n - 1][j]);

 }

 

 return ans;

}

 

// Driver code

int main()

{

 vector<int> ar = { 1, 2, 1, 4, 3 };

 

 cout << getMinimumOps(ar);

 

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

// Java implementation of the approach

import java.util.*;

 

class GFG 

{

 

// Function to return the minimum number

// of given operations required

// to sort the array

static int getMinimumOps(Vector<Integer> ar)

{

 // Number of elements in the array

 int n = ar.size();

 

 // Smallest element in the array

 int small = Collections.min(ar);

 

 // Largest element in the array

 int large = Collections.max(ar);

 

 /*

 dp(i, j) represents the minimum number

 of operations needed to make the 

 array[0 .. i] sorted in non-decreasing

 order given that ith element is j

 */

 int [][]dp = new int[n][large + 1];

 

 // Fill the dp[]][ array for base cases

 for (int j = small; j <= large; j++)

 {

 dp[0][j] = Math.abs(ar.get(0) - j);

 }

 

 /*

 Using results for the first (i - 1) 

 elements, calculate the result 

 for the ith element

 */

 for (int i = 1; i < n; i++) 

 {

 int minimum = Integer.MAX_VALUE;

 for (int j = small; j <= large; j++)

 {

 

 /*

 If the ith element is j then we can have

 any value from small to j for the i-1 th

 element

 We choose the one that requires the 

 minimum operations

 */

 minimum = Math.min(minimum, dp[i - 1][j]);

 dp[i][j] = minimum + Math.abs(ar.get(i) - j);

 }

 }

 

 /*

 If we made the (n - 1)th element equal to j

 we required dp(n-1, j) operations

 We choose the minimum among all possible 

 dp(n-1, j) where j goes from small to large

 */

 int ans = Integer.MAX_VALUE;

 for (int j = small; j <= large; j++) 

 {

 ans = Math.min(ans, dp[n - 1][j]);

 }

 return ans;

}

 

// Driver code

public static void main(String[] args)

{

 Integer []arr = { 1, 2, 1, 4, 3 }; 

 Vector<Integer> ar = new Vector<>(Arrays.asList(arr));

 

 System.out.println(getMinimumOps(ar));

}

}

 

// This code is contributed by 29AjayKumar  
  
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

# of given operations required

# to sort the array

def getMinimumOps(ar):

 

 # Number of elements in the array

 n = len(ar)

 

 # Smallest element in the array

 small = min(ar)

 

 # Largest element in the array

 large = max(ar)

 

 """

 dp(i, j) represents the minimum number

 of operations needed to make the

 array[0 .. i] sorted in non-decreasing

 order given that ith element is j

 """

 dp = [[ 0 for i in range(large + 1)] 

 for i in range(n)]

 

 # Fill the dp[]][ array for base cases

 for j in range(small, large + 1):

 dp[0][j] = abs(ar[0] - j)

 """

 /*

 Using results for the first (i - 1)

 elements, calculate the result

 for the ith element

 */

 """

 for i in range(1, n):

 minimum = 10**9

 for j in range(small, large + 1):

 

 # """

 # /*

 # If the ith element is j then we can have

 # any value from small to j for the i-1 th

 # element

 # We choose the one that requires the

 # minimum operations

 # """

 minimum = min(minimum, dp[i - 1][j])

 dp[i][j] = minimum + abs(ar[i] - j)

 """

 /*

 If we made the (n - 1)th element equal to j

 we required dp(n-1, j) operations

 We choose the minimum among all possible

 dp(n-1, j) where j goes from small to large

 */

 """

 ans = 10**9

 for j in range(small, large + 1):

 ans = min(ans, dp[n - 1][j])

 

 return ans

 

# Driver code

ar = [1, 2, 1, 4, 3]

 

print(getMinimumOps(ar))

 

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

// C# implementation of the approach

using System;

using System.Linq;

using System.Collections.Generic; 

 

class GFG 

{

 

// Function to return the minimum number

// of given operations required

// to sort the array

static int getMinimumOps(List<int> ar)

{

 // Number of elements in the array

 int n = ar.Count;

 

 // Smallest element in the array

 int small = ar.Min();

 

 // Largest element in the array

 int large = ar.Max();

 

 /*

 dp(i, j) represents the minimum number

 of operations needed to make the 

 array[0 .. i] sorted in non-decreasing

 order given that ith element is j

 */

 int [,]dp = new int[n, large + 1];

 

 // Fill the dp[], array for base cases

 for (int j = small; j <= large; j++)

 {

 dp[0, j] = Math.Abs(ar[0] - j);

 }

 

 /*

 Using results for the first (i - 1) 

 elements, calculate the result 

 for the ith element

 */

 for (int i = 1; i < n; i++) 

 {

 int minimum = int.MaxValue;

 for (int j = small; j <= large; j++)

 {

 

 /*

 If the ith element is j then we can have

 any value from small to j for the i-1 th

 element

 We choose the one that requires the 

 minimum operations

 */

 minimum = Math.Min(minimum, dp[i - 1, j]);

 dp[i, j] = minimum + Math.Abs(ar[i] - j);

 }

 }

 

 /*

 If we made the (n - 1)th element equal to j

 we required dp(n-1, j) operations

 We choose the minimum among all possible 

 dp(n-1, j) where j goes from small to large

 */

 int ans = int.MaxValue;

 for (int j = small; j <= large; j++) 

 {

 ans = Math.Min(ans, dp[n - 1, j]);

 }

 return ans;

}

 

// Driver code

public static void Main(String[] args)

{

 int []arr = { 1, 2, 1, 4, 3 }; 

 List<int> ar = new List<int>(arr);

 

 Console.WriteLine(getMinimumOps(ar));

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

**Complexity Analysis:** Time complexity for the above approach is O(N * R)
where N is the number of elements in the array and R = largest – smallest
element of the array + 1.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

