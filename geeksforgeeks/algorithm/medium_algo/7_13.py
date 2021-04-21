Rearrange numbers in an array such that no two adjacent numbers are same



Given an array of integers. The task is to rearrange elements of the array
such that no two adjacent elements in the array are same.

 **Examples:**

    
    
    **Input** : arr[] = {1, 1, 1, 2, 2, 2}
    **Output** : {2, 1, 2, 1, 2, 1}
    
    **Input** : arr[] = {1, 1, 1, 1, 2, 2, 3, 3}
    **Output** : {1, 3, 1, 3, 2, 1, 2, 1}

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

The idea is to put the highest frequency element first (a greedy approach). We
use a priority queue (Or Binary Max Heap) and put all elements and ordered by
their frequencies (highest frequency element at the root). We then one by one
take the highest frequency element from the heap and add it to result. After
we add, we decrease the frequency of the element and temporarily move this
element out of priority queue so that it is not picked next time.

We have to follow the step to solve this problem, they are:

  1. Build a Priority_queue or max_heap, pq that stores elements and their frequencies.   
…… Priority_queue or max_heap is built on the bases of the frequency of
elements.

  2. Create a temporary Key that will be used as the previously visited element (the previous element in the resultant array. Initialize it { num = -1, freq = -1 }
  3. While pq is not empty. 
    * Pop an element and add it to the result.
    * Decrease frequency of the popped element by ‘1’.
    * Push the previous element back into the priority_queue if it’s frequency > ‘0’.
    * Make the current element as the previous element for the next iteration.
  4. If the length of resultant string and original are not equal, print “not possible”. Else print result.

Below is the implementation of the above approach:

## C++14

 __

 __  
 __

 __

 __  
 __  
 __

// C++14 program to rearrange numbers in

// an Array such that no two numbers are

// adjacent

#include <bits/stdc++.h>

using namespace std;

// Function to rearrange numbers in array such

// that no two adjacent numbers are same

void rearrangeArray(int arr[], int N)

{

 

 // Store frequencies of all elements

 // of the array

 map<int, int>mp, visited;

 

 for(int i = 0; i < N; i++)

 {

 mp[arr[i]]++;

 }

 

 priority_queue<pair<int, int>>pq;

 

 // Adding high freq elements

 // in descending order

 for(int i = 0; i < N ; i++)

 {

 int val = arr[i];

 

 if (mp[val] > 0 and visited[val] != 1)

 {

 pq.push({mp[val], val});

 }

 visited[val] = 1;

 }

 

 // 'result[]' that will store resultant value

 vector<int>result(N);

 

 // Work as the previous visited element

 // initial previous element will be ( '-1' and

 // it's frequency wiint also be '-1' )

 pair<int, int>prev = { -1, -1 };

 int l = 0;

 

 // Traverse queue

 while (pq.size() != 0)

 {

 

 // Pop top element from queue and add it

 // to result

 pair<int,int>k = pq.top();

 pq.pop();

 result[l] = k.second;

 

 // If frequency of previous element is less

 // than zero that means it is useless, we

 // need not to push it

 if (prev.first > 0)

 {

 pq.push(prev);

 }

 

 // Make current element as the previous

 // decrease frequency by 'one'

 k.first--;

 prev = k;

 l++;

 }

 

 for(auto it : result)

 {

 if (it == 0)

 {

 

 // If found 0, No valid result

 // array possible

 cout << "Not valid Array" << endl;

 return;

 }

 }

 

 for(auto it : result)

 {

 cout << it << ", ";

 }

}

// Driver Code

int main()

{

 int A[] = { 1, 1, 1, 1, 2, 2, 3, 3 };

 

 // Size of the array

 int N = sizeof(A) / sizeof(A[0]);

 

 rearrangeArray(A, N);

}

// This code is contributed by koulick_sadhu  
  
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

// Java Program to rearrange numbers in an Array

// such that no two numbers are adjacent

import java.util.Comparator;

import java.util.PriorityQueue;

// Comparator class to sort in descending order

class KeyComparator implements Comparator<Key>

{

 // Overriding compare()method of Comparator

 public int compare(Key k1, Key k2)

 {

 if (k1.freq < k2.freq)

 return 1;

 else if (k1.freq > k2.freq)

 return -1;

 return 0;

 }

}

// Object of num and its freq

class Key

{

 int freq; // store frequency of character

 int num;

 Key(int freq, int num)

 {

 this.freq = freq;

 this.num = num;

 }

}

public class GFG

{

 // Function to rearrange numbers in array such

 // that no two adjacent numbers are same

 static void rearrangeArray(int[] arr)

 {

 int n = arr.length;

 // Store frequencies of all elements

 // of the array

 int[] count = new int[10000];

 int visited[] = new int[10000];

 for (int i = 0; i < n; i++)

 count[arr[i]]++;

 // Insert all characters with their frequencies

 // into a priority_queue

 PriorityQueue<Key> pq

 = new PriorityQueue<>(new KeyComparator());

 // Adding high freq elements in descending order

 for (int i = 0; i < n; i++)

 {

 int val = arr[i];

 if (count[val] > 0 && visited[val] != 1)

 pq.add(new Key(count[val], val));

 visited[val] = 1;

 }

 // 'result[]' that will store resultant value

 int result[] = new int[n];

 // work as the previous visited element

 // initial previous element will be ( '-1' and

 // it's frequency will also be '-1' )

 Key prev = new Key(-1, -1);

 // Traverse queue

 int l = 0;

 while (pq.size() != 0)

 {

 // pop top element from queue and add it

 // to result

 Key k = pq.peek();

 pq.poll();

 result[l] = k.num;

 // If frequency of previous element is less

 // than zero that means it is useless, we

 // need not to push it

 if (prev.freq > 0)

 pq.add(prev);

 // make current element as the previous

 // decrease frequency by 'one'

 (k.freq)--;

 prev = k;

 l++;

 }

 // If length of the resultant array and original

 // array is not same then the array is not valid

 if (l != result.length)

 {

 System.out.println(" Not valid Array ");

 }

 // Otherwise Print the result array

 else

 {

 for (int i : result)

 {

 System.out.print(i + " ");

 }

 }

 }

 // Driver Code

 public static void main(String args[])

 {

 int arr[] = new int[] { 1, 1, 1, 1, 2, 2,
3, 3 };

 rearrangeArray(arr);

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

# Python3 program to rearrange numbers in

# an Array such that no two numbers are

# adjacent

# Function to rearrange numbers in array such

# that no two adjacent numbers are same

def rearrangeArray(arr, N) :

 

 # Store frequencies of all elements

 # of the array

 mp = {}

 visited = {} 

 for i in range(N) :

 if(arr[i] in mp) :

 mp[arr[i]] += 1

 else :

 mp[arr[i]] = 1

 

 pq = []

 

 # Adding high freq elements

 # in descending order

 for i in range(N) :

 val = arr[i]

 if((val in mp) and ((val not in visited) or
(visited[val] != 1))) :

 pq.append([mp[val], val])

 visited[val] = 1

 pq.sort()

 pq.reverse()

 

 # 'result[]' that will store resultant value

 result = [0]*N

 

 # Work as the previous visited element

 # initial previous element will be ( '-1' and

 # it's frequency wiint also be '-1' )

 prev = [-1, -1]

 l = 0

 

 # Traverse queue

 while (len(pq) != 0) :

 

 # Pop top element from queue and add it

 # to result

 k = pq[0]

 pq.pop(0)

 result[l] = k[1]

 

 # If frequency of previous element is less

 # than zero that means it is useless, we

 # need not to push it

 if (prev[0] > 0) :

 

 pq.append(prev)

 pq.sort()

 pq.reverse()

 

 # Make current element as the previous

 # decrease frequency by 'one'

 prev = [k[0] - 1, k[1]]

 l += 1

 

 for it in result :

 if (it == 0) :

 

 # If found 0, No valid result

 # array possible

 print("Not valid Array")

 return

 for it in result :

 print(it , end = " ")

 

A = [ 1, 1, 1, 1, 2, 2, 3, 3 ]

 

# Size of the array

N = len(A)

rearrangeArray(A, N)

#This code is contributed by divyesh072019.  
  
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

// C# program to rearrange numbers in

// an Array such that no two numbers are

// adjacent

using System;

using System.Collections.Generic;

class GFG{

 

 // Function to rearrange numbers in array such

 // that no two adjacent numbers are same

 static void rearrangeArray(int[] arr, int N)

 {

 

 // Store frequencies of all elements

 // of the array

 Dictionary<int, int> mp = new Dictionary<int, int>();

 Dictionary<int, int> visited = new Dictionary<int,
int>();

 

 for(int i = 0; i < N; i++)

 {

 if(mp.ContainsKey(arr[i]))

 {

 mp[arr[i]] += 1;

 }

 else{

 mp[arr[i]] = 1;

 }

 }

 

 List<Tuple<int, int>> pq = new
List<Tuple<int,int>>();

 

 // Adding high freq elements

 // in descending order

 for(int i = 0; i < N ; i++)

 {

 int val = arr[i];

 

 if (mp.ContainsKey(val) && (!visited.ContainsKey(val) || visited[val] !=
1))

 {

 pq.Add(new Tuple<int,int>(mp[val], val));

 }

 visited[val] = 1;

 }

 

 pq.Sort();

 pq.Reverse();

 

 // 'result[]' that will store resultant value

 int[] result = new int[N];

 

 // Work as the previous visited element

 // initial previous element will be ( '-1' and

 // it's frequency wiint also be '-1' )

 Tuple<int, int> prev = new Tuple<int,int>( -1, -1 );

 int l = 0;

 

 // Traverse queue

 while (pq.Count != 0)

 {

 

 // Pop top element from queue and add it

 // to result

 Tuple<int,int> k = pq[0];

 pq.RemoveAt(0);

 result[l] = k.Item2;

 

 // If frequency of previous element is less

 // than zero that means it is useless, we

 // need not to push it

 if (prev.Item1 > 0)

 {

 pq.Add(prev);

 pq.Sort();

 pq.Reverse();

 }

 

 // Make current element as the previous

 // decrease frequency by 'one'

 prev = new Tuple<int,int>(k.Item1 - 1, k.Item2);

 l++;

 }

 foreach(int it in result)

 {

 if (it == 0)

 {

 

 // If found 0, No valid result

 // array possible

 Console.WriteLine("Not valid Array");

 return;

 }

 }

 foreach(int it in result)

 {

 Console.Write(it + " ");

 }

 }

 // Driver code

 static void Main()

 {

 int[] A = { 1, 1, 1, 1, 2, 2, 3, 3 };

 

 // Size of the array

 int N = A.Length;

 rearrangeArray(A, N);

 }

}

// This code is contributed by divyeshrabadiya07.  
  
---  
  
 __

 __

 **Output:**

    
    
    1 3 1 2 1 3 2 1

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

