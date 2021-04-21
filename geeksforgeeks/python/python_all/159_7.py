Python | Splitting string to list of characters



Sometimes we get a string and we need to split it into the individual
processing. This is quite a common utility and has application in many
domains, be it Machine Learning or Web Development. Having shorthands to it
can be helpful. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usinglist()**  
This is the simplest way to achieve this particular task using the internal
implementation of the inbuilt list function which helps in breaking a string
into its character components.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# split string to character list

# using list()

 

# initializing string

test_string = 'GeeksforGeeks'

 

# printing the original string

print ("The original string is : " + str(test_string))

 

# using list()

# to split string to character list

res = list(test_string)

 

# printing result

print ("The splitted character's list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original string is : GeeksforGeeks  
> The splitted character’s list is : [‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’, ‘r’,
> ‘G’, ‘e’, ‘e’, ‘k’, ‘s’]

  

  

**Method #2 : Usingmap()**  
The map function can also be used to perform this particular task. The map
function needs to be feeded with _None_ value to perform this task as first
argument and the target string as the last argument. Works for Python2 only.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# split string to character list

# using map()

 

# initializing string

test_string = 'GeeksforGeeks'

 

# printing the original string

print ("The original string is : " + str(test_string))

 

# using map()

# to split string to character list

res = list(map(None, test_string))

 

# printing result

print ("The splitted character's list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original string is : GeeksforGeeks  
> The splitted character’s list is : [‘G’, ‘e’, ‘e’, ‘k’, ‘s’, ‘f’, ‘o’, ‘r’,
> ‘G’, ‘e’, ‘e’, ‘k’, ‘s’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

