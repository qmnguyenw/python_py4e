Find the sum of remaining sticks after each iterations



Given **N** number of sticks of varying lengths in an array **arr** , the task
is to determine the sum of the count of sticks that are left after each
iteration. At each iteration, cut the length of the shortest stick from
remaining sticks.  
 **Examples:**

    
    
    **Input:** N = 6, arr = {5, 4, 4, 2, 2, 8}
    **Output:** 7
    **Explanation:**
    Iteration 1: 
    Initial arr = {5, 4, 4, 2, 2, 8}
    Shortest stick = 2
    arr with reduced length = {3, 2, 2, 0, 0, 6}
    Remaining sticks = 4
    
    Iteration 2: 
    arr = {3, 2, 2, 4}
    Shortest stick = 2
    Left stick = 2
    
    Iteration 3: 
    arr = {1, 2}
    Shortest stick = 1
    Left stick = 1
    
    Iteration 4: 
    arr = {1}
    Min length = 1
    Left stick = 0
    
    **Input:** N = 8, arr = {1, 2, 3, 4, 3, 3, 2, 1}
    **Output:** 11

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** Approach to solve this problem is to sort the array and then
find number of minimum length sticks that are of same length while traversing
and update the sum accordingly at each step and in the end return the sum.

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the sum of

// remaining sticks after each iterations

#include <bits/stdc++.h>

using namespace std;

// Function to calculate

// sum of remaining sticks

// after each iteration

int sum(vector<int> &arr;, int n)

{

 int sum = 0;

 sort(arr.begin(),arr.end());

 int prev=0,count=1,s=arr.size();

 int i=1;

 while(i<arr.size()){

 if(arr[i]==arr[prev]){

 count++;

 }else{

 prev=i;

 sum+=s-count;

 s-=count;

 count=1;

 }

 i++;

 }

 return sum;

}

// Driver code

int main()

{

 int n = 6;

 vector<int> ar{ 5, 4, 4, 2, 2, 8 };

 int ans = sum(ar, n);

 cout << ans << '\n';

 return 0;

}  
  
---  
  
 __

 __

 ** _Time Complexity_ :** **O(Nlog(N))** where N is the number of sticks.

 ** _Another Approach:_**  

  * Store the frequency of stick lengths in a map
  * In each iteration, 
    * Find the frequency of min length’s stick
    * Decrease the frequency of min length’s stick from each stick’s frequency
    * Add the count of non-zero sticks to the resultant stick.   

Below is the implementation of above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find the sum of

// remaining sticks after each iterations

#include <bits/stdc++.h>

using namespace std;

// Function to calculate

// sum of remaining sticks

// after each iteration

int sum(int ar[], int n)

{

 map<int, int> mp;

 // storing frequency of stick length

 for (int i = 0; i < n; i++) {

 mp[ar[i]]++;

 }

 int sum = 0;

 for (auto p : mp) {

 n -= p.second;

 sum += n;

 }

 return sum;

}

// Driver code

int main()

{

 int n = 6;

 int ar[] = { 5, 4, 4, 2, 2, 8 };

 int ans = sum(ar, n);

 cout << ans << '\n';

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

// Java program to find the sum of

// remaining sticks after each iterations

import java.util.HashMap;

import java.util.Map;

class GFG

{

 

 // Function to calculate

 // sum of remaining sticks

 // after each iteration

 static int sum(int ar[], int n)

 {

 HashMap<Integer,

 Integer> mp = new HashMap<>();

 

 for (int i = 0; i < n; i++)

 {

 mp.put(ar[i], 0);

 }

 

 // storing frequency of stick length

 for (int i = 0; i < n; i++)

 {

 mp.put(ar[i], mp.get(ar[i]) + 1) ;

 }

 

 int sum = 0;

 

 for(Map.Entry p : mp.entrySet())

 {

 n -= (int)p.getValue();

 sum += n;

 }

 return sum;

 }

 

 // Driver code

 public static void main (String[] args)

 {

 int n = 6;

 int ar[] = { 5, 4, 4, 2, 2, 8 };

 

 int ans = sum(ar, n);

 

 System.out.println(ans);

 

 }

}

// This code is contributed by kanugargng  
  
---  
  
 __

 __

## Python 3

 __

 __  
 __

 __

 __  
 __  
 __

# Python proagram to find sum

# of remaining sticks

# Function to calculate

# sum of remaining sticks

# after each iteration

def sum(ar, n):

 mp = dict()

 for i in ar:

 if i in mp:

 mp[i]+= 1

 else:

 mp[i] = 1

 

 mp = sorted(list(mp.items()))

 

 sum = 0

 

 for pair in mp:

 n-= pair[1]

 sum+= n

 return sum

# Driver code

def main():

 n = 6

 ar = [5, 4, 4, 2, 2, 8]

 ans = sum(ar, n)

 print(ans)

main()  
  
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

// C# program to find the sum of

// remaining sticks after each iterations

using System;

using System.Collections.Generic; 

class GFG

{

 

 // Function to calculate

 // sum of remaining sticks

 // after each iteration

 static int sum(int []ar, int n)

 {

 SortedDictionary<int,

 int> mp = new SortedDictionary<int,

 int>();

 // storing frequency of stick length

 for (int i = 0; i < n; i++)

 {

 if(!mp.ContainsKey(ar[i]))

 mp.Add(ar[i], 0);

 else

 mp[ar[i]] = 0;

 }

 

 // storing frequency of stick length

 for (int i = 0; i < n; i++)

 {

 if(!mp.ContainsKey(ar[i]))

 mp.Add(ar[i], 1);

 else

 mp[ar[i]] = ++mp[ar[i]];

 }

 

 int sum = 0;

 

 foreach(KeyValuePair<int, int> p in mp)

 {

 n -= p.Value;

 sum += n;

 }

 return sum;

 }

 

 // Driver code

 public static void Main (String[] args)

 {

 int n = 6;

 int []ar = { 5, 4, 4, 2, 2, 8 };

 

 int ans = sum(ar, n);

 

 Console.WriteLine(ans);

 }

}

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    7

**Time Complexity:**![O\(Nlog\(N\)\)  ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-07fcf46e959c031c5fb2c8999f7bbc92_l3.png) where
N is the number of sticks

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

