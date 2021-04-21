Rearrange a string so that all same characters become d distance away



Given a string and a positive integer d. Some characters may be repeated in
the given string. Rearrange characters of the given string such that the same
characters become d distance away from each other. Note that there can be many
possible rearrangements, the output should be one of the possible
rearrangements. If no such arrangement is possible, that should also be
reported.  
Expected time complexity is O(n) where n is the length of the input string.

**Examples:**

    
    
    Input:  "abb", d = 2
    Output: "bab"
    
    Input:  "aacbbc", d = 3
    Output: "abcabc"
    
    Input: "geeksforgeeks", d = 3
    Output: egkegkesfesor
    
    Input:  "aaa",  d = 2
    Output: Cannot be rearranged
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

The approach to solve this problem is to count frequencies of all characters
and consider the most frequent character first and place all occurrences of it
as close as possible. After the most frequent character is placed, repeat the
same process for the remaining characters.

  1. Let the given string be str and size of string be n
  2. Traverse str, store all characters and their frequencies in a Max Heap MH(implemented using priority queue). The value of frequency decides the order in MH, i.e., the most frequent character is at the root of MH.
  3. Make all characters of str as ‘\0’.
  4. Do the following while MH is not empty. 
    * Extract the Most frequent character. Let the extracted character be x and its frequency be f.
    * Find the first available position in str, i.e., find the first ‘\0’ in str. 
    * Let the first position be p. Fill x at p, p+d,.. p+(f-1)d

Below is the implementation of the above algorithm.

## C

 __

 __  
 __

 __

 __  
 __  
 __

// C program to rearrange a string so that all same

// characters become at least d distance away

#include <stdio.h>

#include <string.h>

#include <stdlib.h>

#define MAX 256

 

// A structure to store a character 'c' and its frequency

// 'f' in input string

typedef struct charFreq {

 char c;

 int f;

} charFreq ;

 

// A utility function to swap two charFreq items.

void swap(charFreq* x, charFreq* y)

{

 charFreq z = *x;

 *x = *y;

 *y = z;

}

 

// A utility function to maxheapify the node freq[i] of a

// heap stored in freq[]

void maxHeapify(charFreq freq[], int i, int heap_size)

{

 int l = i * 2 + 1;

 int r = i * 2 + 2;

 int largest = i;

 if (l < heap_size && freq[l].f > freq[i].f)

 largest = l;

 if (r < heap_size && freq[r].f > freq[largest].f)

 largest = r;

 if (largest != i) {

 swap(&freq;[i], &freq;[largest]);

 maxHeapify(freq, largest, heap_size);

 }

}

 

// A utility function to convert the array freq[] to a max

// heap

void buildHeap(charFreq freq[], int n)

{

 int i = (n - 1) / 2;

 while (i >= 0) {

 maxHeapify(freq, i, n);

 i--;

 }

}

 

// A utility function to remove the max item or root from

// max heap

charFreq extractMax(charFreq freq[], int heap_size)

{

 charFreq root = freq[0];

 if (heap_size > 1) {

 freq[0] = freq[heap_size - 1];

 maxHeapify(freq, 0, heap_size - 1);

 }

 return root;

}

 

// The main function that rearranges input string 'str' such

// that two same characters become d distance away

void rearrange(char str[], int d)

{

 // Find length of input string

 int n = strlen(str);

 

 // Create an array to store all characters and their

 // frequencies in str[]

 charFreq freq[MAX] = { { 0, 0 } };

 

 int m = 0; // To store count of distinct characters in

 // str[]

 

 // Traverse the input string and store frequencies of

 // all characters in freq[] array.

 for (int i = 0; i < n; i++) {

 char x = str[i];

 

 // If this character has occurred first time,

 // increment m

 if (freq[x].c == 0)

 freq[x].c = x, m++;

 

 (freq[x].f)++;

 str[i] = '\0'; // This change is used later

 }

 

 // Build a max heap of all characters

 buildHeap(freq, MAX);

 

 // Now one by one extract all distinct characters from

 // max heap and put them back in str[] with the d

 // distance constraint

 for (int i = 0; i < m; i++) {

 charFreq x = extractMax(freq, MAX - i);

 

 // Find the first available position in str[]

 int p = i;

 while (str[p] != '\0')

 p++;

 

 // Fill x.c at p, p+d, p+2d, .. p+(f-1)d

 for (int k = 0; k < x.f; k++) {

 // If the index goes beyond size, then string

 // cannot be rearranged.

 if (p + d * k >= n) {

 printf("Cannot be rearranged");

 exit(0);

 }

 str[p + d * k] = x.c;

 }

 }

}

 

// Driver Code

int main()

{

 char str[] = "aabbcc";

 

 // Function Call

 rearrange(str, 3);

 printf("%s",str);

}  
  
