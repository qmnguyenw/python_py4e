Python | Get the string after occurrence of given substring



Sometimes, more than finding a substring, we might need to get the string
which is occurring after the substring has been found. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingpartition()**  
The partition function can be used to perform this task in which we just
return the part of partition occurring after the partition word.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Get String after substring occurrence

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

# Get String after substring occurrence

res = test_string.partition(spl_word)[2]

 

# print result

print("String after the substring occurrence : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GeeksforGeeks is best for geeks
    The split string : best
    String after the substring occurrence :  for geeks
    

**Method #2 : Usingsplit()**  
The split function can also be applied to perform this particular task, in
this function, we use the power of limiting the split and then print the later
string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Get String after substring occurrence

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

# Get String after substring occurrence

res = test_string.partition(spl_word)[2]

 

# print result

print("String after the substring occurrence : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string : GeeksforGeeks is best for geeks
    The split string : best
    String after the substring occurrence :  for geeks
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

