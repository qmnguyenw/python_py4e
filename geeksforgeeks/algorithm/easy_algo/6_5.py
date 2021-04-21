Sort the array of strings according to alphabetical order defined by another
string



Given a string **str** and an array of strings **strArr[]** , the task is to
sort the array according to the alphabetical order defined by **str**.  
**Note:** **str** and every string in **strArr[]** consists of only lower case
alphabets.  
 **Examples:**

> **Input:** str = “fguecbdavwyxzhijklmnopqrst”,  
> strArr[] = {“geeksforgeeks”, “is”, “the”, “best”, “place”, “for”,
> “learning”}  
> **Output:** for geeksforgeeks best is learning place the  
>  **Input:** str = “avdfghiwyxzjkecbmnopqrstul”,  
> strArr[] = {“rainbow”, “consists”, “of”, “colours”}  
> **Output:** consists colours of rainbow

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.  

**Approach:** Traverse every character of **str** and store the value in a map
with **character** as the **key** and its **index** in the array as the
**value**.  
Now, this map will act as the new alphabetical order of the characters. Start
comparing the string in the **strArr[]** and instead of compairing the ASCII
values of the characters, compare the values mapped to those particular
characters in the map i.e. if character **c1** appears before character **c2**
in **str** then **c1 < c2**.  
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

// Map to store the characters with their order

// in the new alphabetical order

unordered_map<char, int> h;

// Function that returns true if x < y

// according to the new alphabetical order

bool compare(string x, string y)

{

 for (int i = 0; i < min(x.size(), y.size()); i++) {

 if (h[x[i]] == h[y[i]])

 continue;

 return h[x[i]] < h[y[i]];

 }

 return x.size() < y.size();

}

// Driver code

int main()

{

 string str = "fguecbdavwyxzhijklmnopqrst";

 vector<string> v{ "geeksforgeeks", "is", "the",

 "best", "place", "for", "learning" };

 // Store the order for each character

 // in the new alphabetical sequence

 h.clear();

 for (int i = 0; i < str.size(); i++)

 h[str[i]] = i; 

 sort(v.begin(), v.end(), compare);

 // Print the strings after sorting

 for (auto x : v)

 cout << x << " ";

 

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

import java.util.Arrays;

import java.util.Comparator;

public class GFG

{

private static void sort(String[] strArr, String str)

{

 Comparator<String> myComp = new Comparator<String>()

 {

 @Override

 public int compare(String a, String b)

 {

 for(int i = 0;

 i < Math.min(a.length(),

 b.length()); i++)

 {

 if (str.indexOf(a.charAt(i)) ==

 str.indexOf(b.charAt(i)))

 {

 continue;

 }

 else if(str.indexOf(a.charAt(i)) >

 str.indexOf(b.charAt(i)))

 {

 return 1;

 }

 else

 {

 return -1;

 }

 }

 return 0;

 }

 };

 Arrays.sort(strArr, myComp);

}

// Driver Code

public static void main(String[] args)

{

 String str = "fguecbdavwyxzhijklmnopqrst";

 String[] strArr = {"geeksforgeeks", "is", "the", "best",

 "place", "for", "learning"};

 

 sort(strArr, str);

 for(int i = 0; i < strArr.length; i++)

 {

 System.out.print(strArr[i] + " ");

 }

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

# Python3 implementation of the approach

# Function to sort and print the array

# according to the new alphabetical order

def sortStringArray(s, a, n):

 

 # Sort the array according to the new alphabetical order

 a = sorted(a, key = lambda word: [s.index(c) for c in
word])

 for i in a:

 print(i, end =' ')

# Driver code

s = "fguecbdavwyxzhijklmnopqrst"

a = ["geeksforgeeks", "is", "the", "best", "place",
"for", "learning"]

n = len(a)

sortStringArray(s, a, n)  
  
---  
  
 __

 __

 **Output:**

    
    
    for geeksforgeeks best is learning place the

_**Time Complexity:** O(N * log(N)), where N is the size of _the _string
**str**_

 _ **Auxiliary Space:** O(N)_

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

