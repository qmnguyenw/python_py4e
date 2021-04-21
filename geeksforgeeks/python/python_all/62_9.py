Length of race track based on the final distance between participants



Given three integers **A, B** and **C** , the task is to find the length of a
race track if 3 racers are competing in a race where the first racer beats the
second racer by **A** metres, the first racer beats the third racer by **B**
metres and the second racer beats the third by **C** metres.

 **Examples:**

>  **Input:** A = 11, B = 90, C = 80  
>  **Output:** 880
>
>  **Input:** A = 10, B = 20, C = 12  
>  **Output:** 60

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach :**  
Let X be the length of the race track.

  

  

 **Case 1:** By the time when the First racer finished the race, distances
covered by all the 3 racers are:  
First = X, Second = X – A, Third = X – B  
Let the time taken by the First racer to finish the race be **T 1.**

 **Case 2:** By the time when the Second racer finished the race, distances
covered by the remaining 2 racers are:  
Second = X, Third = X – C  
Let the time taken by the Second racer to finish the race be **T 2.**

The ratio of the speeds of the Second and the Third racer will be constant in
both case 1 and case 2 which implies:

>  **= > ((X – A) / T1) / ((X – B) / T1) = (X / T2) / ((X – C) / T2)  
> => (X – A) / (X – B) = (X) / (X – C)  
> => X2 – A*X – C*X + A*C = X2 – B*X  
> => A*C = (C + A – B)*X  
> => X = A*C / (C + A – B)**

Below is the implementation of the above program:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Program for the above approach

 

#include <bits/stdc++.h>

using namespace std;

#define int long long

 

int32_t main()

{

 int A = 11;

 int B = 90;

 int C = 80;

 

 int ans = C * A;

 ans = ans / (C + A - B);

 

 cout << ans << endl;

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

// Java Program for the

// above approach

 

import java.util.Scanner;

 

class GFG {

 public static void main(String args[])

 {

 int a = 11;

 int b = 90;

 int c = 80;

 

 System.out.println(c * a

 / (c + a - b));

 }

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

# Python3 Program for the

# above approach 

 

# Function to get the length

# of the race track

def findlength(a, b, c):

 # return the answer

 return c * a/(c + a-b)

 

a = 11

b = 90

c = 80

 

print(findlength(a, b, c))   
  
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

// C# program for the above approach

using System;

class GFG{

 

static void Main()

{

 int a = 11; 

 int b = 90; 

 int c = 80; 

 

 Console.WriteLine(c * a / (c + a - b));

}

}

 

// This code is contributed by divyeshrabadiya07   
  
---  
  
__

__

**Output:**

    
    
    880
    

**Note:** This is an interview question asked at **POSTMAN (SDE Internship)**

Want to learn from the best curated videos and practice problems, check out
the **C++ Foundation Course **for Basic to Advanced C++ and **C++ STL Course**
for foundation plus STL.

My Personal Notes _arrow_drop_up_

Save

