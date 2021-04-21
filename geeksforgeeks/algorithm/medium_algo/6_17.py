Count of triples (A, B, C) where A*C is greater than B*B



Given three integers **A** , **B** and **C**. The task is to count the number
of triples **(a, b, c)** such that **a * c > b2**, where **0 < a <= A**, **0 <
b <= B** and **0 < c <= C**.

 **Examples:**

>  **Input:** A = 3, B = 2, C = 2  
>  **Output:** 6  
> Following triples are counted :  
> (1, 1, 2), (2, 1, 1), (2, 1, 2), (3, 1, 1), (3, 1, 2) and (3, 2, 2).
>
>  **Input:** A = 3, B = 3, C = 3  
>  **Output:** 11

 **Naive approach:**  
The brute force approach is to consider all possible triples **(a, b, c)** and
count those triples that satisfy the constraint **a*c > b2**.

  

  

Below is the implementation of the given approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation

#include <bits/stdc++.h>

using namespace std;

 

// function to return the count

// of the valid triplets

long long countTriplets(int A, int B, int C)

{

 long long ans = 0;

 for (int i = 1; i <= A; i++) {

 for (int j = 1; j <= B; j++) {

 for (int k = 1; k <= C; k++) {

 if (i * k > j * j)

 ans++;

 }

 }

 }

 return ans;

}

 

// Driver Code

int main()

