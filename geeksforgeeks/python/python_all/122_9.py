Python | Convert String to list of tuples



Sometimes, while working with data, we can have a problem in which we have a
string list of data and we need to convert the same to list of records. This
kind of problem can come when we deal with a lot of string data. Let’s discuss
certain ways in which this task can be performed.

 **Method #1 : Using zip() + split() + list slicing**  
The combination of above functionalities can be used to solve this problem. In
this, first, the string is converted to list of strings and then required
tuples are made using zip() and list slicing functionality.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to list of tuples

# Using zip() + list slicing + split()

 

# initialize string 

test_string = "GFG is best Computer Science Portal"

 

# printing original string 

print("The original string : " + str(test_string))

 

# Convert String to list of tuples

# Using zip() + list slicing + split()

temp = test_string.split()

res = list(zip(temp[::2], temp[1::2]))

 

# printing result

print("List after String to tuple conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original string : GFG is best Computer Science Portal  
> List after String to tuple conversion : [(‘GFG’, ‘is’), (‘best’,
> ‘Computer’), (‘Science’, ‘Portal’)]

  

  

**Method #2 : Using iter() + split() + next() \+ generator expression**  
This is yet another method to perform this particular task. In this, we use
iterator to reach to solution of this task. Method is same as above, just
iterator is used for faster access.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert String to list of tuples

# Using iter() + split() + next() + generator expression

 

# initialize string 

test_string = "GFG is best Computer Science Portal"

 

# printing original string 

print("The original string : " + str(test_string))

 

# Convert String to list of tuples

# Using iter() + split() + next() + generator expression

temp = iter(test_string.split())

res = [(ele, next(temp)) for ele in temp]

 

# printing result

print("List after String to tuple conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original string : GFG is best Computer Science Portal  
> List after String to tuple conversion : [(‘GFG’, ‘is’), (‘best’,
> ‘Computer’), (‘Science’, ‘Portal’)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

