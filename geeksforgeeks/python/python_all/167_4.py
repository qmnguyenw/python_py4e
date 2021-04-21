Program for Reversed String Pattern



Given a string **str** as the input. The task is to print the pattern as shown
in the example.

 **Examples:**

>  **Input :** str = “geeks”  
>  **Output :**  
>  g  
> e e  
> * s k  
>  **Explanation :**  
>  In the first line print the first character in the string.  
> In the second line print the next two characters in reverse order.  
> In the third line there are not enough characters to print so append *s and
> print the characters in reverse order.
>
>  **Input:** str = “orange”  
>  **Output:**  
>  o  
> a r  
> e g n

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  * Initialize an empty list and a variable **x** with value **1**.
  * Traverse through the input string **str** and append the characters to the list.
  * If the length of the list is equal to the value of **x** then
    1. Print the characters in the list in reverse order.
    2. Increment the value of x by 1.
    3. Empty the list
  * If the length of the last printed characters is not **0** and it is less than the value of **x** then append **x-length(x) *s** and print it in reverse order.

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

 

// method declared to print the pattern of

// the string passed as argument

void reverseString(string str)

 { 

 // a temporary string to store the 

 // value of each row of pattern 

 string r = "";

 int x = 1;

 for (int i = 0 ; i < str.length(); i++)

 { 

 // extracting each character and 

 // adding it to the string r

 r = r + str[i];

 if (r.length() == x)

 {

 // loop to print the string r in reverse order

 for(int j = r.length() - 1; j >= 0; j--)

 cout<<r.at(j) << " ";

 x += 1;

 r = "";

 cout<<endl;

 }

 }

 

 // condition checking to add the "*" if required

 if (r.length() < x && r.length() != 0)

 { 

 // adding the number of "*" required in r

 for(int k = 1; k <= x - r.length(); k++)

 r = r + "*";

 

 // printing r in reverse order 

 for(int j = r.length() - 1; j >= 0; j--)

 cout << r.at(j) << " "; 

 }

 }

 

// Driver Code

int main()

{ 

 // sample tring to check the code

 string str = "geeks";

 

 // method calling

 reverseString(str);

}

 

// This code is contributed by Rajput-Ji  
  
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

class GFG

{ 

 // method declared to print the pattern of

 // the string passed as argument

 public static void reverseString(String str)

 { 

 // a temporary string to store the 

 // value of each row of pattern 

 String r = "";

 int x = 1;

 for (int i = 0 ; i < str.length(); i++)

 { 

 // extracting each character and 

 // adding it to the string r

 r = r + str.charAt(i);

 if (r.length() == x)

 {

 // loop to print the string r in reverse order

 for(int j = r.length() - 1; j >= 0; j--)

 System.out.print(r.charAt(j) + " ");

 x += 1;

 r = "";

 System.out.println();

 }

 }

 

 // condition checking to add the "*" if required

 if (r.length() < x && r.length() != 0)

 { 

 // adding the number of "*" required in r

 for(int k = 1; k <= x - r.length(); k++)

 r = r + "*";

 

 // printing r in reverse order 

 for(int j = r.length() - 1; j >= 0; j--)

 System.out.print(r.charAt(j) + " "); 

 }

 }

 

 // Driver Code

 public static void main(String args[])

 { 

 // sample tring to check the code

 String str = "geeks";

 

 // method calling

 reverseString(str);

 }

}

 

// This code is contributed by Animesh_Gupta  
  
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

# function to print the pattern

def reverseString(str):

 

 # initialize an empty list

 r = []

 

 # initialize the value of x as 1

 x = 1

 

 # traverse through all the characters of x

 for i in str:

 

 # append all the characters to the list

 r.append(i)

 

 # if the length of the list is x

 if len(r)== x:

 

 # print the list in revere order

 print(*reversed(r))

 

 # increment the value of x

 x+= 1

 # empty the list

 r = []

 

 # if the list is not empty 

 # length of the list is less than x

 if len(r)<x and len(r)!= 0:

 

 # print x-len(r) *s and the reversed list

 print('* ' * (x-len(r)), *reversed(r))

 

# get the input string 

str = "geeks"

 

# calling the function to print the pattern

reverseString(str)  
  
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

using System;

 

class GFG

{ 

 // method declared to print the pattern of

 // the string passed as argument

 public static void reverseString(String str)

 { 

 // a temporary string to store the 

 // value of each row of pattern 

 String r = "";

 int x = 1;

 for (int i = 0 ; i < str.Length; i++)

 { 

 // extracting each character and 

 // adding it to the string r

 r = r + str[i];

 if (r.Length == x)

 {

 // loop to print the string r in reverse order

 for(int j = r.Length - 1; j >= 0; j--)

 Console.Write(r[j] + " ");

 x += 1;

 r = "";

 Console.WriteLine();

 }

 }

 

 // condition checking to add the "*" if required

 if (r.Length < x && r.Length != 0)

 { 

 // adding the number of "*" required in r

 for(int k = 1; k <= x - r.Length; k++)

 r = r + "*";

 

 // printing r in reverse order 

 for(int j = r.Length - 1; j >= 0; j--)

 Console.Write(r[j] + " "); 

 }

 }

 

 // Driver Code

 public static void Main(String []args)

 { 

 // sample tring to check the code

 String str = "geeks";

 

 // method calling

 reverseString(str);

 }

}

 

// This code is contributed by PrinciRaj1992  
  
---  
  
 __

 __

 **Output:**

    
    
    g
    e e
    * s k
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

