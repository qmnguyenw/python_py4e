Python Program to find the Larger String without Using Built-in Functions



Given two strings. The task is to find the larger string without using built-
in functions.

 **Examples:**

    
    
     **Input:**
    GeeksforGeeks
    Geeks
    **Output:**
    GeeksforGeeks
    
    **Input:**
    GeeksForFeeks is an good Computer Coding Website
    It offers several topics
    **Output:**
    GeeksForFeeks is an good Computer Coding Website
    

**Step-by-step Approach:**

  * Take two strings in separate variables.
  * Initialize the two count variables to zero.
  * Use a for loop to traverse through the characters in the string and increment the count variables each time a character is encountered.
  * Compare the count variables of both the strings.
  * Print the larger string.
  * Exit.

 **Below is the complete program based on the above approach:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

string1="GeeksForFeeks is an good Computer Coding Website "

string2="It offers several topics"

count1=0

count2=0

 

for i in string1:

 count1=count1+1

for j in string2:

 count2=count2+1

 

if(count1<count2):

 print("Larger string is:")

 print(string2)

 

elif(count1==count2):

 print("Both strings are equal.")

 

else:

 print("Larger string is:")

 print(string1)  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    Larger string is:
    GeeksForFeeks is an good Computer Coding Website 
    

