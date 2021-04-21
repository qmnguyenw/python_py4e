Minimum steps in which N can be obtained using addition or subtraction at
every step



Given N, print the sequence of a minimum number of steps in which N can be
obtained starting from 0 using addition or subtraction of the step number.

 **Note** : At each step we can add or subtract a number equal to the step
number from the current position. For example, at step 1 we can add 1 or -1.
Similarily at step 2 we add 2 or -2 and so on.

Below diagram shows all possible positions that can be reached from 0 in 3
steps by performing the specified operations.

![](https://media.geeksforgeeks.org/wp-content/uploads/Screen-
Shot-2018-06-27-at-12.06.16-PM.png)

 **Examples :**

  

  

    
    
    Input: n = -4
    Output: Minimum number of Steps: 3
            Step sequence: 1 -2 -3
    **Explanation** : 
    Step 1: At step 1 we add 1 to move from 0 to 1.
    Step 2: At step 2 we add (-2) to move from 1 to -1.
    Step 3: At step 3 we add (-3) to move from -1 to -4.
    
    Input: n = 11
    Output: Minimum number of steps = 4 
            Step sequence: 1 -2 3 4 5 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** The approach to solve the above problem is to mark the step
numbers where we have to subtract or add where if N is positive or negative
respectively. If N is positive, add numbers at every step, until the sum
exceeds N. Once the sum exceeds N, check if sum-N is even or not. If sum-N is
even, then at step number (sum-N)/2, subtraction is to be done. If sum-N is an
odd number, then check if the last step at which sum exceeded N was even or
odd. If it was odd, perform one more step else perform two steps. If sum = N
at any step, then additin or subtraction at every step will give the answer.

Let N = 11, then 1+2+3+4+5=15 exceeds 11. Subtract 15-11 to get 4, which is
equivalent to performing subtraction at step 2. Hence the sequence of steps is
1 -2 3 4 5

Let N=12, then 1+2+3+4+5=15 exceeds 11. Subtract 15-12 to get 3, which cannot
be performed at any step. So add two more steps, one is the 6th step and 7th
step. The target is to make sum-N even, so perform addition at 6th step and
subtraction at 7th step, which combines to subtract 1 from the sum. Now sum-N
is even, 14-12=2 which is equivalent to performing subtraction at step 1.
Hence the sequence of steps are -1 2 3 4 5 6 -7

Let N=20, then 1+2+3+4+5+6 exceeds 20. Subtract 21-20 to get 1, so add 7 to 21
to get 28. Performing addition at next step will do as (sum-n) is odd. sum-N
gives 8 which is equivalent to performing subtraction at step 4. Hence the
sequence of steps is 1 2 3 -4 5 6 7.

Below is the illustration of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print the sequence

// of minimum steps in which N can be

// obtained from 0 using addition or

// subtraction of the step number.

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the vector

// which stores the step sequence

vector<int> findSteps(int n)

{

 // Steps sequence

 vector<int> ans;

 

 // Current sum

 int sum = 0;

 

 // Sign of the number

 int sign = (n >= 0 ? 1 : -1);

 n = abs(n);

 

 int i;

 // Basic steps required to get sum >= required value.

 for (i = 1; sum < n; i++) {

 ans.push_back(sign * i);

 sum += i;

 }

 cout << i << endl;

 

 // Reached ahead of N

 if (sum > sign * n) {

 

 // If the last step was an odd number

 if (i % 2) {

 sum -= n;

 

 // sum-n is odd

 if (sum % 2) {

 ans.push_back(sign * i);

 sum += i++;

 }

 // subtract the equivalent sum-n

 ans[(sum / 2) - 1] *= -1;

 }

 else {

 sum -= n;

 

 // sum-n is odd

 if (sum % 2) {

 

 // since addition of next step and subtraction

 // at the next next step will give sum = sum-1

 sum--;

 ans.push_back(sign * i);

 ans.push_back(sign * -1 * (i + 1));

 }

 // subtract the equivalent sum-n

 ans[(sum / 2) - 1] *= -1;

 }

 }

 // returns the vector

 return ans;

}

 

// Function to print the steps

void printSteps(int n)

{

 vector<int> v = findSteps(n);

 

 // prints the number of steps which is the size of vector

 cout << "Minimum number of Steps: " << v.size() << "\n";

 

 cout << "Step sequence:";

 

 // prints the steps stored

 // in the vector

 for (int i = 0; i < v.size(); i++)

 cout << v[i] << " ";

}

 

// Driver Code

int main()

