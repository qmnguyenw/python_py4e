Python | Filter String with substring at specific position



Sometimes, while working with Python string lists, we can have a problem in
which we need to extract only those lists that have a specific substring at
specific position. This kind of problem can come in data processing and web
development domains. Lets discuss certain ways in which this task can be
performed.

 **Method #1 : Using list comprehension + list slicing**  
The combination of above functionalities can be used to perform this
particular task. In this, we check for substring range using list slicing and
task of extraction list is compiled in list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Filter String with substring at specific position

# using list comprehension + list slicing

 

# Initializing list

test_list = ['geeksforgeeks', 'is', 'best', 'for',
'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing substring

sub_str = 'geeks'

 

# Initializing range 

i, j = 0, 5

 

# Filter String with substring at specific position

# using list comprehension + list slicing

res = [ele for ele in test_list if ele[i: j] ==
sub_str]

 

# printing result 

print ("Filtered list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['geeksforgeeks', 'is', 'best', 'for', 'geeks']
    Filtered list : ['geeksforgeeks', 'geeks']
    

**Method #2 : Usingfilter() + lambda**  
The combination of above methods can be used to perform this task. In this, we
filter the elements using logic compiled using lambda using filter().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Filter String with substring at specific position

# using filter() + lambda

 

# Initializing list

test_list = ['geeksforgeeks', 'is', 'best', 'for',
'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing substring

sub_str = 'geeks'

 

# Initializing range 

i, j = 0, 5

 

# Filter String with substring at specific position

# using filter() + lambda

res = list(filter(lambda ele: ele[i: j] == sub_str,
test_list))

 

# printing result 

print ("Filtered list : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : ['geeksforgeeks', 'is', 'best', 'for', 'geeks']
    Filtered list : ['geeksforgeeks', 'geeks']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

