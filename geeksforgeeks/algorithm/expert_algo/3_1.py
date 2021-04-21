Check if it is possible to form string B from A under the given constraints



Given two strings **A** and **B** and two integers **b** and **m**. The task
is to find that if it is possible to form string **B** from **A** such that
**A** is divided into groups of **b** characters except the last group which
will have characters **≤ b** and you are allowed to pick atmost **m**
characters from each group, and also order of characters in **B** must be same
as that of **A**. If it is possible then print **Yes** else print **No**.

 **Examples:**

> **Input:** A = abcbbcdefxyz, B = acdxyz, b = 5, m = 2  
> **Output:** Yes  
> Groups can be “abcbb”, “cdefx” and “yz”  
> Now “acdxyz” can be used to pick “ac” and “dx” can be picked from “cdefx”.  
> Finally, “yz” if the last group.
>
>  **Input:** A = abcbbcdefxyz, B = baz, b = 3, m = 2  
> **Output:** No

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** The idea is to use binary search. Iterate through string **A**
and store the frequency of each of the characters of **A** in vector **S**.
Now iterate through **B** and if the current character is not in the vector
then print **No** since its not possible to form string **B** using **A**.
Else, check the first occurrence of current character starting from the index
of the last chosen character **low** , which denotes starting position in
string **A** from where we want to match characters of string **B**. Keep
track of number of characters stored in each group. If it exceeds, the given
limit of characters in current block, we update the pointer **low** to the
next block.

  

  

Below is the implementation of the above approach:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <bits/stdc++.h>

using namespace std;

// Function that returns true if it is possible

// to form B from A satisfying the given conditions

bool isPossible(string A, string B, int b, int m)

{

 // Vector to store the frequency

 // of characters in A

 vector<int> S[26];

 // Vector to store the count of characters

 // used from a particular group of characters

 vector<int> box(A.length(), 0);

 // Store the frequency of the characters

 for (int i = 0; i < A.length(); i++) {

 S[A[i] - 'a'].push_back(i);

 }

 int low = 0;

 for (int i = 0; i < B.length(); i++) {

 auto it = lower_bound(S[B[i] - 'a'].begin(),

 S[B[i] - 'a'].end(), low);

 // If a character in B is not

 // present in A

 if (it == S[B[i] - 'a'].end())

 return false;

 int count = (*it) / b;

 box[count] = box[count] + 1;

 // If count of characters used from

 // a particular group of characters

 // exceeds m

 if (box[count] >= m) {

 count++;

 // Update low to the starting index

 // of the next group

 low = (count)*b;

 }

 // If count of characters used from

 // a particular group of characters

 // has not exceeded m

 else

 low = (*it) + 1;

 }

 return true;

}

// Driver code

int main()

