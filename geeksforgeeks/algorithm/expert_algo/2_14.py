Find all the possible mappings of characters in a sorted order



Given a number find all the possible mappings of the characters in sorted
order.

 **Examples:**

    
    
    **Input:** 123
    **Output:** ABC
             AW
             LC
    **Explanation:** 
    1 = A; 2 = B; 3 = C; 12 = L; 23 = W 
    
                     {1, 2, 3}                          
                    /        \                          
                   /          \                         
           "A"{2, 3}           "L"{3}                      
               /      \          /   \                  
              /        \        /     \
            "AB"{3}  "A"{23}  **"LC"**    null
            /  \        /  \
           /    \      /    \
          **"ABC"** null  **"AW"**  null 
    
    **Input :** 2122
    **Output :** BABB
             BAV
             BLB
             UBB
             UV
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach :**

  1. A recursive function which takes an input character array which contains the number stored in a form of characters, an output character array, and two variables(say i and j) that can be used to iterate over both the arrays is created.
  2. Using recursion, character for the ith digit in the input array is obtained and the corresponding mapped character with that digit is stored at the jth index in the output array.
  3. There will be two recursive calls. The first call will process a single-digit every time, whereas the second call will process two digits at a time.
  4. While processing two digits at a time, the number should be always less than 26 because after combining, the corresponding character has to lie between A to Z.
  5. At last, in the base case when the whole input string has been processed, the output array is printed.

Below is the implementation of the above approach.  

## CPP

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to find all the possible

// string mappings of a given number

// in a sorted order

#include <bits/stdc++.h>

using namespace std;

 

// Function to find the string mappings

void mapped(char inputarr[], char outputarr[],

 int i, int j)

{

 

 // Base case

 if (inputarr[i] == '\0') {

 outputarr[j] = '\0';

 cout << outputarr << endl;

 return;

 }

 

 // Convert the character to integer

 int digit = inputarr[i] - '0';

 

 // To store the characters corresponding

 // to the digits which are further

 // stored in outputarr[]

 char ch = digit + 'A' - 1;

 outputarr[j] = ch;

 

 // First recursive call taking one digit at a time

 mapped(inputarr, outputarr, i + 1, j + 1);

 

 if (inputarr[i + 1] != '\0') {

 int second_digit = inputarr[i + 1] - '0';

 int number = digit * 10 + second_digit;

 

 if (number <= 26) {

 ch = number + 'A' - 1;

 outputarr[j] = ch;

 

 // Second recursive call processing

 // two digits at a time

 mapped(inputarr, outputarr, i + 2, j + 1);

 }

 }

}

 

// Driver code

int main()

{

 char inputarr[] = { '1', '2', '3' };

 int m = pow(2, 3) - 1;

 int n = sizeof(m) / sizeof(int);

 char outputarr[n];

 

 mapped(inputarr, outputarr, 0, 0);

 

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

// Java program to find all the possible

// string mappings of a given number 

// in a sorted order 

 

class GFG

{

 

 // Function to find the string mappings 

 static void mapped(char inputarr[], char outputarr[], 

 int i, int j) 

 { 

 

 // Base case 

 if (i >= inputarr.length)

 { 

 String str = new String(outputarr);

 System.out.println(str.substring(0, j)); 

 return; 

 } 

 

 // Convert the character to integer 

 int digit = inputarr[i] - '0'; 

 

 // To store the characters corresponding 

 // to the digits which are further 

 // stored in outputarr[] 

 char ch = (char)(digit + (int)('A') - 1); 

 outputarr[j] = ch; 

 

 // First recursive call taking one digit at a time 

 mapped(inputarr, outputarr, i + 1, j + 1); 

 

 if (i + 1 < inputarr.length) 

 { 

 int second_digit = inputarr[i + 1] - '0'; 

 int number = digit * 10 + second_digit; 

 

 if (number <= 26) 

 { 

 ch = (char)(number + (int)'A' - 1); 

 outputarr[j] = ch; 

 

 // Second recursive call processing 

 // two digits at a time 

 mapped(inputarr, outputarr, i + 2, j + 1); 

 } 

 } 

 } 

 

 // Driver code 

 public static void main (String[] args) 

 { 

 char inputarr[] = { '1', '2', '3' }; 

 int m = (int)Math.pow(2, 3) - 1; 

 int n = 1; 

 char outputarr[] = new char[m]; 

 

 mapped(inputarr, outputarr, 0, 0); 

 } 

}

 

// This code is contributed by AnkitRai01  
  
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

# Python3 program to find all the possible

# string mappings of a given number

# in a sorted order

 

# Function to find the string mappings

def mapped(inputarr, outputarr, i, j):

 

 # Base case

 if (i == len(inputarr)):

 print("".join(outputarr[:j]))

 return

 

 # Convert the character to integer

 digit = ord(inputarr[i]) - ord('0')

 

 # To store the characters corresponding

 # to the digits which are further

 # stored in outputarr[]

 ch = digit + ord('A') - 1

 outputarr[j] = chr(ch)

 

 # First recursive call taking one digit at a time

 mapped(inputarr, outputarr, i + 1, j + 1)

 

 if (i + 1 < len(inputarr) and [i + 1] !=
'\0'):

 second_digit = ord(inputarr[i + 1]) - ord('0')

 number = digit * 10 + second_digit

 

 if (number <= 26):

 ch = number + ord('A') - 1

 outputarr[j] = chr(ch)

 

 # Second recursive call processing

 # two digits at a time

 mapped(inputarr, outputarr, i + 2, j + 1)

 

# Driver code

inputarr = ['1', '2', '3']

m = pow(2, 3) - 1

n = 1

outputarr = ['0'] * m

 

mapped(inputarr, outputarr, 0, 0)

 

# This code is contributed by mohit kumar 29  
  
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

// C# program to find all the possible

// string mappings of a given number 

// in a sorted order 

using System;

 

class GFG 

{ 

 

 // Function to find the string mappings 

 static void mapped(char []inputarr, char []outputarr, 

 int i, int j) 

 { 

 

 // Base case 

 if (i >= inputarr.Length) 

 { 

 string str = new string(outputarr); 

 Console.WriteLine(str.Substring(0, j)); 

 return; 

 } 

 

 // Convert the character to integer 

 int digit = inputarr[i] - '0'; 

 

 // To store the characters corresponding 

 // to the digits which are further 

 // stored in outputarr[] 

 char ch = (char)(digit + (int)('A') - 1); 

 outputarr[j] = ch; 

 

 // First recursive call taking one digit at a time 

 mapped(inputarr, outputarr, i + 1, j + 1); 

 

 if (i + 1 < inputarr.Length) 

 { 

 int second_digit = inputarr[i + 1] - '0'; 

 int number = digit * 10 + second_digit; 

 

 if (number <= 26) 

 { 

 ch = (char)(number + (int)'A' - 1); 

 outputarr[j] = ch; 

 

 // Second recursive call processing 

 // two digits at a time 

 mapped(inputarr, outputarr, i + 2, j + 1); 

 } 

 } 

 } 

 

 // Driver code 

 public static void Main () 

 { 

 char []inputarr = { '1', '2', '3' }; 

 int m = (int)Math.Pow(2, 3) - 1; 

 int n = 1; 

 char []outputarr = new char[m]; 

 

 mapped(inputarr, outputarr, 0, 0); 

 } 

} 

 

// This code is contributed by AnkitRai01   
  
---  
  
__

__

**Output:**

    
    
    ABC
    AW
    LC
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

