Permutations of n things taken all at a time with m things never come together



Given **n** and **m** , the task is to find the number of permutations of
**n** distinct things taking them all at a time such that **m** particular
things never come together.  
 **Examples:**  

    
    
    **Input  :** 7, 3
    **Output :** 420
    
    **Input  :** 9, 2
    **Output :** 282240

 **Approach:**  
 **Derivation of the formula –**  
Total number of arrangements possible using n distinct objects taking all at a
time = ![n!  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-ac5276a4cdd5ec8b0bf01449a6e174f0_l3.png)  
Number of arrangements of n distinct things taking all at a time, when m
particular things always come together, is ![\(n-m+1\)! × m!
](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
efece8228c9ae66cd3aaeac0795f5dbd_l3.png)  
Hence, the number of permutations of ![n  ](https://www.geeksforgeeks.org/wp-
content/ql-
cache/quicklatex.com-3ebe7b3d5f19356fe8152deb8e32c84d_l3.png)distinct things
taking all at a time, when ![m  ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-da172dc13d67d481ddb21f56e0f3e860_l3.png)particular things
never come together –  

    
    
    **Permutations = n! - (n-m+1)! × m!**

 **Below is the Python implementation of above approach –**  

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

int factorial(int n)

{

 int fact = 1;

 for (int i = 2; i <= n; i++)

 fact = fact * i ;

 return (fact);

}

int result(int n, int m)

{

 return(factorial(n) - 

 factorial(n - m + 1) *

 factorial(m));

}

// Driver Code

int main()

{

 cout(result(5, 3));

}

// This code is contributed by Mohit Kumar  
  
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

static int factorial(int n)

{

 int fact = 1;

 for (int i = 2; i <= n; i++)

 fact = fact * i ;

 return (fact);

}

static int result(int n, int m)

{

 return(factorial(n) -

 factorial(n - m + 1) *

 factorial(m));

}

// Driver Code

public static void main(String args[])

{

 System.out.println(result(5, 3));

}

}

// This code is contributed by Arnab Kundu  
  
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

def factorial(n):

 fact = 1;

 for i in range(2, n + 1):

 fact = fact * i

 return (fact)

def result(n, m):

 return(factorial(n) - factorial(n - m + 1) *
factorial(m))

# driver code

print(result(5, 3))  
  
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

 static int factorial(int n)

 {

 int fact = 1;

 for (int i = 2; i <= n; i++)

 fact = fact * i ;

 return (fact);

 }

 

 static int result(int n, int m)

 {

 return(factorial(n) -

 factorial(n - m + 1) *

 factorial(m));

 }

 

 // Driver Code

 public static void Main()

 {

 Console.WriteLine(result(5, 3));

 }

}

// This code is contributed by AnkitRai01  
  
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

// Below is the JavaScript implementation of above approach

function factorial(n)

{

 let fact = 1;

 for (let i = 2; i <= n; i++)

 fact = fact * i ;

 return (fact);

}

function result(n, m)

{

 return(factorial(n) -

 factorial(n - m + 1) *

 factorial(m));

}

// Driver Code

document.write(result(5, 3));

// This code is contributed by Surbhi Tyagi.

</script>  
  
---  
  
 __

 __

 **Output :**

    
    
    84

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