{

 string A = "abcbbcdefxyz";

 string B = "acdxyz";

 int b = 5;

 int m = 2;

 if (isPossible(A, B, b, m))

 cout << "Yes";

 else

 cout << "No";

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

// Java implementation of the approach

import java.io.*;

import java.util.*;

class GFG{

 

// Function that returns true if it is

// possible to form B from A satisfying

// the given conditions

static boolean isPossible(String A, String B,

 int b, int m)

{

 

 // List to store the frequency

 // of characters in A

 List<List<Integer>> S = new ArrayList<List<Integer>>();

 for(int i = 0; i < 26; i++)

 S.add(new ArrayList<Integer>());

 

 // Vector to store the count of characters

 // used from a particular group of characters

 int[] box = new int[A.length()];

 // Store the frequency of the characters

 for(int i = 0; i < A.length(); i++)

 {

 S.get(A.charAt(i) - 'a').add(i);

 }

 int low = 0;

 for(int i = 0; i < B.length(); i++)

 {

 List<Integer> indexes = S.get(

 B.charAt(i) - 'a');

 int it = lower_bound(indexes, low);

 // If a character in B is not

 // present in A

 if (it == indexes.size())

 return false;

 int count = indexes.get(it) / b;

 box[count] = box[count] + 1;

 // If count of characters used from

 // a particular group of characters

 // exceeds m

 if (box[count] >= m)

 {

 count++;

 // Update low to the starting index

 // of the next group

 low = (count) * b;

 }

 // If count of characters used from

 // a particular group of characters

 // has not exceeded m

 else

 low = indexes.get(it) + 1;

 }

 return true;

}

static int lower_bound(List<Integer> indexes, int k)

{

 int low = 0, high = indexes.size() - 1;

 while (low < high)

 {

 int mid = (low + high) / 2;

 if (indexes.get(mid) < k)

 low = mid + 1;

 else

 high = mid;

 }

 return (indexes.get(low) < k) ? low + 1 : low;

}

// Driver code

public static void main(String[] args)

{

 String A = "abcbbcdefxyz";

 String B = "acdxyz";

 int b = 5;

 int m = 2;

 if (isPossible(A, B, b, m))

 System.out.println("Yes");

 else

 System.out.println("No");

}

}

// This code is contributed by jithin  
  
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

# Python3 implementation of the approach

# Function that returns true if it is

# possible to form B from A satisfying

# the given conditions

def isPossible(A, B, b, m) :

 

 # List to store the frequency

 # of characters in A

 S = []

 

 for i in range(26) :

 

 S.append([]) 

 

 # Vector to store the count of characters

 # used from a particular group of characters

 box = [0] * len(A)

 

 # Store the frequency of the characters

 for i in range(len(A)) :

 

 S[ord(A[i]) - ord('a')].append(i)

 

 low = 0

 

 for i in range(len(B)) :

 

 indexes = S[ord(B[i]) - ord('a')]

 

 it = lower_bound(indexes, low)

 

 # If a character in B is not

 # present in A

 if (it == len(indexes)) :

 return False

 

 count = indexes[it] // b

 box[count] = box[count] + 1

 

 # If count of characters used from

 # a particular group of characters

 # exceeds m

 if (box[count] >= m) :

 

 count += 1

 

 # Update low to the starting index

 # of the next group

 low = (count) * b

 

 # If count of characters used from

 # a particular group of characters

 # has not exceeded m

 else :

 low = indexes[it] + 1

 

 return True

 

def lower_bound(indexes, k) :

 low, high = 0, len(indexes) - 1

 

 while (low < high) :

 

 mid = (low + high) // 2

 if (indexes[mid] < k) :

 low = mid + 1

 else :

 high = mid

 

 if indexes[low] < k :

 return (low + 1)

 else :

 return low

 

A = "abcbbcdefxyz"

B = "acdxyz"

b = 5

m = 2

if (isPossible(A, B, b, m)) :

 print("Yes")

else :

 print("No")

 # This code is contributed by divyeshrabadiya07  
  
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

class GFG {

 

 // Function that returns true if it is

 // possible to form B from A satisfying

 // the given conditions

 static bool isPossible(string A, string B, int b, int
m)

 {

 

 // List to store the frequency

 // of characters in A

 List<List<int>> S = new List<List<int>>();

 

 for(int i = 0; i < 26; i++)

 {

 S.Add(new List<int>());

 }

 

 // Vector to store the count of characters

 // used from a particular group of characters

 int[] box = new int[A.Length];

 

 // Store the frequency of the characters

 for(int i = 0; i < A.Length; i++)

 {

 S[A[i] - 'a'].Add(i);

 }

 

 int low = 0;

 

 for(int i = 0; i < B.Length; i++)

 {

 List<int> indexes = S[B[i] - 'a'];

 

 int it = lower_bound(indexes, low);

 

 // If a character in B is not

 // present in A

 if (it == indexes.Count)

 return false;

 

 int count = indexes[it] / b;

 box[count] = box[count] + 1;

 

 // If count of characters used from

 // a particular group of characters

 // exceeds m

 if (box[count] >= m)

 {

 count++;

 

 // Update low to the starting index

 // of the next group

 low = (count) * b;

 }

 

 // If count of characters used from

 // a particular group of characters

 // has not exceeded m

 else

 low = indexes[it] + 1;

 }

 

 return true;

 }

 

 static int lower_bound(List<int> indexes, int k)

 {

 int low = 0, high = indexes.Count - 1;

 

 while (low < high)

 {

 int mid = (low + high) / 2;

 if (indexes[mid] < k)

 low = mid + 1;

 else

 high = mid;

 }

 return (indexes[low] < k) ? low + 1 : low;

 }

 static void Main() {

 

 string A = "abcbbcdefxyz";

 string B = "acdxyz";

 int b = 5;

 int m = 2;

 

 if (isPossible(A, B, b, m))

 Console.WriteLine("Yes");

 else

 Console.WriteLine("No");

 }

}

// This code is contributed by divyesh072019  
  
---  
  
 __

 __

  

**Output:**

    
    
    Yes

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

