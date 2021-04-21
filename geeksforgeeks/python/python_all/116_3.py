Python | Remove given character from Strings list



Sometimes, while working with Python list, we can have a problem in which we
need to remove a particular character from each string from list. This kind of
application can come in many domains. Let’s discuss certain ways to solve this
problem.

 **Method #1 : Usingreplace() + enumerate() \+ loop**  
This is brute force way in which this problem can be solved. In this, we
iterate through each string and replace specified character with empty string
to perform removal.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove character from Strings list

# using loop + replace() + enumerate()

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize character

char = 's'

 

# Remove character from Strings list

# using loop + replace() + enumerate()

for idx, ele in enumerate(test_list):

 test_list[idx] = ele.replace(char, '')

 

# printing result

print("The list after removal of character : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    The list after removal of character : ['gfg', 'i', 'bet', 'for', 'geek']
    

**Method #2 : Using list comprehension +replace()**  
This task can also be performed using above functionalities. In this, we offer
a one-liner solution to this problem compacting the code using similar method
as above.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove character from Strings list

# using list comprehension + replace()

 

# initialize list 

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list 

print("The original list : " + str(test_list))

 

# initialize character

char = 's'

 

# Remove character from Strings list

# using list comprehension + replace()

res = [ele.replace(char, '') for ele in test_list]

 

# printing result

print("The list after removal of character : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    The list after removal of character : ['gfg', 'i', 'bet', 'for', 'geek']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

