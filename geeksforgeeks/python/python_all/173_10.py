Check if the given push and pop sequences of Stack is valid or not



Given push[] and pop[] sequences with distinct values. The task is to check if
this could have been the result of a sequence of push and pop operations on an
initially empty stack. Return “True” if it otherwise returns “False”.

 **Examples:**

    
    
    **Input:** pushed = { 1, 2, 3, 4, 5 }, popped = { 4, 5, 3, 2, 1 }
    **Output:** True
    Following sequence can be performed:
    push(1), push(2), push(3), push(4), pop() -> 4,
    push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
    
    **Input:** pushed = { 1, 2, 3, 4, 5 }, popped = { 4, 3, 5, 1, 2 }
    **Output:** False
    1 can't be popped before 2.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** If the element X has been pushed to the stack then check if the
top element in the pop[] sequence is X or not. If it is X then pop it right
now else top of the push[] sequence will be changed and make the sequences
invalid. So, similarly do the same for all the elements and check if the stack
is empty or not in the last. If empty then print **True** else print
**False**.

 **Below is the implementation of above approach:**

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of above approach

#include <iostream>

#include <stack>

 

using namespace std;

 

// Function to check validity of stack sequence

bool validateStackSequence(int pushed[], int popped[], int
len){

 

 // maintain count of popped elements

 int j = 0;

 

 // an empty stack

 stack <int> st;

 for(int i = 0; i < len; i++){

 st.push(pushed[i]);

 

 // check if appended value is next to be popped out

 while (!st.empty() && j < len && st.top() == popped[j]){

 st.pop();

 j++;

 }

 }

 

 return j == len;

}

 

// Driver code

int main()

{

 int pushed[] = {1, 2, 3, 4, 5};

 int popped[] = {4, 5, 3, 2, 1};

 int len = sizeof(pushed)/sizeof(pushed[0]);

 

 cout << (validateStackSequence(pushed, popped, len) ? "True" :
"False");

 

 return 0;

}

 

// This code is contributed by Rituraj Jain  
  
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

// Java program for above implementation

import java.util.*;

 

class GfG 

{

 

 // Function to check validity of stack sequence 

 static boolean validateStackSequence(int pushed[],

 int popped[], int len) 

 {

 

 // maintain count of popped elements 

 int j = 0;

 

 // an empty stack 

 Stack<Integer> st = new Stack<>();

 for (int i = 0; i < len; i++) 

 {

 st.push(pushed[i]);

 

 // check if appended value 

 // is next to be popped out 

 while (!st.empty() && j < len && 

 st.peek() == popped[j]) 

 {

 st.pop();

 j++;

 }

 }

 

 return j == len;

 }

 

 // Driver code 

 public static void main(String[] args) 

 {

 int pushed[] = {1, 2, 3, 4, 5};

 int popped[] = {4, 5, 3, 2, 1};

 int len = pushed.length;

 

 System.out.println((validateStackSequence(pushed, popped, len) ? "True"
: "False"));

 }

}

 

/* This code contributed by PrinciRaj1992 */  
  
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

# Function to check validity of stack sequence

def validateStackSequence(pushed, popped):

 # maintain count of popped elements

 j = 0

 

 # an empty stack

 stack = []

 

 for x in pushed:

 stack.append(x)

 

 # check if appended value is next to be popped out

 while stack and j < len(popped) and stack[-1] ==
popped[j]:

 stack.pop()

 j = j + 1

 

 return j == len(popped)

 

 

# Driver code

pushed = [1, 2, 3, 4, 5]

popped = [4, 5, 3, 2, 1]

print(validateStackSequence(pushed, popped))  
  
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

// C# program for above implementation

using System; 

using System.Collections.Generic; 

 

class GfG 

{

 

 // Function to check validity of stack sequence 

 static bool validateStackSequence(int []pushed,

 int []popped, int len) 

 {

 

 // maintain count of popped elements 

 int j = 0;

 

 // an empty stack 

 Stack<int> st = new Stack<int>();

 for (int i = 0; i < len; i++) 

 {

 st.Push(pushed[i]);

 

 // check if appended value 

 // is next to be popped out 

 while (st.Count != 0 && j < len && 

 st.Peek() == popped[j]) 

 {

 st.Pop();

 j++;

 }

 }

 

 return j == len;

 }

 

 // Driver code 

 public static void Main(String[] args) 

 {

 int []pushed = {1, 2, 3, 4, 5};

 int []popped = {4, 5, 3, 2, 1};

 int len = pushed.Length;

 

 Console.WriteLine((validateStackSequence(pushed, 

 popped, len) ? "True" : "False"));

 }

}

 

// This code contributed by Rajput-Ji  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP implementation of above approach

 

// Function to check validity of stack sequence

function validateStackSequence($pushed, $popped, $len)

{

 

 // maintain count of popped elements

 $j = 0;

 

 // an empty stack

 $st = array();

 for($i = 0; $i < $len; $i++)

 {

 array_push($st, $pushed[$i]);

 

 // check if appended value is next

 // to be popped out

 while (!empty($st) && $j < $len && 

 $st[count($st) - 1] == $popped[$j])

 {

 array_pop($st);

 $j++;

 }

 }

 

 return $j == $len;

}

 

// Driver code

$pushed = array(1, 2, 3, 4, 5);

$popped = array(4, 5, 3, 2, 1);

$len = count($pushed);

 

echo (validateStackSequence($pushed, 

 $popped, $len) ? "True" : "False");

 

// This code is contributed by mits

?>  
  
---  
  
 __

 __

 **Output:**

    
    
    True
    

**Time Complexity:** O(N), where N is size of stack.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

