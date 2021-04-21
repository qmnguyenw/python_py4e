Move all occurence of letter ‘x’ from the string s to the end using Recursion



Given a **string s** , our task is to move all the occurrence of letter **x**
to the end of the string s using recursion.  
 _ **Note:** If there are only letter x in the given string then return the
string unaltered._

 **Examples:**

> **Input:** s= “geekxsforgexxeksxx”  
> **Output:** geeksforgeeksxxxxx  
> **Explanation:**  
> All occurrence of letter ‘x’ is moved to the end.
>
>  **Input:** s = “xxxxx”  
> **Output:** xxxxx  
> **Explanation:**  
> Since there are only letter x in the given string therefore the output is
> unaltered.  
>

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:**  
To solve the problem mentioned above we can use Recursion. Traverse in the
string and check recursively if the current character is equal to the
character ‘x’ or not. If not then print the character otherwise move to the
next character until the length of the string s is reached.

Below is the implementation of the above approach:

  

  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation to Move all occurence of letter ‘x’

// from the string s to the end using Recursion

#include <bits/stdc++.h>

using namespace std;

// Function to move all 'x' in the end

void moveAtEnd(string s, int i, int l)

{

 if (i >= l)

 return;

 // Store current character

 char curr = s[i];

 // Check if current character is not 'x'

 if (curr != 'x')

 cout << curr;

 // recursive function call

 moveAtEnd(s, i + 1, l);

 // Check if current character is 'x'

 if (curr == 'x')

 cout << curr;

 return;

}

// Driver code

int main()

