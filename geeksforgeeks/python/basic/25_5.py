Switch Case in Python (Replacement)



What is the replacement of Switch Case in Python ?

Unlike every other programming language we have used before, Python does not
have a switch or case statement. To get around this fact, we use dictionary
mapping.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to convert number into string

# Switcher is dictionary data type here

def numbers_to_strings(argument):

 switcher = {

 0: "zero",

 1: "one",

 2: "two",

 }

 

 # get() method of dictionary data type returns 

 # value of passed argument if it is present 

 # in dictionary otherwise second argument will

 # be assigned as default value of passed argument

 return switcher.get(argument, "nothing")

 

# Driver program

if __name__ == "__main__":

 argument=0

 print (numbers_to_strings(argument))  
  
---  
  
 __

 __

This code is analogous to given code in C++ :

 __

 __  
 __

 __

 __  
 __  
 __

#include<bits/stdc++.h>

using namespace std;

 

// Function to convert number into string

string numbers_to_strings(int argument){

 switch(argument) {

 case 0:

 return "zero";

 case 1:

 return "one";

 case 2:

 return "two";

 default:

 return "nothing";

 };

};

 

// Driver program

int main()

{

 int argument = 0;

 cout << numbers_to_strings(argument);

 return 0;

}  
  
---  
  
 __

 __

Output:

    
    
    Zero
    

This article is contributed by **Shashank Mishra (Gullu)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

  

  

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

