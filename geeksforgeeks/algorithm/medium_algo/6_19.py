Expand the string according to the given conditions



Given string **str** of the type **“3(ab)4(cd)”** , the task is to expand it
to “abababcdcdcdcd” where integers are from the range **[1, 9]**.  
This problem was asked in ThoughtWorks interview held in October 2018.  
 **Examples:**

> **Input:** str = “3(ab)4(cd)”  
> **Output:** abababcdcdcdcd  
>  **Input:** str = “2(kl)3(ap)”  
> **Output:** klklapapap

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach:** We traverse through the string and wait for a numeric value,
**num** to turn up at position **i**. As soon as it arrives, we check **i +
1** for a **‘(‘**. If it’s present then the program enters into a loop to
extract whatever is within **‘(‘** and **‘)’** and concatenate it to an empty
string, **temp**. Later another loop prints the generated string **num**
number of times. Repeat these steps until the string finishes.  
Below is the implementation of the approach:  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include<bits/stdc++.h>

using namespace std;

// Function to expand and print the given string

void expandString(string strin)

{

 string temp = "";

 int j;

 for (int i = 0; i < strin.length(); i++)

 {

 if (strin[i] >= 0)

 {

 // Subtract '0' to convert char to int

 int num = strin[i] - '0';

 if (strin[i + 1] == '(')

 {

 // Characters within brackets

 for (j = i + 1; strin[j] != ')'; j++)

 {

 if ((strin[j] >= 'a' && strin[j] <= 'z') ||

 (strin[j] >= 'A' && strin[j] <= 'Z'))

 {

 temp += strin[j];

 }

 }

 // Expanding

 for (int k = 1; k <= num; k++)

 {

 cout << (temp);

 }

 // Reset the variables

 num = 0;

 temp = "";

 if (j < strin.length())

 {

 i = j;

 }

 }

 }

 }

}

// Driver code

int main()

{

 string strin = "3(ab)4(cd)";

 expandString(strin);

}

// This code is contributed by Surendra_Gangwar  
  
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

public class GFG {

 // Function to expand and print the given string

 static void expandString(String strin)

 {

 String temp = "";

 int j;

 for (int i = 0; i < strin.length(); i++) {

 if (strin.charAt(i) >= 0) {

 // Subtract '0' to convert char to int

 int num = strin.charAt(i) - '0';

 if (strin.charAt(i + 1) == '(') {

 // Characters within brackets

 for (j = i + 1; strin.charAt(j) != ')'; j++) {

 if ((strin.charAt(j) >= 'a'

 && strin.charAt(j) <= 'z')

 || (strin.charAt(j) >= 'A'

 && strin.charAt(j) <= 'Z')) {

 temp += strin.charAt(j);

 }

 }

 // Expanding

 for (int k = 1; k <= num; k++) {

 System.out.print(temp);

 }

 // Reset the variables

 num = 0;

 temp = "";

 if (j < strin.length()) {

 i = j;

 }

 }

 }

 }

 }

 // Driver code

 public static void main(String args[])

 {

 String strin = "3(ab)4(cd)";

 expandString(strin);

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

# Function to expand and print the given string

def expandString(strin):

 

 temp = ""

 j = 0

 i = 0

 while(i < len(strin)):

 if (strin[i] >= "0"):

 

 # Subtract '0' to convert char to int

 num = ord(strin[i])-ord("0")

 if (strin[i + 1] == '('):

 

 # Characters within brackets

 j = i + 1

 while(strin[j] != ')'):

 if ((strin[j] >= 'a' and strin[j] <= 'z') or \

 (strin[j] >= 'A' and strin[j] <= 'Z')):

 temp += strin[j]

 j += 1

 

 # Expanding

 for k in range(1, num + 1):

 print(temp,end="")

 

 # Reset the variables

 num = 0

 temp = ""

 if (j < len(strin)):

 i = j

 i += 1

# Driver code

strin = "3(ab)4(cd)"

expandString(strin)

# This code is contributed by shubhamsingh10  
  
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

// C# implementation of

// the above approach

using System;

class GFG{

// Function to expand and

// print the given string

static void expandString(string strin)

{

 string temp = "";

 int j;

 for (int i = 0;

 i < strin.Length; i++)

 {

 if (strin[i] >= 0)

 {

 // Subtract '0' to

 // convert char to int

 int num = strin[i] - '0';

 if (strin[i + 1] == '(')

 {

 // Characters within brackets

 for (j = i + 1;

 strin[j] != ')'; j++)

 {

 if ((strin[j] >= 'a' &&

 strin[j] <= 'z') ||

 (strin[j] >= 'A' &&

 strin[j] <= 'Z'))

 {

 temp += strin[j];

 }

 }

 // Expanding

 for (int k = 1; k <= num; k++)

 {

 Console.Write(temp);

 }

 // Reset the variables

 num = 0;

 temp = "";

 if (j < strin.Length)

 {

 i = j;

 }

 }

 }

 }

}

// Driver code

public static void Main(String [] args)

{

 string strin = "3(ab)4(cd)";

 expandString(strin);

}

}

// This code is contributed by Chitranayal  
  
---  
  
 __

 __

 **Output:**

    
    
    abababcdcdcdcd
    
    
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

  
  

  

My Personal Notes _arrow_drop_up_

Save

