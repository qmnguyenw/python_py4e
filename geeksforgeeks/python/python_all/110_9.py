Python – Remove Initial character in String List



Sometimes, we come across an issue in which we require to delete the initial
character from each string, that we might have added by mistake and we need to
extend this to the whole list. This type of utility is common in web
development. Having shorthands to perform this particular job is always a
plus. Let’s discuss certain ways in which this can be achieved.

 **Method #1 : Using list comprehension + list slicing**  
This task can be performed by using the ability of list slicing to remove the
characters and the list comprehension helps in extending that logic to whole
list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove Initial character in String List

# using list comprehension + list slicing

 

# initializing list

test_list = ['Amanjeet', 'sakash', 'kakshat', 'Knikhil']

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + list slicing

# Remove Initial character in String List

res = [sub[1 : ] for sub in test_list]

 

# printing result

print("The list after removing initial characters : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Amanjeet', 'sakash', 'kakshat', 'Knikhil']
    The list after removing initial characters : ['manjeet', 'akash', 'akshat', 'nikhil']
    

**Method #2 : Usingmap() \+ lambda**  
The map function can perform the task of getting the functionality executed
for all the members of list and lambda function performs the task of removal
of initial element using list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Remove Initial character in String List

# using map() + lambda

 

# initializing list

test_list = ['Amanjeet', 'sakash', 'kakshat', 'Knikhil']

 

# printing original list 

print("The original list : " + str(test_list))

 

# using map() + lambda

# Remove Initial character in String List

res = list(map(lambda i: i[ 1 : ], test_list))

 

# printing result

print("The list after removing initial characters : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Amanjeet', 'sakash', 'kakshat', 'Knikhil']
    The list after removing initial characters : ['manjeet', 'akash', 'akshat', 'nikhil']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

