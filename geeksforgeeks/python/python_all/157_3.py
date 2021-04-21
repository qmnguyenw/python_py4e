Python | Remove last character in list of strings



Sometimes, we come across an issue in which we require to delete the last
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

# remove last character from list of strings

# using list comprehension + list slicing

 

# initializing list

test_list = ['Manjeets', 'Akashs', 'Akshats', 'Nikhils']

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + list slicing

# remove last character from list of strings

res = [sub[ : -1] for sub in test_list]

 

# printing result

print("The list after removing last characters : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Manjeets', 'Akashs', 'Akshats', 'Nikhils']
    The list after removing last characters : ['Manjeet', 'Akash', 'Akshat', 'Nikhil']
    

**Method #2 : Usingmap() \+ lambda**  
The map function can perform the task of getting the functionality executed
for all the members of list and lambda function performs the task of removal
of last element using list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# remove last character from list of strings

# using map() + lambda

 

# initializing list

test_list = ['Manjeets', 'Akashs', 'Akshats', 'Nikhils']

 

# printing original list 

print("The original list : " + str(test_list))

 

# using map() + lambda

# remove last character from list of strings

res = list(map(lambda i: i[ : -1], test_list))

 

# printing result

print("The list after removing last characters : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['Manjeets', 'Akashs', 'Akshats', 'Nikhils']
    The list after removing last characters : ['Manjeet', 'Akash', 'Akshat', 'Nikhil']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

