Majority Element | Set-2 (Hashing)



Given an array of size N, find the majority element. The majority element is
the element that appears more than
![\\floor{\\frac{n}{2}}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-b604f584ee3691c14a7c78f6dd07db70_l3.png) times in the
given array.

 **Examples:**

    
    
    Input: [3, 2, 3]
    Output: 3
    
    Input: [2, 2, 1, 1, 1, 2, 2]
    Output: 2
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

The problem has been solved using 4 different methods in the previous post. In
this post hashing based solution is implemented. We count occurrences of all
elements. And if count of any element becomes more than n/2, we return it.

Hence if there is a majority-element, it will be the value of the key.

Below is the implementation of the above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

 

#define ll long long int

 

// function to print the majority Number

int majorityNumber(int arr[], int n)

{

 int ans = -1;

 unordered_map<int, int>freq;

 for (int i = 0; i < n; i++)

 {

 freq[arr[i]]++;

 if (freq[arr[i]] > n / 2)

 ans = arr[i];

 }

 return ans;

} 

 

// Driver code

int main()

{

 int a[] = {2, 2, 1, 1, 1, 2, 2};

 int n = sizeof(a) / sizeof(int);

 cout << majorityNumber(a, n); 

 return 0;

}

 

// This code is contributed 

// by sahishelangia  
  
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

import java.util.*;

 

class GFG 

{

 

// function to print the majority Number

static int majorityNumber(int arr[], int n)

{

 int ans = -1;

 HashMap<Integer,

 Integer> freq = new HashMap<Integer,

 Integer>();

 

 for (int i = 0; i < n; i++)

 {

 if(freq.containsKey(arr[i]))

 {

 freq.put(arr[i], freq.get(arr[i]) + 1);

 }

 else

 {

 freq.put(arr[i], 1);

 }

 if (freq.get(arr[i]) > n / 2)

 ans = arr[i];

 }

 return ans;

} 

 

// Driver code

public static void main(String[] args) 

{

 int a[] = {2, 2, 1, 1, 1, 2, 2};

 int n = a.length;

 System.out.println(majorityNumber(a, n));

}

} 

 

// This code is contributed by Princi Singh  
  
---  
  
 __

 __

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# function to print the

# majorityNumber

def majorityNumber(nums):

 

 # stores the num count 

 num_count = {}

 

 # iterate in the array 

 for num in nums:

 

 if num in num_count:

 num_count[num] += 1

 else:

 num_count[num] = 1

 

 for num in num_count:

 if num_count[num] > len(nums)/2:

 return num

 return -1

 

# Driver Code

a = [2, 2, 1, 1, 1, 2, 2]

print majorityNumber(a)  
  
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

 

// function to print the majority Number

static int majorityNumber(int []arr, int n)

{

 int ans = -1;

 Dictionary<int,

 int> freq = new Dictionary<int,

 int>();

 

 for (int i = 0; i < n; i++)

 {

 if(freq.ContainsKey(arr[i]))

 {

 freq[arr[i]] = freq[arr[i]] + 1;

 }

 else

 {

 freq.Add(arr[i], 1);

 }

 if (freq[arr[i]] > n / 2)

 ans = arr[i];

 }

 return ans;

} 

 

// Driver code

public static void Main(String[] args) 

{

 int []a = {2, 2, 1, 1, 1, 2, 2};

 int n = a.Length;

 Console.WriteLine(majorityNumber(a, n));

}

}

 

// This code is contributed by Rajput-Ji  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Below is the time and space complexity of the above algorithm:-

 **Time Complexity** : O(n)  
 **Auxiliary Space** : O(n)

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

