Count the number of pop operations on stack to get each element of the array



 **Prerequisite:** Stack, Hashing

Given a stack of N numbers and an array of numbers. Count the numbers of pop
operations required to get each element of the array. Once an element is
popped then its not pushed back again. Assume that the all the elements from
the array present inside the stack initially.

 **Examples:**

> Input: N = 5  
> Stack: 6 4 3 2 1  
> Array: 6 3 4 1 2  
> Output: 1 2 0 2 0
>
> The 1st element of the stack is the same as the array elements. So to get 6,
> one pop is required i.e. pop 6 from the stack. To get 3, 2 elements will be
> popped i.e. 4 and 3. To get 4, 4 was already popped, thus we won’t pop more
> elements. Similarly, to get 1, we will pop 2 elements and for the 2, no pop
> count will be added.
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** This question can be solved easily by using a stack. We will
keep popping the elements till we find the element we are searching. The only
hurdle is that how to handle the case when the element is already popped and
is not present in the stack. For that, we will maintain a hash map. As we pop
an element from the stack we will insert that element in the hash map so that
if the element comes later in the array we will first check if its present
inside the hash maps or in other words has been popped out from the stack
previously. Otherwise, we will know it’s present inside the stack and we will
start popping the elements till we find the required number.

Below is the implementation of above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to implement above approach

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the count

void countEle(stack<int>& s, int a[], int N)

{

 // Hashmap to store all the elements

 // which are popped once.

 unordered_map<int, bool> mp;

 for (int i = 0; i < N; ++i) {

 int num = a[i];

 

 // Check if the number is present

 // in the hashmap Or in other words

 // been popped out from the stack before.

 if (mp.find(num) != mp.end())

 cout << "0 ";

 

 else {

 int cnt = 0;

 

 // Keep popping the elements

 // while top is not equal to num

 while (s.top() != num) {

 mp[s.top()] = true;

 s.pop();

 cnt++;

 }

 // Pop the top ie. equal to num

 s.pop();

 cnt++;

 

 // Print the number of elements popped.

 cout << cnt << " ";

 }

 }

}

 

// Driver code

int main()

{

 int N = 5;

 

 stack<int> s;

 s.push(1);

 s.push(2);

 s.push(3);

 s.push(4);

 s.push(6);

 

 int a[] = { 6, 3, 4, 1, 2 };

 countEle(s, a, N);

 

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

// Java program to implement above approach

import java.util.HashMap;

import java.util.Stack;

 

class GFG 

{

 

 // Function to find the count

 public static void countEle(Stack<Integer> s, 

 int[] a, int N) 

 {

 

 // Hashmap to store all the elements

 // which are popped once.

 HashMap<Integer, 

 Boolean> mp = new HashMap<>();

 for (int i = 0; i < N; ++i)

 {

 int num = a[i];

 

 // Check if the number is present

 // in the hashmap Or in other words

 // been popped out from the stack before.

 if (mp.containsKey(num))

 System.out.print("0 ");

 else

 {

 int cnt = 0;

 

 // Keep popping the elements

 // while top is not equal to num

 while (s.peek() != num) 

 {

 mp.put(s.peek(), true);

 s.pop();

 cnt++;

 }

 

 // Pop the top ie. equal to num

 s.pop();

 cnt++;

 

 // Print the number of elements popped.

 System.out.print(cnt + " ");

 }

 }

 }

 

 // Driver code

 public static void main(String[] args) 

 {

 int N = 5;

 

 Stack<Integer> s = new Stack<>();

 s.add(1);

 s.add(2);

 s.add(3);

 s.add(4);

 s.add(6);

 

 int[] a = { 6, 3, 4, 1, 2 };

 countEle(s, a, N);

 }

}

 

// This code is contributed by

// sanjeev2552  
  
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

# Python3 program to implement above approach

 

# Function to find the count 

def countEle(s, a, N): 

 

 # Hashmap to store all the elements 

 # which are popped once. 

 mp = {} 

 for i in range(0, N): 

 num = a[i] 

 

 # Check if the number is present 

 # in the hashmap Or in other words 

 # been popped out from the stack before. 

 if num in mp: 

 print("0", end = " ") 

 

 else:

 cnt = 0

 

 # Keep popping the elements 

 # while top is not equal to num 

 while s[-1] != num:

 mp[s.pop()] = True

 cnt += 1

 

 # Pop the top ie. equal to num 

 s.pop()

 cnt += 1

 

 # Print the number of elements popped. 

 print(cnt, end = " ") 

 

# Driver code 

if __name__ == "__main__":

 

 N = 5

 s = [] 

 s.append(1) 

 s.append(2) 

 s.append(3) 

 s.append(4) 

 s.append(6) 

 

 a = [6, 3, 4, 1, 2] 

 countEle(s, a, N) 

 

# This code is contributed by Rituraj Jain  
  
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

// C# implementation of the above approach:

using System;

using System.Collections.Generic;

 

class GFG 

{

 

 // Function to find the count

 public static void countEle(Stack<int> s, 

 int[] a, int N) 

 {

 

 // Hashmap to store all the elements

 // which are popped once.

 Dictionary<int,

 bool> mp = new Dictionary<int,

 bool>();

 for (int i = 0; i < N; ++i)

 {

 int num = a[i];

 

 // Check if the number is present

 // in the hashmap Or in other words

 // been popped out from the stack before.

 if (mp.ContainsKey(num))

 Console.Write("0 ");

 else

 {

 int cnt = 0;

 

 // Keep popping the elements

 // while top is not equal to num

 while (s.Peek() != num) 

 {

 mp.Add(s.Peek(), true);

 s.Pop();

 cnt++;

 }

 

 // Pop the top ie. equal to num

 s.Pop();

 cnt++;

 

 // Print the number of elements popped.

 Console.Write(cnt + " ");

 }

 }

 }

 

 // Driver code

 public static void Main(String[] args) 

 {

 int N = 5;

 

 Stack<int> s = new Stack<int>();

 s.Push(1);

 s.Push(2);

 s.Push(3);

 s.Push(4);

 s.Push(6);

 

 int[] a = { 6, 3, 4, 1, 2 };

 countEle(s, a, N);

 }

}

 

// This code is contributed by PrinciRaj1992   
  
---  
  
__

__

**Output:**

    
    
    1 2 0 2 0
    

**Time Complexity:** O(N)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

