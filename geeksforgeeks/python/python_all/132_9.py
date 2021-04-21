Print all Increasing Subsequence of a List



Given a list or array of integer, the task is to print all such subsequences
of this list such in which the elements are arranged in increasing order.

A _Subsequence_ of the list is an ordered subset of that list’s element having
same sequential ordering as the original list.

 **Examples:**

>  **Input:** arr = {1, 2]}  
>  **Output:**  
>  2  
> 1  
> 1 2
>
>  **Input:** arr = {1, 3, 2}  
>  **Output:**  
>  2  
> 3  
> 1  
> 1 2  
> 1 3
>
>  
>
>
>  
>

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  * Here, we will use recursion to find the desired output.
  * The function will take two lists as an argument and the base condition will be until the list is empty.
  * At each step of recursion, we will make the decision whether to include or exclude a particular element of the original list.
  * For achieving this, we will maintain two list namely **inp** and **out** , the input and output list of that step.
  * While including an element in output list, we will check whether that element is greater than the last element in output list, if yes then we will include that element.
  * When the length of the input list becomes zero then the output list will contain the desired output. This is also a base condition too.

Below is the implementation of the above approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to store all

// increasing subsequence of the given list 

#include<bits/stdc++.h>

using namespace std;

 

vector<vector<int>>st;

 

// Method to find increasing subsequence 

void find(vector<int>inp, vector<int>out)

{

 if(inp.size() == 0)

 {

 if(out.size() != 0)

 {

 

 // Storing result 

 st.push_back(out);

 }

 return;

 }

 

 vector<int>temp;

 temp.push_back(inp[0]);

 

 // Excluding 1st element 

 inp.erase(inp.begin());

 find(inp, out);

 

 // Including first element 

 // checking the condition

 // for increasing subsequence

 if(out.size() == 0)

 find(inp, temp);

 

 else if(temp[0] > out[out.size() - 1])

 {

 out.push_back(temp[0]);

 find(inp, out);

 }

}

 

// Driver code

int main()

{

 

 // Input list

 vector<int>ls1 = { 1, 3, 2 };

 vector<int>ls2;

 

 // Calling the function

 find(ls1, ls2);

 

 // Printing the list

 for(int i = 0; i < st.size(); i++)

 {

 for(int j = 0; j < st[i].size(); j++)

 cout << st[i][j] << " ";

 

 cout << endl;

 }

}

 

// This code is contributed by Stream_Cipher  
  
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

# Python3 implementation

# To store all increasing subsequence of the given list

st = []

 

# Method to find increasing subsequence

def find(inp, out) :

 if len(inp)== 0 :

 if len(out) != 0 :

 # storing result

 st.append(out)

 return

 

 # excluding 1st element

 find(inp[1:], out[:])

 

 # including first element

 # checking the condition

 # for increasing subsequence

 if len(out)== 0:

 find(inp[1:], inp[:1])

 elif inp[0] > out[-1] :

 out.append(inp[0])

 find(inp[1:], out[:])

 

# The input list

ls1 = [1, 3, 2]

ls2 = []

 

# Calling the function

find(ls1, ls2)

 

# Printing the lists

for i in st:

 print(*i)  
  
---  
  
 __

 __

 **Output:**

    
    
    2
    3
    1
    1 2
    1 3
    

**Time Complexity** : ![O\(2^{n}\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-688da79cb9ae16340134d986a9951ee3_l3.png).

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

