Python | Converting String content to dictionary



Sometimes, we are fed with string and we may have to convert it’s content to
dictionary. The string may have a specified format that could be key-value
convertible. This type of problem is quite common in Machine Learning domain.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Usingsplit() \+ dictionary comprehension**  
The combination of above method can be used to perform this particular task.
This is 2 process method. In 1st step, the string is converted to list using
split and then converted back to dictionary using dictionary comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Converting String content to dictionary

# Using dictionary comprehension + split()

 

# initializing string 

test_str = "Gfg = 1, Good = 2, CS = 3, Portal = 4"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using dictionary comprehension + split()

# Converting String content to dictionary

res = {key: int(val) for key, val in (item.split('=')

 for item in test_str.split(', '))}

 

# printing result 

print("The newly created dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Gfg = 1, Good = 2, CS = 3, Portal = 4
    The newly created dictionary : {' CS ': 3, 'Gfg ': 1, ' Portal ': 4, ' Good ': 2}
    

**Method #2 : Usingeval()**  
This particular problem can be solved using the inbuilt function eval which
internally evaluates the string and converts the string to dictionary
depending upon the condition.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Converting String content to dictionary

# Using eval()

 

# initializing string 

test_str = "Gfg = 1, Good = 2, CS = 3, Portal = 4"

 

# printing original string 

print("The original string is : " + test_str)

 

# Using eval()

# Converting String content to dictionary

res = eval('dict(% s)' % test_str)

 

# printing result 

print("The newly created dictionary : " + str(res))  
  
---  
  
 __

 __

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

