Python – Index Mapping Cypher



Sometimes, while working with Python, we can have problems in security or
gaming domain, in which we need to create certain cyphers, they can be
different types of. This includes Index Mapping Cypher in which we pass a
string of integers and we get element characters in that order. Lets discuss
certain ways to construct this.

 **Method #1 : Using loop**  
This is brute force manner in which this can be constructed. In this, we
manually check for each character and map it as index number to value in
string.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Mapping Cypher 

# Using loop

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing cypher string 

cyp_str = "53410"

 

# Index Mapping Cypher 

# Using loop

res = ""

temp = [int(idx) for idx in cyp_str]

for ele in temp:

 res += test_str[ele]

 

# printing result 

print("The deciphered value string : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The deciphered value string : fkseg
    

**Method #2 : Using join() + loop**  
The combination of above functions can also be used to solve this problem. In
this, we reduce a final loop by using join() to construct decipher string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Index Mapping Cypher 

# Using loop + join()

 

# initializing string

test_str = "geeksforgeeks"

 

# printing original string

print("The original string is : " + test_str)

 

# initializing cypher string 

cyp_str = "53410"

 

# Index Mapping Cypher 

# Using loop + join()

res = [test_str[int(idx)] for idx in cyp_str]

res = ''.join(res)

 

# printing result 

print("The deciphered value string : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : geeksforgeeks
    The deciphered value string : fkseg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

