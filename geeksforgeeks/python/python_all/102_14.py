Python – String till Substring



Sometimes, more than finding a substring, we might need to get the string that
is occurring before the substring has been found. Let’s discuss certain ways
in which this task can be performed.  

### **Method #1 : Using partition()**  

The partition function can be used to perform this task in which we just
return the part of the partition occurring before the partition word.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# String till Substring

# using partition()

# initializing string

test_string = "GeeksforGeeks is best for geeks"

# initializing split word

spl_word = 'best'

# printing original string

print("The original string : " + str(test_string))

# printing split string

print("The split string : " + str(spl_word))

# using partition()

# String till Substring

res = test_string.partition(spl_word)[0]

# print result

print("String before the substring occurrence : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GeeksforGeeks is best for geeks
    The split string : best
    String before the substring occurrence : GeeksforGeeks is

###  
**Method #2 : Using split()**  

The split function can also be applied to perform this particular task, in
this function, we use the power of limiting the split and then print the
former string.  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# String till Substring

# using split()

# initializing string

test_string = "GeeksforGeeks is best for geeks"

# initializing split word

spl_word = 'best'

# printing original string

print("The original string : " + str(test_string))

# printing split string

print("The split string : " + str(spl_word))

# using split()

# String till Substring

res = test_string.split(spl_word)[0]

# print result

print("String before the substring occurrence : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GeeksforGeeks is best for geeks
    The split string : best
    String before the substring occurrence : GeeksforGeeks is

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

