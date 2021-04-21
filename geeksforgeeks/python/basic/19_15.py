Program to print all the numbers divisible by 3 and 5 for a given number



Given the integer N, the task is to print all the numbers less than N, which
are divisible by 3 and 5.

 **Examples :**

    
    
    Input : 50
    Output : 0 15 30 45 
    
    Input : 100
    Output : 0 15 30 45 60 75 90 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach :** For example, let’s take N = 20 as a limit, then the program
should print all numbers less than 20 which are divisible by both 3 and 5. For
this divide each number from 0 to N by both 3 and 5 and check their remainder.
If remainder is 0 in both cases then simply print that number.

Below is the implementaion :  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to print all the numbers

// divisible by 3 and 5 for a given number

#include <iostream>

using namespace std;

 

// Result function with N

void result(int N)

{ 

 // iterate from 0 to N

 for (int num = 0; num < N; num++)

 { 

 // Short-circuit operator is used 

 if (num % 3 == 0 && num % 5 == 0)

 cout << num << " ";

 }

}

 

// Driver code

int main()

{ 

 // input goes here

 int N = 100;

 

 // Calling function

 result(N);

 return 0;

}

 

// This code is contributed by Manish Shaw

// (manishshaw1)  
  
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

// Java program to print all the numbers

// divisible by 3 and 5 for a given number

 

class GFG{

 

 // Result function with N

 static void result(int N)

 { 

 // iterate from 0 to N

 for (int num = 0; num < N; num++)

 { 

 // Short-circuit operator is used 

 if (num % 3 == 0 && num % 5 == 0)

 System.out.print(num + " ");

 }

 }

 

 // Driver code

 public static void main(String []args)

 {

 // input goes here

 int N = 100;

 

 // Calling function

 result(N);

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

# Python program to print all the numbers

# divisible by 3 and 5 for a given number

 

# Result function with N

def result(N):

 

 # iterate from 0 to N

 for num in range(N):

 

 # Short-circuit operator is used 

 if num % 3 == 0 and num % 5 == 0:

 print(str(num) + " ", end = "")

 

 else:

 pass

 

# Driver code

if __name__ == "__main__":

 

 # input goes here

 N = 100

 

 # Calling function

 result(N)  
  
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

// C# program to print all the numbers

// divisible by 3 and 5 for a given number

using System;

public class GFG{

 

 // Result function with N

 static void result(int N)

 { 

 // iterate from 0 to N

 for (int num = 0; num < N; num++)

 { 

 // Short-circuit operator is used 

 if (num % 3 == 0 && num % 5 == 0)

 Console.Write(num + " ");

 }

 }

 

 // Driver code

 static public void Main (){

 // input goes here

 int N = 100;

 // Calling function

 result(N);

 }

//This code is contributed by ajit. 

}  
  
---  
  
 __

 __

## PHP

 __

 __  
 __

 __

 __  
 __  
 __

<?php

// PHP program to print all the numbers

// divisible by 3 and 5 for a given number

 

// Result function with N

function result($N)

{ 

 // iterate from 0 to N

 for ($num = 0; $num < $N; $num++)

 { 

 // Short-circuit operator is used 

 if ($num % 3 == 0 && $num % 5 == 0)

 echo $num, " ";

 }

}

 

// Driver code

 

// input goes here

$N = 100;

 

// Calling function

result($N);

 

// This code is contributed by ajit

?>  
  
---  
  
 __

 __

  
 **Output :**

    
    
    0 15 30 45 60 75 90 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