{

 string s = "geekxsforgexxeksxx";

 int l = s.length();

 moveAtEnd(s, 0, l);

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

// Java implementation to Move all occurence of letter ‘x’

// from the string s to the end using Recursion

import java.util.*;

class GFG{

// Function to move all 'x' in the end

static void moveAtEnd(String s, int i, int l)

{

 if (i >= l)

 return;

 // Store current character

 char curr = s.charAt(i);

 // Check if current character is not 'x'

 if (curr != 'x')

 System.out.print(curr);

 // recursive function call

 moveAtEnd(s, i + 1, l);

 // Check if current character is 'x'

 if (curr == 'x')

 System.out.print(curr);

 return;

}

// Driver code

public static void main(String args[])

{

 String s = "geekxsforgexxeksxx";

 int l = s.length();

 moveAtEnd(s, 0, l);

}

}

// This code is contributed by Code_Mech  
  
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

# Python3 implementation to move all

# occurrences of letter ‘x’ from the

# string s to the end using recursion

# Function to move all 'x' in the end

def moveAtEnd(s, i, l):

 if(i >= l):

 return

 # Store current character

 curr = s[i]

 # Check if current character

 # is not 'x'

 if(curr != 'x'):

 print(curr, end = "")

 # Recursive function call

 moveAtEnd(s, i + 1, l)

 # Check if current character is 'x'

 if(curr == 'x'):

 print(curr, end = "")

 return

# Driver code

if __name__ == '__main__':

 s = "geekxsforgexxeksxx"

 l = len(s)

 moveAtEnd(s, 0, l)

# This code is contributed by Shivam Singh  
  
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

// C# implementation to Move all occurence of letter ‘x’

// from the string s to the end using Recursion

using System;

class GFG{

// Function to move all 'x' in the end

static void moveAtEnd(string s, int i, int l)

{

 if (i >= l)

 return;

 // Store current character

 char curr = s[i];

 // Check if current character is not 'x'

 if (curr != 'x')

 Console.Write(curr);

 // recursive function call

 moveAtEnd(s, i + 1, l);

 // Check if current character is 'x'

 if (curr == 'x')

 Console.Write(curr);

 return;

}

// Driver code

public static void Main()

{

 string s = "geekxsforgexxeksxx";

 int l = s.Length;

 moveAtEnd(s, 0, l);

}

}

// This code is contributed by Nidhi_Biet  
  
---  
  
 __

 __

## Javascript

 __

 __  
 __

 __

 __  
 __  
 __

<script>

// Javascript implementation to Move

// all occurence of letter ‘x’ from

// the string s to the end using Recursion

// Function to move all 'x' in the end

function moveAtEnd(s, i, l)

{

 if (i >= l)

 return;

 // Store current character

 let curr = s[i];

 // Check if current character is not 'x'

 if (curr != 'x')

 document.write(curr);

 // Recursive function call

 moveAtEnd(s, i + 1, l);

 // Check if current character is 'x'

 if (curr == 'x')

 document.write(curr);

 return;

}

// Driver code

let s = "geekxsforgexxeksxx";

let l = s.length;

moveAtEnd(s, 0, l);

// This code is contributed by suresh07

</script>  
  
---  
  
 __

 __

 **Output**

    
    
    geeksforgeeksxxxxx

 **Another Implementation involving swapping of characters:**

In this approach, we will be swapping adjacent characters to bring ‘x’ at the
end.

Below is the implementation of the above technique:

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program for above approach

#include<bits/stdc++.h>

using namespace std;

// Recursive program to bring 'x'

// to the end

void rec(char *a, int i)

{

 

 // When the string is completed

 // from reverse direction end of recursion

 if(i == 0)

 {

 cout << a << endl;

 return;

 }

 

 // If the character x is found

 if(a[i] == 'x')

 {

 

 // Transverse the whole string

 int j = i;

 while(a[j] != '\0' && a[j+1] != '\0')

 {

 

 // Swap the x so that

 // it moves to the last

 swap(a[j], a[j+1]);

 j++;

 }

 }

 

 // call to the smaller problem now

 rec(a, i - 1);

}

// Driver Code

int main()

{

 char a[] = {'g', 'e', 'e', 'k', 'x',

 's', 'x', 'x', 'k', 's', '\0'};

 

 // Size of a

 int n = 10;

 

 // Call to rec

 rec(a,n-1);

}

/* This code is contributed by Harsh kedia */  
  
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

// Java program for the

// above approach

import java.util.*;

class Main{

 

// Recursive program to

// bring 'x' to the end

public static void rec(char a[],

 int i)

{ 

 // When the string is completed

 // from reverse direction end

 // of recursion

 if(i == 0)

 {

 System.out.println(a);

 return;

 }

 // If the character x is found

 if(a[i] == 'x')

 {

 // Transverse the whole string

 int j = i;

 while(a[j] != '\0' &&

 a[j + 1] != '\0')

 {

 // Swap the x so that

 // it moves to the last

 char temp = a[j];

 a[j] = a[j + 1];

 a[j + 1] = temp;

 j++;

 }

 }

 // call to the smaller

 // problem now

 rec(a, i - 1);

} 

// Driver code

public static void main(String[] args)

{

 char a[] = {'g', 'e', 'e', 'k',

 'x', 's', 'x', 'x',

 'k', 's', '\0'};

 // Size of a

 int n = 10;

 // Call to rec

 rec(a,n-1);

}

}

// This code is contributed by divyeshrabadiya07  
  
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

# Python3 program for above approach

# Recursive program to bring 'x'

# to the end

def rec(a, i):

 

 # When the string is completed

 # from reverse direction end

 # of recursion

 if (i == 0):

 a.pop()

 print("".join(a))

 return

 

 # If the character x is found

 if (a[i] == 'x'):

 

 # Transverse the whole string

 j = i

 while(a[j] != '\0' and

 a[j + 1] != '\0'):

 

 # Swap the x so that

 # it moves to the last

 (a[j], a[j + 1]) = (a[j + 1], a[j])

 j += 1

 

 # Call to the smaller problem now

 rec(a, i - 1)

# Driver code

if __name__=="__main__":

 

 a = [ 'g', 'e', 'e', 'k', 'x',

 's', 'x', 'x', 'k', 's', '\0' ]

 

 # Size of a

 n = 10

 

 # Call to rec

 rec(a, n - 1)

# This code is contributed by rutvik_56  
  
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

// C# program for the

// above approach

using System;

class GFG

{

 

 // Recursive program to

 // bring 'x' to the end

 static void rec(char[] a, int i)

 {

 

 // When the string is completed

 // from reverse direction end

 // of recursion

 if(i == 0)

 {

 Console.WriteLine(a);

 return;

 }

 

 // If the character x is found

 if(a[i] == 'x')

 {

 

 // Transverse the whole string

 int j = i;

 while(a[j] != '\0' &&

 a[j + 1] != '\0')

 {

 

 // Swap the x so that

 // it moves to the last

 char temp = a[j];

 a[j] = a[j + 1];

 a[j + 1] = temp;

 j++;

 }

 }

 

 // call to the smaller

 // problem now

 rec(a, i - 1);

 }

 

 // Driver code 

 static void Main()

 {

 char[] a = {'g', 'e', 'e', 'k',

 'x', 's', 'x', 'x',

 'k', 's', '\0'};

 

 // Size of a

 int n = 10;

 

 // Call to rec

 rec(a,n-1);

 }

}

// This code is contributed by divyesh072019  
  
---  
  
 __

 __

 **Output**

    
    
    geeksksxxx

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

