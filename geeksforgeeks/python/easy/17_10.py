Count of lines required to write the given String



Given a string **str** and an integer array **width[]** where:

> width[0] = width of character ‘a’  
> width[1] = width of character ‘b’  
> …  
> width[25] = width of character ‘z’

The task is to find the number of lines it’ll take to write the string **str**
on a paper and the width of the last line upto which it is occupied.  
 **Note:** Width of a line is **10 units**.

 **Examples:**

>  **Input:** str = “bbbcccdddaa”,  
> width[] = {4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
> 1, 1, 1, 1}  
>  **Output:** (2, 8)  
> “bbbcccddd” will cover first line (9 * 1 = 9 units)  
> As ‘a’ has a width of 4 which cannot fit the remaining 1 unit in the first
> line.  
> It’ll have to be written in the second line.  
> So, next line will contain “aa” covering 4 * 2 = 8 units.  
> We need 1 full line and one line with width 8 units.
>
>  
>
>
>  
>
>
>  **Input:** str = “abcdefghijklmnopqrstuvwxyz”,  
> width[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
> 1, 1, 1, 1}  
>  **Output:** (3, 6)  
> All the characters have the same width of 1. To write all 26 characters,  
> We need 2 full lines and one line with width 6 units.

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** We will write each character in the string **str** one by one.
As we write a character, we immediately update (lines, width) that keeps track
of how many lines we have used till now and what is the length of the used
space in the last line.  
If the **width[char]** in **str** fits our current line, we will add it.
Otherwise, we will start with a new line

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

 

// Function to return the number of lines required

pair<int, int> numberOfLines(string S, int *widths)

{

 // If string is empty

 if (S.empty())

 return {0, 0};

 

 // Initialize lines and width

 int lines = 1, width = 0;

 

 // Iterate through S

 for (auto character : S)

 {

 int w = widths[character - 'a'];

 width += w;

 

 if (width >= 10)

 {

 lines++;

 width = w;

 }

 }

 

 // Return lines and width used

 return {lines, width};

}

 

// Driver Code

int main()

{

 string S = "bbbcccdddaa";

 int widths[] = {4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,

 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

 

 // Function call to print required answer

 pair<int, int> ans = numberOfLines(S, widths);

 cout << ans.first << " " << ans.second << endl;

 

 return 0;

}

 

// This code is contributed by

// sanjeev2552  
  
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

// JAVA implementation of the approach

class GFG

{

 

// Function to return the number of lines required

static int[] numberOfLines(String S, int []widths)

{

 // If String is empty

 if (S.isEmpty())

 return new int[]{0, 0};

 

 // Initialize lines and width

 int lines = 1, width = 0;

 

 // Iterate through S

 for (char character : S.toCharArray())

 {

 int w = widths[character - 'a'];

 width += w;

 

 if (width >= 10)

 {

 lines++;

 width = w;

 }

 }

 

 // Return lines and width used

 return new int[]{lines, width};

}

 

// Driver Code

public static void main(String[] args)

{

 String S = "bbbcccdddaa";

 int widths[] = {4, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1,

 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1};

 

 // Function call to print required answer

 int []ans = numberOfLines(S, widths);

 System.out.print(ans[0]+ " " + ans[1] +"\n");

}

}

 

// This code is contributed by Rajput-Ji  
  
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

 

# Function to return the number of lines required

def numberOfLines(S, widths):

 

 # If string is empty

 if(S == ""):

 return 0, 0

 

 # Initialize lines and width

 lines, width = 1, 0

 

 # Iterate through S

 for c in S:

 w = widths[ord(c) - ord('a')]

 width += w

 if width > 10:

 lines += 1

 width = w

 

 # Return lines and width used

 return lines, width

 

 

# Driver Code

S = "bbbcccdddaa"

Widths = [4, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1,

 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1]

 

# Function call to print required answer

print(numberOfLines(S, Widths))  
  
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

 

class GFG

{

 

// Function to return the number of lines required

static int[] numberOfLines(String S, int []widths)

{

 // If String is empty

 if (S.Length == 0)

 return new int[]{0, 0};

 

 // Initialize lines and width

 int lines = 1, width = 0;

 

 // Iterate through S

 foreach (char character in S.ToCharArray())

 {

 int w = widths[character - 'a'];

 width += w;

 

 if (width >= 10)

 {

 lines++;

 width = w;

 }

 }

 

 // Return lines and width used

 return new int[]{lines, width};

}

 

// Driver Code

public static void Main(String[] args)

{

 String S = "bbbcccdddaa";

 int []widths = {4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,

 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

 

 // Function call to print required answer

 int []ans = numberOfLines(S, widths);

 Console.Write(ans[0]+ " " + ans[1] +"\n");

}

}

 

// This code is contributed by 29AjayKumar  
  
---  
  
 __

 __

 **Output:**

    
    
    (2, 8)
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

