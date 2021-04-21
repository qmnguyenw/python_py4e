Minimum area of square holding two identical rectangles



Given the length **L** and breadth **B** of two identical rectangles, the task
is to find the minimum area of a square in which the two identical rectangles
with dimensions **L × B** can be embedded.

 **Examples:**

>  **Input:** L = 7, B = 4  
>  **Output:** 64  
>  **Explanation:** Two rectangles with sides 7 x 4 can fit into square with
> side 8. By placing two rectangles with side 4 upon each other and the length
> of contact is 7.
>
>  **Input:** L = 1, B = 3  
>  **Output:** 9  
>  **Explanation:** Two rectangles with sides 1 x 3 can fit into square with
> side 3. By placing two rectangles with side 1 upon each other and a gap of 1
> between the 2 rectangles.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  * If one side of the rectangle is lesser than or equal to half the length of the other side then the side of the square is the longer side of the rectangle.
  * If twice the length of the smaller side is greater than the larger side, then the side of the square is twice the length of the smaller side of the rectangle.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for the above problem

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the

// area of the square

int areaSquare(int L, int B)

{

 // Larger side of rectangle

 int large = max(L, B);

 

 // Smaller side of the rectangle

 int small = min(L, B);

 

 if (large >= 2 * small)

 return large * large;

 else

 return (2 * small) * (2 * small);

}

 

// Driver code

int main()

{

 int L = 7;

 int B = 4;

 cout << areaSquare(L, B);

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

import java.io.*;

 

class GFG{

 

// Function to find the

// area of the square

static int areaSquare(int L, int B)

{

 

 // Larger side of rectangle

 int large = Math.max(L, B);

 

 // Smaller side of the rectangle

 int small = Math.min(L, B);

 

 if (large >= 2 * small)

 {

 return large * large;

 }

 else

 {

 return (2 * small) * (2 * small);

 }

}

 

// Driver code

public static void main(String[] args)

{

 int L = 7;

 int B = 4;

 

 System.out.println(areaSquare(L, B));

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

# Python3 program for the above problem

 

# Function to find the

# area of the square

def areaSquare(L, B):

 

 # Larger side of rectangle

 large = max(L, B)

 

 # Smaller side of the rectangle

 small = min(L, B)

 

 if(large >= 2 * small):

 return large * large

 else:

 return (2 * small) * (2 * small)

 

# Driver code

if __name__ == '__main__':

 

 L = 7

 B = 4

 

 print(areaSquare(L, B))

 

# This code is contributed by Shivam Singh  
  
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

// C# program for the above problem

using System;

 

class GFG{

 

// Function to find the

// area of the square

public static int areaSquare(int L, int B)

{

 

 // Larger side of rectangle

 int large = Math.Max(L, B);

 

 // Smaller side of the rectangle

 int small = Math.Min(L, B);

 

 if (large >= 2 * small)

 {

 return large * large;

 }

 else

 {

 return (2 * small) * (2 * small);

 }

}

 

// Driver code

public static void Main()

{

 int L = 7;

 int B = 4;

 

 Console.Write(areaSquare(L, B));

}

}

 

// This code is contributed by Code_Mech  
  
---  
  
 __

 __

 **Output:**

    
    
    64
    

_  
**Time Complexity:** O(1)  
 **Auxiilary Space Complexity:** O(1)  
_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

