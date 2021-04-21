Python | Union Operation in two Strings



One of the string operation can be computing the union of two strings. This
can be useful application that can be dealt with. This article deals with
computing the same through different ways.

 **Method 1 : Naive Method**  
The task of performing string union can be computed by naive method by
creating an empty string and checking for new occurrence of character common
to both string and not common strings and appending it and hence computing the
new union string. This can be achieved by loops and if/else statements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Union Operation in two Strings

# using naive method 

 

# initializing strings

test_str1 = 'GeeksforGeeks'

test_str2 = 'Codefreaks'

 

# Printing initial strings

print ("The original string 1 is : " + test_str1)

print ("The original string 2 is : " + test_str2)

 

# using naive method to

# Union Operation in two Strings

res = ""

temp = test_str1

for i in test_str2:

 if i not in temp:

 test_str1 += i

 

# printing result

print ("The string union is : " + test_str1)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string 1 is : GeeksforGeeks
    The original string 2 is : Codefreaks
    The string union is : GeeksforGeeksCda
    

**Method 2 : Usingset() + union()**  
Set in python usually can perform the task of performing set operations such
as set union. This utility of sets can be used to perform this task as well.
Firstly, both the strings are converted into sets using set() and then union
is performed using union(). Returns the sorted set.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# Union Operation in two Strings

# using set() + union()

 

# initializing strings

test_str1 = 'GeeksforGeeks'

test_str2 = 'Codefreaks'

 

# Printing initial strings

print ("The original string 1 is : " + test_str1)

print ("The original string 2 is : " + test_str2)

 

# using set() + union() to

# Union Operation in two Strings

res = set(test_str1).union(test_str2)

 

# printing result

print ("The string union is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string 1 is : GeeksforGeeks
    The original string 2 is : Codefreaks
    The string union is : {'s', 'G', 'r', 'e', 'o', 'f', 'k', 'C', 'd', 'a'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

