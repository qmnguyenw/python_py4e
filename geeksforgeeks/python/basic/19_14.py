Program to check if a string contains any special character



Given a string, the task is to check if that string contains any special
character (defined special character set). If any special character found,
don’t accept that string.

 **Examples :**

    
    
    Input : Geeks$For$Geeks
    Output : String is not accepted.
    
    Input : Geeks For Geeks
    Output : String is accepted
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach :** Make a regular expression(regex) object of all the special
characters that we don’t want, then pass a string in search method. If any one
character of string is matching with regex object then search method returns a
match object otherwise return None.

Below is the implementation :  

## C++

 __

 __  
 __

 __

 __  
 __  
 __

// C++ program to check if a string

// contains any special character

 

// import required packages

#include <iostream> 

#include <regex> 

using namespace std; 

 

// Function checks if the string 

// contains any special character

void run(string str)

{

 

 // Make own character set 

 regex regx("[@_!#$%^&*()<>?/|}{~:]");

 

 // Pass the string in regex_search 

 // method

 if(regex_search(str, regx) == 0)

 cout << "String is accepted";

 else

 cout << "String is not accepted.";

} 

 

// Driver Code 

int main() 

{ 

 

 // Enter the string 

 string str = "Geeks$For$Geeks"; 

 

 // Calling run function

 run(str); 

 

 return 0; 

}

 

// This code is contributed by Yash_R  
  
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

# Python3 program to check if a string

# contains any special character

 

# import required package

import re

 

# Function checks if the string

# contains any special character

def run(string):

 

 # Make own character set and pass 

 # this as argument in compile method

 regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

 

 # Pass the string in search 

 # method of regex object. 

 if(regex.search(string) == None):

 print("String is accepted")

 

 else:

 print("String is not accepted.")

 

 

# Driver Code

if __name__ == '__main__' :

 

 # Enter the string

 string = "Geeks$For$Geeks"

 

 # calling run function 

 run(string)  
  
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

<?Php

// PHP program to check if a string 

// contains any special character 

 

// Function checks if the string 

// contains any special character 

function run($string)

{

 $regex = preg_match('[@_!#$%^&*()<>?/\|}{~:]', 

 $string);

 if($regex) 

 print("String is accepted"); 

 

 else

 print("String is not accepted.");

} 

 

// Driver Code 

 

// Enter the string 

$string = 'Geeks$For$Geeks';

 

// calling run function

run($string);

 

// This code is contributed by Aman ojha

?>  
  
---  
  
 __

 __

 **Output :**

    
    
    String is not accepted.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

