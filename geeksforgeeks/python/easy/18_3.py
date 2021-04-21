Minimum number of characters to be replaced to make a given string Palindrome



Given a string **str** , the task is to find the minimum number of characters
to be replaced to make a given string palindrome. Replacing a character means
replacing it with any single character at the same position. We are not
allowed to remove or add any characters.

If there are multiple answers, print the lexicographically smallest string.

 **Examples:**

    
    
    **Input:** str = "geeks"
    **Output:** 2
    geeks can be converted to geeeg to make it palindrome
    by replacing minimum characters.
    
    **Input:** str = "ameba"
    **Output:** 1
    We can get "abeba" or "amema" with only 1 change. 
    Among those two, "abeba" is lexicographically smallest.
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:** Run a loop from 0 up to (length)/2-1 and check if a character
at ith index i.e. s[i]!=s[length-i-1] then we will replace the alphabetically
larger character with the one which is alphabetically smaller among them and
continue the same process until all the elements gets traversed.

Below is the implementation of the above approach:  

## C++

  

  

 __

 __  
 __

 __

 __  
 __  
 __

// C++ Implementation of the above approach

#include<bits/stdc++.h>

using namespace std;

 

// Function to find the minimum number 

// character change required 

 

void change(string s)

{

 

 // Finding the length of the string 

 int n = s.length(); 

 

 // To store the number of replacement operations 

 int cc = 0;

 

 for(int i=0;i<n/2;i++)

 {

 

 // If the characters at location 

 // i and n-i-1 are same then 

 // no change is required 

 if(s[i]== s[n-i-1]) 

 continue;

 

 // Counting one change operation 

 cc+= 1;

 

 // Changing the character with higher 

 // ascii value with lower ascii value 

 if(s[i]<s[n-i-1]) 

 s[n-i-1]= s[i] ;

 else

 s[i]= s[n-i-1] ;

 }

 printf("Minimum characters to be replaced = %d\n", (cc)) ;

 cout<<s<<endl; 

}

// Driver code 

int main()

{

string s = "geeks";

change((s));

return 0;

}

//contributed by Arnab Kundu  
  
---  
  
 __

 __

