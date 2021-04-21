Construct an Array of size N in which sum of odd elements is equal to sum of
even elements



Given an **integer N** which is always even, the task is to create an array of
size **N** which contains **N/2 even numbers** and **N/2 odd numbers**. All
the elements of array should be distinct and the sum of even numbers is equal
to the sum of odd numbers. If no such array exists then print -1.  
 **Examples:**  

> **Input:** N = 8  
> **Output:** 2 4 6 8 1 3 5 11  
> **Explanation:**  
> The array has 8 distinct elements which have equal sum of odd and even
> numbers, i.e., (2 + 4 + 6 + 8 = 1 + 3 + 5 + 11).  
>  **Input:** N = 10  
> **Output:** -1  
> **Explanation:**  
> It is not possible to construct array of size 10.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** To solve the problem mentioned above the very first observation
is that it is _not possible to create an array that has size N which is a
multiple of 2 but not multiple of 4_. Because, if that happens then the sum of
one half which contains odd numbers will always be odd and the sum of another
half which contains even numbers will always be even, hence the sum of both
halves can’t be the same.  
Therefore, the array which satisfies the problem statement should always have
a **size N which is a multiple of 4**. The approach is to first construct N/2
even numbers starting from 2, which is the first half of the array. Then
create another part of the array starting from 1 and finally calculate the
last odd element such that it makes both the halves equal. In order to do so
the **last element of odd numbers should be (N/2) – 1 + N**.  
Below is the implementation of the above approach:  

## CPP

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to Create an array

// of size N consisting of distinct

// elements where sum of odd elements

// is equal to sum of even elements

#include <bits/stdc++.h>

using namespace std;

// Function to construct the required array

void arrayConstruct(int N)

{

 // To construct first half,

 // distinct even numbers

 for (int i = 2; i <= N; i = i + 2)

 cout << i << " ";

 // To construct second half,

 // distinct odd numbers

 for (int i = 1; i < N - 1; i = i + 2)

 cout << i << " ";

 // Calculate the last number of second half

 // so as to make both the halves equal

 cout << N - 1 + (N / 2) << endl;

}

// Function to construct the required array

void createArray(int N)

{

 // check if size is multiple of 4

 // then array exist

 if (N % 4 == 0)

 // function call to construct array

 arrayConstruct(N);

 else

 cout << -1 << endl;

}

// Driver code

int main()

{

 int N = 8;

 createArray(N);

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

// Java program to Create an array

// of size N consisting of distinct

// elements where sum of odd elements

// is equal to sum of even elements

class GFG{

 

// Function to conthe required array

static void arrayConstruct(int N)

{

 

 // To confirst half,

 // distinct even numbers

 for (int i = 2; i <= N; i = i + 2)

 System.out.print(i+ " ");

 

 // To consecond half,

 // distinct odd numbers

 for (int i = 1; i < N - 1; i = i + 2)

 System.out.print(i+ " ");

 

 // Calculate the last number of second half

 // so as to make both the halves equal

 System.out.print(N - 1 + (N / 2) +"\n");

}

 

// Function to conthe required array

static void createArray(int N)

{

 

 // check if size is multiple of 4

 // then array exist

 if (N % 4 == 0)

 

 // function call to conarray

 arrayConstruct(N);

 

 else

 System.out.print(-1 +"\n");

}

 

// Driver code

public static void main(String[] args)

{

 int N = 8;

 

 createArray(N);

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

# python3 program to Create an array

# of size N consisting of distinct

# elements where sum of odd elements

# is equal to sum of even elements

# Function to construct the required array

def arrayConstruct(N):

 # To construct first half,

 # distinct even numbers

 for i in range(2, N + 1, 2):

 print(i,end=" ")

 # To construct second half,

 # distinct odd numbers

 for i in range(1, N - 1, 2):

 print(i, end=" ")

 # Calculate the last number of second half

 # so as to make both the halves equal

 print(N - 1 + (N // 2))

# Function to construct the required array

def createArray(N):

 # check if size is multiple of 4

 # then array exist

 if (N % 4 == 0):

 # function call to construct array

 arrayConstruct(N)

 else:

 cout << -1 << endl

# Driver code

if __name__ == '__main__':

 N = 8

 createArray(N)

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

// C# program to Create an array

// of size N consisting of distinct

// elements where sum of odd elements

// is equal to sum of even elements

using System;

class GFG{

 

// Function to conthe required array

static void arrayConstruct(int N)

{

 

 // To confirst half,

 // distinct even numbers

 for (int i = 2; i <= N; i = i + 2)

 Console.Write(i + " ");

 

 // To consecond half,

 // distinct odd numbers

 for (int i = 1; i < N - 1; i = i + 2)

 Console.Write(i + " ");

 

 // Calculate the last number of second half

 // so as to make both the halves equal

 Console.Write(N - 1 + (N / 2) +"\n");

}

 

// Function to conthe required array

static void createArray(int N)

{

 

 // check if size is multiple of 4

 // then array exist

 if (N % 4 == 0)

 

 // function call to conarray

 arrayConstruct(N);

 

 else

 Console.Write(-1 +"\n");

}

 

// Driver code

public static void Main(String[] args)

{

 int N = 8;

 

 createArray(N);

}

}

// This code is contributed by Rajput-Ji  
  
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

// JavaScript program to Create an array

// of size N consisting of distinct

// elements where sum of odd elements

// is equal to sum of even elements

// Function to construct the required array

function arrayConstruct(N)

{

 // To construct first half,

 // distinct even numbers

 for (let i = 2; i <= N; i = i + 2)

 document.write(i + " ");

 // To construct second half,

 // distinct odd numbers

 for (let i = 1; i < N - 1; i = i + 2)

 document.write(i + " ");

 // Calculate the last number of second half

 // so as to make both the halves equal

 document.write(N - 1 + (N / 2) + "<br>");

}

// Function to construct the required array

function createArray(N)

{

 // check if size is multiple of 4

 // then array exist

 if (N % 4 == 0)

 // function call to construct array

 arrayConstruct(N);

 else

 document.write(-1 + "<br>");

}

// Driver code

 let N = 8;

 createArray(N);

// This code is contributed by Surbhi Tyagi.

</script>  
  
---  
  
 __

 __

 **Output:**

    
    
    2 4 6 8 1 3 5 11

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

