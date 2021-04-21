Program to print N minimum elements from list of integers



Given a list of integers, the task is to generate another list with N minimum
elements.

 **Examples:**

    
    
    Input: {23, 1, 6, 2, 90}
    Output: {1, 2}
    
    Input: {34, 21, 56, 42, 89, 90, -1}
    Output: {-1, 21}

 **Approach:** The idea is to use the concept used in Find the smallest and
second smallest elements in an array.

  * First, find the smallest number in the given list.
  * Then add that current minimum element to another list that will contain the N minimum elements.
  * Remove the current minimum element from the given list.
  * Continue with the same process until the N minimum elements are found.

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find N

// minimum elements

#include <bits/stdc++.h>

using namespace std;

void Nminelements(vector<int>list1, int N)

{

 vector<int> final_list;

 int n = list1.size();

 for (int i = 0; i < N; i++)

 {

 int min1 = 9999999;

 for (int j = 0; j < n; j++)

 {

 if (list1[j] < min1)

 min1 = list1[j];

 }

 

 // remove minimum element

 // from list so that it do

 // not come in calculation again 

 list1.erase(remove(list1.begin(),

 list1.end(), min1),

 list1.end());

 final_list.push_back(min1);

 }

 for(int i = 0; i < final_list.size(); i++)

 cout << final_list[i] << " ";

}

// Driver code

int main()

{

 vector<int> list1 = {4, 78, 34, 10,

 8, 21, 11, 231};

 int N = 2;

 Nminelements(list1, N);

}

// This code is contributed by Subhadeep  
  
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

// Java program to find N

// minimum elements

import java.io.*;

import java.util.*;

class GFG{

 

static void Nminelements(ArrayList<Integer> list1, int N)

{

 ArrayList<Integer> final_list = new ArrayList<Integer>();

 

 for(int i = 0; i < N; i++)

 {

 int min1 = 9999999;

 int index = 0;

 for(int j = 0; j < list1.size(); j++)

 {

 if ((int)list1.get(j) < min1)

 { min1 = (int)list1.get(j);

 index = j;

 }

 }

 

 // Remove minimum element

 // from list so that it do

 // not come in calculation again

 list1.remove(index);

 final_list.add(min1);

 }

 for(int i = 0; i < final_list.size(); i++)

 System.out.print(final_list.get(i) + " ");

}

 

// Driver code

public static void main (String[] args)

{

 ArrayList<Integer> list1 = new ArrayList<Integer>(

 Arrays.asList(4, 78, 34, 10, 8, 21, 11, 231
));

 int N = 2;

 

 Nminelements(list1, N);

}

}

// This code is contributed by avanitrachhadiya2155  
  
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

# Python3 program to find N minimum elements

def Nminelements(list1, N):

 final_list =[];

 

 for i in range(0, N): 

 min1 = 9999999;

 

 for j in range(len(list1)): 

 if list1[j]<min1:

 min1 = list1[j];

 # remove minimum element from list so

 # that it do not come in calculation again 

 list1.remove(min1);

 final_list.append(min1)

 

 print(final_list)

 

# Driver code

list1 = [4, 78, 34, 10, 8, 21, 11, 231];

N = 2;

Nminelements(list1, N)  
  
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

// C# program to find N

// minimum elements

using System;

using System.Collections;

class GFG{

static void Nminelements(ArrayList list1, int N)

{

 ArrayList final_list = new ArrayList();

 for(int i = 0; i < N; i++)

 {

 int min1 = 9999999;

 for(int j = 0; j < list1.Count; j++)

 {

 if ((int)list1[j] < min1)

 min1 = (int)list1[j];

 }

 

 // Remove minimum element

 // from list so that it do

 // not come in calculation again

 list1.Remove(min1);

 final_list.Add(min1);

 }

 for(int i = 0; i < final_list.Count; i++)

 Console.Write(final_list[i] + " ");

}

// Driver code

public static void Main()

{

 ArrayList list1 = new ArrayList(){ 4, 78, 34, 10,

 8, 21, 11, 231 };

 int N = 2;

 

 Nminelements(list1, N);

}

}

// This code is contributed by chitranayal  
  
---  
  
 __

 __

 **Output:**

    
    
    4 8

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