{

 int A, B, C;

 A = 3, B = 2, C = 2;

 

 // function calling

 cout << countTriplets(A, B, C);

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

import java.util.*;

 

class GFG

{

 

// function to return the count

// of the valid triplets

static long countTriplets(int A, int B, int C)

{

 long ans = 0;

 for (int i = 1; i <= A; i++) 

 {

 for (int j = 1; j <= B; j++)

 {

 for (int k = 1; k <= C; k++) 

 {

 if (i * k > j * j)

 ans++;

 }

 }

 }

 return ans;

}

 

// Driver Code

public static void main (String[] args)

{

 int A = 3, B = 2, C = 2;

 

 // function calling

 System.out.println(countTriplets(A, B, C));

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

# Python3 implementation for above approach

 

# function to return the count

# of the valid triplets

def countTriplets(A, B, C):

 ans = 0

 for i in range(1, A + 1):

 for j in range(1, B + 1):

 for k in range(1, C + 1):

 if (i * k > j * j):

 ans += 1

 

 return ans

 

# Driver Code

A = 3

B = 2

C = 2

 

# function calling

print(countTriplets(A, B, C))

 

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

 

// function to return the count

// of the valid triplets

static long countTriplets(int A, 

 int B, int C)

{

 long ans = 0;

 for (int i = 1; i <= A; i++) 

 {

 for (int j = 1; j <= B; j++)

 {

 for (int k = 1; k <= C; k++) 

 {

 if (i * k > j * j)

 ans++;

 }

 }

 }

 return ans;

}

 

// Driver Code

public static void Main (String[] args)

{

 int A = 3, B = 2, C = 2;

 

 // function calling

 Console.WriteLine(countTriplets(A, B, C));

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    

**Time Complexity:**![O\(A*B*C\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f7a197c3c12517d8f22c7c7f73ab9b1c_l3.png).

 **Efficient approach:**

Let us count all triplets for a given value of **b = k** for all **k** from
**1** to **B**.

  1. For a given **b = k** we need to find all **a = i** and **c = j** that satisfy **i * j > k2**
  2. For **a = i** , find smallest **c = j** that satisfies the condition.

Since **c = j** satisfies this condition therefore **c = j + 1, c = j + 2, …**
and so on, will also satisfy the condition.  
So we can easily count all triples in which **a = i** and **b = k**.

  3. Also if for some **a = i** , **c = j** is the smallest value such that the given condition is satisfied so it can be observed that **a = j** and all **c >= i** also satisfy the condition.

The condition is also satisfied by **a = j + 1** and **c >= i** that is all
values **a >= j** and **c >= i** also satisfy the condition.

  4. The above observation helps us to count all triples in which **b = k** and **a >= j** easily.
  5. Now we need to count all triples in which **b = k** and **i < a < j**.
  6. Thus for a given value of **b = k** we only need to go upto **a = square root of k**.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation

#include <bits/stdc++.h>

using namespace std;

 

// Counts the number of triplets

// for a given value of b

long long getCount(int A, int B2,

 int C)

{

 long long count = 0;

 

 // Count all triples in which a = i

 for (int i = 1; i <= A; i++) {

 

 // Smallest value j

 // such that i*j > B2

 long long j = (B2 / i) + 1;

 

 // Count all (i, B2, x)

 // such that x >= j

 if (C >= j)

 count = (count + C - j + 1);

 

 // count all (x, B2, y) such

 // that x >= j this counts

 // all such triples in

 // which a >= j

 if (A >= j && C >= i)

 count = (count

 + (C - i + 1)

 * (A - j + 1));

 

 // As all triples with a >= j

 // have been counted reduce

 // A to j - 1.

 if (A >= j)

 A = j - 1;

 }

 return count;

}

 

// Counts the number of triples that

// satisfy the given constraints

long long countTriplets(int A, int B,

 int C)

{

 long long ans = 0;

 for (int i = 1; i <= B; i++) {

 

 // GetCount of triples in which b = i

 ans = (ans

 + getCount(A, i * i, C));

 }

 return ans;

}

 

// Driver Code

int main()

{

 int A, B, C;

 A = 3, B = 2, C = 2;

 

 // Function calling

 cout << countTriplets(A, B, C);

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

 

// Counts the number of triplets

// for a given value of b

static long getCount(int A, int B2, int C)

{

 long count = 0;

 

 // Count all triples in which a = i

 for (int i = 1; i <= A; i++)

 {

 

 // Smallest value j

 // such that i*j > B2

 long j = (B2 / i) + 1;

 

 // Count all (i, B2, x)

 // such that x >= j

 if (C >= j)

 count = (count + C - j + 1);

 

 // count all (x, B2, y) such

 // that x >= j this counts

 // all such triples in

 // which a >= j

 if (A >= j && C >= i)

 count = (count + (C - i + 1) *

 (A - j + 1));

 

 // As all triples with a >= j

 // have been counted reduce

 // A to j - 1.

 if (A >= j)

 A = (int) (j - 1);

 }

 return count;

}

 

// Counts the number of triples that

// satisfy the given constraints

static long countTriplets(int A, int B, int C)

{

 long ans = 0;

 for (int i = 1; i <= B; i++)

 {

 

 // GetCount of triples in which b = i

 ans = (ans + getCount(A, i * i, C));

 }

 return ans;

}

 

// Driver Code

public static void main(String[] args)

{

 int A, B, C;

 A = 3; B = 2; C = 2;

 

 // Function calling

 System.out.println(countTriplets(A, B, C));

}

}

 

// This code is contributed by Princi Singh  
  
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

# Python3 implementation

 

# Counts the number of triplets

# for a given value of b

def getCount(A, B2, C):

 

 count = 0

 

 # Count all triples in which a = i

 i=1

 while(i<A):

 

 # Smallest value j

 # such that i*j > B2

 j = (B2 // i) + 1

 # Count all (i, B2, x)

 # such that x >= j

 if (C >= j):

 count = count + C - j + 1

 

 # count all (x, B2, y) such

 # that x >= j this counts

 # all such triples in

 # which a >= j

 if (A>= j and C >= i):

 count = count+ (C - i + 1) * (A - j + 1)

 

 # As all triples with a >= j

 # have been counted reduce

 # A to j - 1.

 if (A >= j):

 A = j - 1

 i+=1

 

 return count

 

 

# Counts the number of triples that

# satisfy the given constraints

def countTriplets(A, B, C):

 

 ans = 0

 for i in range(1,B+1):

 # GetCount of triples in which b = i

 ans = (ans+ getCount(A, i * i, C))

 

 return ans

 

 

# Driver Code

 

A = 3

B = 2

C = 2

 

# Function calling

print(countTriplets(A, B, C))

 

# This code is contributed by shubhamsingh10  
  
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

using System.Collections.Generic; 

 

class GFG 

{

 

// Counts the number of triplets

// for a given value of b

static long getCount(int A, int B2, int C)

{

 long count = 0;

 

 // Count all triples in which a = i

 for (int i = 1; i <= A; i++)

 {

 

 // Smallest value j

 // such that i*j > B2

 long j = (B2 / i) + 1;

 

 // Count all (i, B2, x)

 // such that x >= j

 if (C >= j)

 count = (count + C - j + 1);

 

 // count all (x, B2, y) such

 // that x >= j this counts

 // all such triples in

 // which a >= j

 if (A >= j && C >= i)

 count = (count + (C - i + 1) *

 (A - j + 1));

 

 // As all triples with a >= j

 // have been counted reduce

 // A to j - 1.

 if (A >= j)

 A = (int) (j - 1);

 }

 return count;

}

 

// Counts the number of triples that

// satisfy the given constraints

static long countTriplets(int A, int B, int C)

{

 long ans = 0;

 for (int i = 1; i <= B; i++)

 {

 

 // GetCount of triples in which b = i

 ans = (ans + getCount(A, i * i, C));

 }

 return ans;

}

 

// Driver Code

public static void Main(String[] args)

{

 int A, B, C;

 A = 3; B = 2; C = 2;

 

 // Function calling

 Console.WriteLine(countTriplets(A, B, C));

}

}

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

 **Output:**

    
    
    6
    

**Time Complexity:**![O\(B^{2}\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d93c3f212f56863e3df1110d0800417f_l3.png)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

