Minimum number of operations to convert a given sequence into a Geometric
Progression



Given a sequence of N elements, only three operations can be performed on any
element at most one time. The operations are:

  1. Add one to the element.
  2. Subtract one from the element.
  3. Leave the element unchanged.

Perform any one of the operations on all elements in the array. The task is to
find the minimum number of operations(addition and subtraction) that can be
performed on the sequence, in order to convert it into a Geometric
Progression. If it is not possible to generate a GP by performing the above
operations, print -1.

 **Examples** :

>  **Input** : a[] = {1, 1, 4, 7, 15, 33}  
>  **Output** : The minimum number of operations are 4.  
> Steps:
>
>   1. Keep a1 unchanged
>   2. Add one to a2.
>   3. Keep a3 unchanged
>   4. Subtract one from a4.
>   5. Subtract one from a5.
>   6. Add one to a6.
>

>
> The resultant sequence is {1, 2, 4, 8, 16, 32}
>
>  
>
>
>  
>
>
>  **Input** : a[] = {20, 15, 20, 15}  
>  **Output** : -1

 **Approach** The key observation to be made here is that any Geometric
Progression is uniquely determined by only its first two elements (Since the
ratio between each of the next pairs has to be the same as the ratio between
this pair, consisting of the first two elements). Since only **3*3**
permutations are possible. The possible combination of operations are (+1,
+1), (+1, 0), (+1, -1), (-1, +1), (-1, 0), (-1, -1), (0, +1), (0, 0) and (0,
-1). Using brute force all these **9** permutations and checking if they form
a GP in linear time will give us the answer. The minimum of the operations
which result in combinations which are in GP will be the answer.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find minimum number

// of operations to convert a given

// sequence to an Geometric Progression

#include <bits/stdc++.h>

using namespace std;

 

// Function to print the GP series

void construct(int n, pair<double, double> ans_pair)

{

 // Check for possibility

 if (ans_pair.first == -1) {

 cout << "Not possible";

 return;

 }

 double a1 = ans_pair.first;

 double a2 = ans_pair.second;

 double r = a2 / a1;

 

 cout << "The resultant sequence is:\n";

 for (int i = 1; i <= n; i++) {

 double ai = a1 * pow(r, i - 1);

 cout << ai << " ";

 }

}

 

// Function for getting the Arithmetic Progression

void findMinimumOperations(double* a, int n)

{

 int ans = INT_MAX;

 // The array c describes all the given set of

 // possible operations.

 int c[] = { -1, 0, 1 };

 // Size of c

 int possiblities = 3;

 

 // candidate answer

 int pos1 = -1, pos2 = -1;

 

 // loop through all the permutations of the first two

 // elements.

 for (int i = 0; i < possiblities; i++) {

 for (int j = 0; j < possiblities; j++) {

 

 // a1 and a2 are the candidate first two elements

 // of the possible GP.

 double a1 = a[1] + c[i];

 double a2 = a[2] + c[j];

 

 // temp stores the current answer, including the

 // modification of the first two elements.

 int temp = abs(a1 - a[1]) + abs(a2 - a[2]);

 

 if (a1 == 0 || a2 == 0)

 continue;

 

 // common ratio of the possible GP

 double r = a2 / a1;

 

 // To check if the chosen set is valid, and id yes

 // find the number of operations it takes.

 for (int pos = 3; pos <= n; pos++) {

 

 // ai is value of a[i] according to the assumed

 // first two elements a1, a2

 // ith element of an GP = a1*((a2-a1)^(i-1))

 double ai = a1 * pow(r, pos - 1);

 

 // Check for the "proposed" element to be only

 // differing by one

 if (a[pos] == ai) {

 continue;

 }

 else if (a[pos] + 1 == ai || a[pos] - 1 == ai) {

 temp++;

 }

 else {

 temp = INT_MAX; // set the temporary ans

 break; // to infinity and break

 }

 }

 

 // update answer

 if (temp < ans) {

 ans = temp;

 pos1 = a1;

 pos2 = a2;

 }

 }

 }

 if (ans == -1) {

 cout << "-1";

 return;

 }

 

 cout << "Minimum Number of Operations are " << ans << "\n";

 pair<double, double> ans_pair = { pos1, pos2 };

 

 // Calling function to print the sequence

 construct(n, ans_pair);

}

 

// Driver Code

int main()

