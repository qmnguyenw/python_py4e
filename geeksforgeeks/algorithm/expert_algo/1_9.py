Total number Of valid Home delivery arrangements



Given number of orders, find the number of valid arrangements of orders where
delivery of ith order is always after the pickup of ith order. **Examples:**

>  **Input:** N = 1  
>  **Output:** 1  
> Here total event is 2. They are {P1, D1}.  
> Total possible arrangement is 2! = 2. [P1, D1] and [D1, P1].  
> So only valid arrangement possible: [P1, D1].  
> [D1, P1] is invalid arrangement as delivery of 1st order is done before
> pickup of 1st order.
>
>  **Input:** N = 2  
>  **Output:** 6  
> Here total event is 4. They are {P1, D1, P2, D2}.  
> Here total possible arrangements are 4! = 24.  
> Among them 6 are valid arrangements:  
> [P1, P2, D1, D2], [P1, D1, P2, D2], [P1, P2, D2, D1], [P2, P1, D2, D1], [P2,
> P1, D1, D2], and [P2, D2, P1, D1].  
> Rest all are invalid arrangements.  
> Some invalid arrangements:  
> [P1, D1, D2, P2] – Delivery of 2nd order is done before pickup  
> [P2, D1, P1, D2] – Delivery of 1st order is done before pickup  
> [D1, D2, P2, P1] – Delivery of both order is before pickup

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach 1:**

  1. Consider N = 4, we have total of 8 events.
  2. There are 4 events for pickup {P1, P2, P3, P4} and 4 events for delivery {D1, D2, D3, D4}.
  3. If we consider only pickup events, there are no restrictions in arrangements between pickups. So, total possible arrangements 4!
  4. Now we consider delivery. We start from the last pickup we made.
    * For D4, We can place D4 only after P4.  
That is P1, P2, P3, P4, __. So only 1 valid position.

    * For D3, We can place D3 in any one of this following position.  
They are P1, P2, P3, __, P4, __, D4, __ . So 3 valid position.

    * For D2, We can place D2 in any one of this following position.  
They are P1, P2, __, P3, __, P4, __, D4, __, D3 __ .So 5 valid position.

    * For D1, We can place D1 in any one of this following position.  
They are P1, __, P2, __, P3, __, P4, __, D4, __, D3 __, D2, __ .So, 7 valid
positions.

So total valid arrangements: 4! * (1 * 3 * 5 * 7)

For any N, total valid arrangements:

  

  

![N! * \(1 * 3 * 5 * ... * \(2 * N - 1\)\)
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-3c5e032fcf64c4b9901b4306bebe9337_l3.png)

Below is the implementation of the above approach.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find arrangements

int Arrangements(int N)

{

 int result = 1;

 

 for(int i = 1; i <= N; i++) 

 {

 // Here, i for factorial and

 // (2*i-1) for series 

 result = result * i * (2 * i - 1);

 }

 return result;

}

 

// Driver code

int main()

{

 int N = 4;

 

 cout << Arrangements(N);

 

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

// Java implementation of the above approach

class GFG{

 

// Function to find arrangements 

public static int Arrangements(int N) 

{ 

 int result = 1; 

 

 for(int i = 1; i <= N; i++)

 { 

 

 // Here, i for factorial and

 // (2*i-1) for series 

 result = result * i * (2 * i - 1); 

 } 

 return result; 

} 

 

// Driver code 

public static void main(String[] args)

{

 int N = 4; 

 

 System.out.print(Arrangements(N));

}

}

 

// This code is contributed by divyeshrabadiya07  
  
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

# Python3 implementation of the above approach

 

# Function to find arrangements

def Arrangements(N):

 

 result = 1

 

 for i in range(1, N + 1):

 

 # Here, i for factorial and

 # (2*i-1) for series 

 result = result * i * (2 * i - 1)

 

 return result

 

# Driver code

N = 4;

print(Arrangements(N));

 

# This code is contributed by Akanksha_Rai  
  
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

// C# implementation of the above approach

using System;

 

class GFG{ 

 

// Function to find arrangements 

public static int Arrangements(int N) 

{ 

 int result = 1; 

 

 for(int i = 1; i <= N; i++) 

 { 

 

 // Here, i for factorial and 

 // (2*i-1) for series 

 result = result * i * (2 * i - 1); 

 } 

 return result; 

} 

 

// Driver code 

public static void Main(String[] args) 

{ 

 int N = 4; 

 

 Console.Write(Arrangements(N)); 

} 

} 

 

// This code is contributed by AnkitRai01  
  
---  
  
 __

 __

 **Output:**

    
    
    2520
    

_**Time complexity: O(N)  
Auxiliary Space complexity: O(1)**_

 **Approach 2:**

  1. For N number of orders, we have

![  Total events = 2 * N ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-96ad6bbb1440f3558bdfa39e2323fa0d_l3.png)

  2. So the total number of arrangements possible is ![ \( 2 * N \)!  ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-e5516b66a880be808726547befd0f9cc_l3.png)
  3. Now each order can only be valid if delivery is one after pickup.

For each [Pi, Di], we can’t change this arrangement ie we can’t do [Di,
Pi].There is only one valid arrangement for each such order. So we need to
divide by 2 for each order. So total valid arrangement is ![ \( 2 * N \)! / 2
^ N  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-9fce4b1ffb222e2f08a1034b6af9d2b8_l3.png)

Below is the implementation of the above approach.  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the above approach

 

#include <bits/stdc++.h>

using namespace std;

 

// Function to find arrangements

int Arrangements(int N)

{

 int result = 1;

 

 for (int i = 1; i <= 2 * N; i += 2)

 result = (result * i * (i + 1)) / 2;

 

 return result;

}

 

// Driver code

int main()

{

 int N = 4;

 

 cout << Arrangements(N);

 

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

// Java implementation of the above approach

import java.util.*;

class GFG{

 

// Function to find arrangements

public static int Arrangements(int N)

{

 int result = 1;

 

 for (int i = 1; i <= 2 * N; i += 2)

 result = (result * i * (i + 1)) / 2;

 

 return result;

}

 

// Driver code

public static void main(String args[])

{

 int N = 4;

 

 System.out.print(Arrangements(N));

}

}

 

// This code is contributed by Code_Mech  
  
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

# Python3 implementation of the above approach

 

# Function to find arrangements

def Arrangements(N):

 result = 1;

 

 for i in range(1, (2 * N) + 1, 2):

 result = (result * i * (i + 1)) / 2;

 

 return int(result);

 

# Driver code

if __name__ == '__main__':

 N = 4;

 

 print(Arrangements(N));

 

# This code is contributed by gauravrajput1  
  
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

// C# implementation of the above approach

using System;

class GFG{

 

// Function to find arrangements

public static int Arrangements(int N)

{

 int result = 1;

 

 for (int i = 1; i <= 2 * N; i += 2)

 result = (result * i * (i + 1)) / 2;

 

 return result;

}

 

// Driver code

public static void Main()

{

 int N = 4;

 

 Console.Write(Arrangements(N));

}

}

 

// This code is contributed by Code_Mech  
  
---  
  
 __

 __

 **Output:**

    
    
    2520
    

_**Time complexity: O(N)  
Auxiliary Space complexity: O(1)**_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

