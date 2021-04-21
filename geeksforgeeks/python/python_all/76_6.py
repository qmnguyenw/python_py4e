Python – Move Word to Rear end



Sometimes, while working with Python strings, we can have a problem in which
we need to find a word and move it to end of the string. This can have
application in many domains including day-day programming and school
programming. Lets discuss certain ways in which this task can be performed.

 **Method #1 : Usingreplace() + "+" operator**  
The combination of above functions can be used to perform this task. In this,
we replace the element with empty string and append the work to end of string
to perform this task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Move Word to Rear end

# Using replace() + "+" operator

 

# initializing string

test_str = 'Geeksforgeeks is best for geeks '

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing Substring

sub_str = 'best'

 

# Move Word to Rear end

# Using replace() + "+" operator

res = test_str.replace(sub_str, "") + str(sub_str)

 

# printing result 

print("The string after word removal : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Geeksforgeeks is best for geeks 
    The string after word removal : Geeksforgeeks is  for geeks best
    

**Method #2 : Using string slicing andfind()**  
The combination of above functionalities can also be used to perform this
task. In this, we construct the list of string and join it again after
performing move using find() and slicing.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Move Word to Rear end

# Using string slicing and find()

 

# initializing string

test_str = 'Geeksforgeeks is best for geeks '

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing Substring

sub_str = 'best'

 

# Move Word to Rear end

# Using string slicing and find()

res = test_str[:test_str.find(sub_str)] +
test_str[test_str.find(sub_str) + len(sub_str):] + sub_str

 

# printing result 

print("The string after word removal : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original string is : Geeksforgeeks is best for geeks 
    The string after word removal : Geeksforgeeks is  for geeks best
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