{

 

 // array is 1-indexed, with a[0] = 0

 // for the sake of simplicity

 double a[] = { 0, 7, 20, 49, 125 };

 

 int n = sizeof(a) / sizeof(a[0]);

 

 // Function to print the minimum operations

 // and the sequence of elements

 findMinimumOperations(a, n - 1);

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

// Java program to find minimum number

// of operations to convert a given

// sequence to an Geometric Progression

import java.util.*;

 

class GFG

{

 

static class pair

{ 

 double first, second; 

 public pair(double first, double second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

} 

// Function to print the GP series

static void construct(int n, pair ans_pair)

{

 // Check for possibility

 if (ans_pair.first == -1)

 {

 System.out.print("Not possible");

 return;

 }

 double a1 = ans_pair.first;

 double a2 = ans_pair.second;

 double r = a2 / a1;

 

 System.out.print("The resultant sequence is:\n");

 for (int i = 1; i <= n; i++)

 {

 int ai = (int) (a1 * Math.pow(r, i - 1));

 System.out.print(ai + " ");

 }

}

 

// Function for getting the Arithmetic Progression

static void findMinimumOperations(double []a, int n)

{

 int ans = Integer.MAX_VALUE;

 

 // The array c describes all the given set of

 // possible operations.

 int c[] = { -1, 0, 1 };

 

 // Size of c

 int possiblities = 3;

 

 // candidate answer

 int pos1 = -1, pos2 = -1;

 

 // loop through all the permutations of the first two

 // elements.

 for (int i = 0; i < possiblities; i++) 

 {

 for (int j = 0; j < possiblities; j++) 

 {

 

 // a1 and a2 are the candidate first two elements

 // of the possible GP.

 double a1 = a[1] + c[i];

 double a2 = a[2] + c[j];

 

 // temp stores the current answer, including the

 // modification of the first two elements.

 int temp = (int) (Math.abs(a1 - a[1]) + Math.abs(a2 -
a[2]));

 

 if (a1 == 0 || a2 == 0)

 continue;

 

 // common ratio of the possible GP

 double r = a2 / a1;

 

 // To check if the chosen set is valid, and id yes

 // find the number of operations it takes.

 for (int pos = 3; pos <= n; pos++)

 {

 

 // ai is value of a[i] according to the assumed

 // first two elements a1, a2

 // ith element of an GP = a1*((a2-a1)^(i-1))

 double ai = a1 * Math.pow(r, pos - 1);

 

 // Check for the "proposed" element to be only

 // differing by one

 if (a[pos] == ai)

 {

 continue;

 }

 else if (a[pos] + 1 == ai || a[pos] - 1 == ai)

 {

 temp++;

 }

 else

 {

 temp = Integer.MAX_VALUE; // set the temporary ans

 break; // to infinity and break

 }

 }

 

 // update answer

 if (temp < ans) 

 {

 ans = temp;

 pos1 = (int) a1;

 pos2 = (int) a2;

 }

 }

 }

 if (ans == -1) 

 {

 System.out.print("-1");

 return;

 }

 

 System.out.print("Minimum Number of Operations are " + ans+
"\n");

 pair ans_pair = new pair( pos1, pos2 );

 

 // Calling function to print the sequence

 construct(n, ans_pair);

}

 

// Driver Code

public static void main(String[] args)

{

 

 // array is 1-indexed, with a[0] = 0

 // for the sake of simplicity

 double a[] = { 0, 7, 20, 49, 125 };

 

 int n = a.length;

 

 // Function to print the minimum operations

 // and the sequence of elements

 findMinimumOperations(a, n - 1);

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

# Python program to find minimum number

# of operations to convert a given

# sequence to an Geometric Progression

from sys import maxsize as INT_MAX

 

# Function to print the GP series

def construct(n: int, ans_pair: tuple):

 

 # Check for possibility

 if ans_pair[0] == -1:

 print("Not possible")

 return

 

 a1 = ans_pair[0]

 a2 = ans_pair[1]

 r = a2 / a1

 

 print("The resultant sequence is")

 for i in range(1, n + 1):

 ai = a1 * pow(r, i - 1)

 print(int(ai), end=" ")

 

# Function for getting the Arithmetic Progression

def findMinimumOperations(a: list, n: int):

 ans = INT_MAX

 

 # The array c describes all the given set of

 # possible operations.

 c = [-1, 0, 1]

 

 # Size of c

 possibilities = 3

 

 # candidate answer

 pos1 = -1

 pos2 = -1

 

 # loop through all the permutations of the first two

 # elements.

 for i in range(possibilities):

 for j in range(possibilities):

 

 # a1 and a2 are the candidate first two elements

 # of the possible GP.

 a1 = a[1] + c[i]

 a2 = a[2] + c[j]

 

 # temp stores the current answer, including the

 # modification of the first two elements.

 temp = abs(a1 - a[1]) + abs(a2 - a[2])

 

 if a1 == 0 or a2 == 0:

 continue

 

 # common ratio of the possible GP

 r = a2 / a1

 

 # To check if the chosen set is valid, and id yes

 # find the number of operations it takes.

 for pos in range(3, n + 1):

 

 # ai is value of a[i] according to the assumed

 # first two elements a1, a2

 # ith element of an GP = a1*((a2-a1)^(i-1))

 ai = a1 * pow(r, pos - 1)

 

 # Check for the "proposed" element to be only

 # differing by one

 if a[pos] == ai:

 continue

 elif a[pos] + 1 == ai or a[pos] - 1 == ai:

 temp += 1

 else:

 temp = INT_MAX # set the temporary ans

 break # to infinity and break

 

 # update answer

 if temp < ans:

 ans = temp

 pos1 = a1

 pos2 = a2

 if ans == -1:

 print("-1")

 return

 

 print("Minimum number of Operations are", ans)

 ans_pair = (pos1, pos2)

 

 # Calling function to print the sequence

 construct(n, ans_pair)

 

# Driver Code

if __name__ == "__main__":

 

 # array is 1-indexed, with a[0] = 0

 # for the sake of simplicity

 a = [0, 7, 20, 49, 125]

 n = len(a)

 

 # Function to print the minimum operations

 # and the sequence of elements

 findMinimumOperations(a, n - 1)

 

# This code is contributed by

# sanjeev2552  
  
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

// C# program to find minimum number

// of operations to convert a given

// sequence to an Geometric Progression

using System;

 

class GFG

{

 

class pair

{ 

 public double first, second; 

 public pair(double first, double second) 

 { 

 this.first = first; 

 this.second = second; 

 } 

} 

 

// Function to print the GP series

static void construct(int n, pair ans_pair)

{

 // Check for possibility

 if (ans_pair.first == -1)

 {

 Console.Write("Not possible");

 return;

 }

 double a1 = ans_pair.first;

 double a2 = ans_pair.second;

 double r = a2 / a1;

 

 Console.Write("The resultant sequence is:\n");

 for (int i = 1; i <= n; i++)

 {

 int ai = (int) (a1 * Math.Pow(r, i - 1));

 Console.Write(ai + " ");

 }

}

 

// Function for getting the Arithmetic Progression

static void findMinimumOperations(double []a, int n)

{

 int ans = int.MaxValue;

 

 // The array c describes all the given set of

 // possible operations.

 int []c = { -1, 0, 1 };

 

 // Size of c

 int possiblities = 3;

 

 // candidate answer

 int pos1 = -1, pos2 = -1;

 

 // loop through all the permutations of the first two

 // elements.

 for (int i = 0; i < possiblities; i++) 

 {

 for (int j = 0; j < possiblities; j++) 

 {

 

 // a1 and a2 are the candidate first two elements

 // of the possible GP.

 double a1 = a[1] + c[i];

 double a2 = a[2] + c[j];

 

 // temp stores the current answer, including the

 // modification of the first two elements.

 int temp = (int) (Math.Abs(a1 - a[1]) + Math.Abs(a2 - a[2]));

 

 if (a1 == 0 || a2 == 0)

 continue;

 

 // common ratio of the possible GP

 double r = a2 / a1;

 

 // To check if the chosen set is valid, and id yes

 // find the number of operations it takes.

 for (int pos = 3; pos <= n; pos++)

 {

 

 // ai is value of a[i] according to the assumed

 // first two elements a1, a2

 // ith element of an GP = a1*((a2-a1)^(i-1))

 double ai = a1 * Math.Pow(r, pos - 1);

 

 // Check for the "proposed" element to be only

 // differing by one

 if (a[pos] == ai)

 {

 continue;

 }

 else if (a[pos] + 1 == ai || a[pos] - 1 == ai)

 {

 temp++;

 }

 else

 {

 temp = int.MaxValue; // set the temporary ans

 break; // to infinity and break

 }

 }

 

 // update answer

 if (temp < ans) 

 {

 ans = temp;

 pos1 = (int) a1;

 pos2 = (int) a2;

 }

 }

 }

 if (ans == -1) 

 {

 Console.Write("-1");

 return;

 }

 

 Console.Write("Minimum Number of Operations are " + ans+ "\n");

 pair ans_pair = new pair( pos1, pos2 );

 

 // Calling function to print the sequence

 construct(n, ans_pair);

}

 

// Driver Code

public static void Main(String[] args)

{

 

 // array is 1-indexed, with a[0] = 0

 // for the sake of simplicity

 double []a = { 0, 7, 20, 49, 125 };

 

 int n = a.Length;

 

 // Function to print the minimum operations

 // and the sequence of elements

 findMinimumOperations(a, n - 1);

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    Minimum Number of Operations are 2
    The resultant sequence is:
    8 20 50 125
    

**Time Complexity** : O(9*N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

