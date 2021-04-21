Python | Split string on Kth Occurrence of Character



Many problems of split has been dealt with in past, but sometimes, one can
also encounter this problem in which we need to split the string on the Kth
occurrence of character. Let’s discuss certain ways in which this problem can
be solved.

 **Method #1 : Usingsplit() + join()**  
The split and join method can perform this particular task. In this, we split
the string on basis of character and according to K, we perform a rejoin using
the nested join method.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split string on Kth Occurrence of Character

# Using split() + join()

 

# initializing string 

test_str = "Geeks_for_Geeks_is_best"

 

# split char 

splt_char = "_"

 

# initializing K 

K = 3

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using split() + join()

# Split string on Kth Occurrence of Character

temp = test_str.split(splt_char)

res = splt_char.join(temp[:K]), splt_char.join(temp[K:])

 

# printing result 

print("Is list after Kth split is : " + str(list(res)))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks_for_Geeks_is_best
    Is list after Kth split is : ['Geeks_for_Geeks', 'is_best']
    

**Method #2 : Using regex**  
This problem can also be solved using the regex to perform this particular
task. Along with slicing, the finditer method of regex library can help to
achieve this particular task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split string on Kth Occurrence of Character

# Using regex

import re

 

# initializing string 

test_str = "Geeks_for_Geeks_is_best"

 

# split char 

splt_char = "_"

 

# initializing K 

K = 3

 

# printing original string 

print("The original string is : " + str(test_str))

 

# Using regex

# Split string on Kth Occurrence of Character

temp = [x.start() for x in re.finditer(splt_char, test_str)]

res1 = test_str[0:temp[K - 1]]

res2 = test_str[temp[K - 1] + 1:]

res = (res1 + " " + res2).split(" ")

 

# printing result 

print("Is list after Kth split is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeks_for_Geeks_is_best
    Is list after Kth split is : ['Geeks_for_Geeks', 'is_best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

