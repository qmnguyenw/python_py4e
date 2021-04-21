Count of pairs of strings which differ in exactly one position



Given an array **arr[]** of strings of equal lengths. The task is to calculate
the total number of pairs of strings which differ in exactly one position.

 **Examples:**

>  **Input:** arr[] = {“abc”, “abd”, “bbd”}  
>  **Output:** 2  
> (abc, abd) and (abd, bbd) are the only valid pairs.
>
>  **Input:** arr[] = {“def”, “deg”, “dmf”, “xef”, “dxg”}  
>  **Output:** 4

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1:** For every possible pair, check if both the strings differ in
exactly a single index position with a single traversal of the strings.

  

  

 **Method 2:** Two string can be compared in the following way in order to
check whether they differ in a single index position:

> Let **str1 = “abc”** and **str2 = “adc”**  
>  For **str1** , add **“#bc”** , **“a#c”** and **“ab#”** to a set.  
> Now for **str2** , generate the string in the similar manner and if any of
> the generated string  
> is already present in the set then both the strings differ in exactly 1
> index position.  
> For example, **“a#c”** is one of the generated strings.  
>  **Note** that “#” is used because it will not be a part of any of the
> original strings.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// CPP implementation of the approach

#include <bits/stdc++.h>

using namespace std;

 

// Function to return the count of same pairs

int pairCount(map<string, int> &d;)

{

 int sum = 0;

 for (auto i : d)

 sum += (i.second * (i.second - 1)) / 2;

 

 return sum;

}

 

// Function to return total number of strings

// which satisfy required condition

int difference(vector<string> &array;, int m)

{

 // Dictionary changed will store strings

 // with wild cards

 // Dictionary same will store strings

 // that are equal

 map<string, int> changed, same;

 

 // Iterating for all strings in the given array

 for (auto s : array)

 {

 // If we found the string then increment by 1

 // Else it will get default value 0

 same[s]++;

 

 // Iterating on a single string

 for (int i = 0; i < m; i++)

 {

 // Adding special symbol to the string

 string t = s.substr(0, i) + "//" + s.substr(i + 1);

 

 // Incrementing the string if found

 // Else it will get default value 0

 changed[t]++;

 }

 }

 

 // Return counted pairs - equal pairs

 return pairCount(changed) - pairCount(same) * m;

}

 

// Driver Code

int main()

{

 int n = 3, m = 3;

 vector<string> array = {"abc", "abd", "bbd"};

 cout << difference(array, m) << endl;

 

 return 0;

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

# Python3 implementation of the approach

 

# Function to return the count of same pairs

def pair_count(d):

 return sum((i*(i-1))//2 for i in d.values())

 

 

# Function to return total number of strings 

# which satisfy required condition

def Difference(array, m):

 

 # Dictionary changed will store strings 

 # with wild cards

 # Dictionary same will store strings 

 # that are equal

 changed, same = {}, {}

 

 # Iterating for all strings in the given array

 for s in array:

 

 # If we found the string then increment by 1 

 # Else it will get default value 0

 same[s]= same.get(s, 0)+1

 

 # Iterating on a single string

 for i in range(m):

 # Adding special symbol to the string

 t = s[:i]+'#'+s[i + 1:]

 

 # Incrementing the string if found 

 # Else it will get default value 0

 changed[t]= changed.get(t, 0)+1

 

 # Return counted pairs - equal pairs

 return pair_count(changed) - pair_count(same)*m

 

# Driver code

if __name__=="__main__":

 n, m = 3, 3

 array =["abc", "abd", "bbd"]

 print(Difference(array, m))  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