{

 int n = 20;

 printSteps(n);

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

// Java program to print the

// sequence of minimum steps 

// in which N can be obtained 

// from 0 using addition or 

// subtraction of the step 

// number.

import java.util.*;

 

class GFG

{

 

// Function to return the

// Arraylist which stores 

// the step sequence

static ArrayList<Integer> findSteps(int n)

{

 // Steps sequence

 ArrayList<Integer> ans = new ArrayList<Integer>();

 

 // Current sum

 int sum = 0;

 

 // Sign of the number

 int sign = (n >= 0 ? 1 : -1);

 n = Math.abs(n);

 

 int i;

 // Basic steps required to

 // get sum >= required value.

 for (i = 1; sum < n; i++) 

 {

 ans.add(sign * i);

 sum += i;

 }

 System.out.println( i );

 

 // Reached ahead of N

 if (sum > sign * n) 

 {

 

 // If the last step 

 // was an odd number

 if (i % 2 != 0) 

 {

 sum -= n;

 

 // sum-n is odd

 if (sum % 2 != 0) 

 {

 ans.add(sign * i);

 sum += i++;

 }

 

 // subtract the 

 // equivalent sum-n

 ans.set((sum / 2) - 1, 

 ans.get((sum / 2) - 1) * -1);

 }

 else

 {

 sum -= n;

 

 // sum-n is odd

 if (sum % 2 != 0) 

 {

 

 // since addition of next 

 // step and subtraction at

 // the next next step will

 // give sum = sum-1

 sum--;

 ans.add(sign * i);

 ans.add(sign * -1 * (i + 1));

 }

 

 // subtract the 

 // equivalent sum-n

 ans.set((sum / 2) - 1,

 ans.get((sum / 2) - 1) * -1);

 }

 }

 

 // returns the Arraylist

 return ans;

}

 

// Function to print the steps

static void printSteps(int n)

{

 ArrayList<Integer> v = findSteps(n);

 

 // prints the number of steps 

 // which is the size of Arraylist

 System.out.println("Minimum number " + 

 "of Steps: " + 

 v.size());

 

 System.out.print("Step sequence:");

 

 // prints the steps stored

 // in the Arraylist

 for (int i = 0; i < v.size(); i++)

 System.out.print(v.get(i) + " ");

}

 

// Driver Code

public static void main(String args[])

{

 int n = 20;

 printSteps(n);

}

}

// This code is contributed

// by Arnab Kundu  
  
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

// C# program to print the

// sequence of minimum steps 

// in which N can be obtained 

// from 0 using addition or 

// subtraction of the step 

// number.

using System;

using System.Collections.Generic;

 

class GFG

{

 

// Function to return the

// Arraylist which stores 

// the step sequence

static List<int> findSteps(int n)

{

 // Steps sequence

 List<int> ans = new List<int>();

 

 // Current sum

 int sum = 0;

 

 // Sign of the number

 int sign = (n >= 0 ? 1 : -1);

 n = Math.Abs(n);

 

 int i;

 

 // Basic steps required to

 // get sum >= required value.

 for (i = 1; sum < n; i++) 

 {

 ans.Add(sign * i);

 sum += i;

 }

 Console.WriteLine( i );

 

 // Reached ahead of N

 if (sum > sign * n) 

 {

 

 // If the last step 

 // was an odd number

 if (i % 2 != 0) 

 {

 sum -= n;

 

 // sum-n is odd

 if (sum % 2 != 0) 

 {

 ans.Add(sign * i);

 sum += i++;

 }

 

 // subtract the 

 // equivalent sum-n

 ans[(sum / 2) - 1]= 

 ans[(sum / 2) - 1] * -1;

 }

 else

 {

 sum -= n;

 

 // sum-n is odd

 if (sum % 2 != 0) 

 {

 

 // since addition of next 

 // step and subtraction at

 // the next next step will

 // give sum = sum-1

 sum--;

 ans.Add(sign * i);

 ans.Add(sign * -1 * (i + 1));

 }

 

 // subtract the 

 // equivalent sum-n

 ans[(sum / 2) - 1]=

 ans[(sum / 2) - 1] * -1;

 }

 }

 

 // returns the Arraylist

 return ans;

}

 

// Function to print the steps

static void printSteps(int n)

{

 List<int> v = findSteps(n);

 

 // prints the number of steps 

 // which is the size of Arraylist

 Console.WriteLine("Minimum number " + 

 "of Steps: " + 

 v.Count);

 

 Console.Write("Step sequence:");

 

 // prints the steps stored

 // in the Arraylist

 for (int i = 0; i < v.Count; i++)

 Console.Write(v[i] + " ");

}

 

// Driver Code

public static void Main(String []args)

{

 int n = 20;

 printSteps(n);

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output :**

    
    
    7
    Minimum number of Steps: 7
    Step sequence:1 2 3 -4 5 6 7
    

**Time Complexity :** O(sqrt(N))  
 **Auxiliary Space :** O(sqrt(N))

 **Note:** sum = i*(i+1)/2 is equivalent or greater than N, which gives i as
sqrt(N).

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

