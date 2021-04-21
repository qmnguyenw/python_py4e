Python Program that Displays the Letters that are in the First String but not
in the Second



Python program to display the letters in the first string but not in the
second can be done by taking two sets and subtracting them. As sets support
the difference operator, one set could contain the letters of the first string
and another set could contain the letters of the second string and when
subtracted we could obtain the desired result.

 **Examples:**

    
    
     **Input:** set1 = { 'r', 'o', 'h', 'a', 'n'}
           set2 = { 'r', 'i', 't', 'i', 'k', 'a'}
    **Output:** set1 - set2 = { 'o', 'h', 'n'}
    
    **Input:** a = { 'g', 'e', 'e', 'k', 's', 'f', 'o', 'r'}
           b = { 'g', 'e', 'e', 'k', 's'}
    **Output:** c = a - b = { 'f', 'o', 'r'}
    

**Approach:**

  * Take two string, say, a and b
  * Convert that strings into sets, say, setA and setB
  * Subtract setB from setA
  * Print the result

Below are some examples of the above approach.

 **Example 1:**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# string 1

a = "geeksforgeeks"

 

# string 2

b = "geeks"

 

# convert string 1 into set

setA = set(a)

 

# convert string 2 into set

setB = set(b)

 

# store the difference in form of list

result = setA-setB

 

# print result

print(result)  
  
---  
  
 __

 __

 **Output**

    
    
    {'r', 'f', 'o'}
    

**Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# string 1

a = "rohan"

 

# string 2

b = "mohali"

 

# store the difference of sets

result = set(a)-set(b)

 

# print result

print(result)  
  
---  
  
 __

 __

 **Output**

    
    
    {'r', 'n'}
    

**Note:** The output of the above programs will always be different because
sets are unordered collections, thus when subtracted they produce unordered
results.

By the above approach, we could obtain all the letters present in the first
string but not in the second.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