---  
  
 __

 __

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to rearrange a string so that all same

// characters become at least d distance away using STL

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

typedef pair<char, int> PAIR;

 

// Comparator of priority_queue

struct cmp {

 bool operator()(const PAIR& a, const PAIR& b)

 {

 if(a.second < b.second) return true;

 else if(a.second > b.second) return false;

 else return a.first > b.first;

 }

};

 

void rearrange(char* str, int d)

{

 // Length of the string

 int n = strlen(str);

 

 // A structure to store a character and its frequency

 unordered_map<char, int> m;

 

 // Traverse the input string and store frequencies of

 // all characters.

 for (int i = 0; i < n; i++) {

 m[str[i]]++;

 str[i] = '\0';

 }

 

 // max-heap

 priority_queue<PAIR, vector<PAIR>, cmp> pq(m.begin(),

 m.end());

 

 // Now one by one extract all distinct characters from

 // heap and put them back in str[] with the d

 // distance constraint

 while (pq.empty() == false) {

 char x = pq.top().first;

 

 // Find the first available position in str[]

 int p = 0;

 while (str[p] != '\0')

 p++;

 

 // Fill x at p, p+d, p+2d, .. p+(frequency-1)d

 for (int k = 0; k < pq.top().second; k++) {

 

 // If the index goes beyond size, then string

 // cannot be rearranged.

 if (p + d * k >= n) {

 cout << "Cannot be rearranged";

 exit(0);

 }

 str[p + d * k] = x;

 }

 pq.pop();

 }

}

 

// Driver Code

int main()

{

 char str[] = "aabbcc";

 

 // Function call

 rearrange(str, 3);

 cout << str;

}  
  
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

# Python program to rearrange a string so that all same

# characters become at least d distance away

MAX = 256

 

# A structure to store a character 'c' and its frequency 'f'

# in input string

 

 

class charFreq(object):

 def __init__(self, c, f):

 self.c = c

 self.f = f

 

# A utility function to swap two charFreq items.

 

 

def swap(x, y):

 return y, x

 

# A utility function

 

 

def toList(string):

 t = []

 for x in string:

 t.append(x)

 

 return t

 

# A utility function

 

 

def toString(l):

 return ''.join(l)

 

# A utility function to maxheapify the node freq[i] of a heap

# stored in freq[]

 

 

def maxHeapify(freq, i, heap_size):

 l = i*2 + 1

 r = i*2 + 2

 largest = i

 if l < heap_size and freq[l].f > freq[i].f:

 largest = l

 if r < heap_size and freq[r].f > freq[largest].f:

 largest = r

 if largest != i:

 freq[i], freq[largest] = swap(freq[i], freq[largest])

 maxHeapify(freq, largest, heap_size)

 

# A utility function to convert the array freq[] to a max heap

 

 

def buildHeap(freq, n):

 i = (n - 1)//2

 while i >= 0:

 maxHeapify(freq, i, n)

 i -= 1

 

# A utility function to remove the max item or root from max heap

 

 

def extractMax(freq, heap_size):

 root = freq[0]

 if heap_size > 1:

 freq[0] = freq[heap_size-1]

 maxHeapify(freq, 0, heap_size-1)

 

 return root

 

# The main function that rearranges input string 'str' such that

# two same characters become d distance away

 

 

def rearrange(string, d):

 # Find length of input string

 n = len(string)

 

 # Create an array to store all characters and their

 # frequencies in str[]

 freq = []

 for x in range(MAX):

 freq.append(charFreq(0, 0))

 

 m = 0

 

 # Traverse the input string and store frequencies of all

 # characters in freq[] array.

 for i in range(n):

 x = ord(string[i])

 

 # If this character has occurred first time, increment m

 if freq[x].c == 0:

 freq[x].c = chr(x)

 m += 1

 

 freq[x].f += 1

 string[i] = '\0'

 

 # Build a max heap of all characters

 buildHeap(freq, MAX)

 

 # Now one by one extract all distinct characters from max heap

 # and put them back in str[] with the d distance constraint

 for i in range(m):

 x = extractMax(freq, MAX-i)

 

 # Find the first available position in str[]

 p = i

 while string[p] != '\0':

 p += 1

 

 # Fill x.c at p, p+d, p+2d, .. p+(f-1)d

 for k in range(x.f):

 

 # If the index goes beyond size, then string cannot

 # be rearranged.

 if p + d*k >= n:

 print ("Cannot be rearranged")

 return

 

 string[p + d*k] = x.c

 

 return toString(string)

 

 

# Driver program

string = "aabbcc"

print (rearrange(toList(string), 3))

 

# This code is contributed by BHAVYA JAIN  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    abcabc

