Python | Sort each String in String list



Sometimes, while working with Python, we can have a problem in which we need
to perform the sort operation in all the Strings that are present in a list.
This problem can occur in general programming and web development. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Using list comprehension +sorted() + join()**  
This is one way in which this problem can be solved. In this, we use sorted()
functionality to perform sort operation and join() is used to reconstruct the
string list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings in String list

# using list comprehension + sorted() + join()

 

# initialize list 

test_list = ['gfg', 'is', 'good']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Sort Strings in String list

# using list comprehension + sorted() + join()

res = [''.join(sorted(ele)) for ele in test_list]

 

# printing result

print("List after string sorting : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'good']
    List after string sorting : ['fgg', 'is', 'dgoo']
    

**Method #2 : Usingmap() + sorted() + join() \+ lambda**  
The combination of above method can also be used to perform this task. In
this, we perform the functionality of traversal using map() and lambda rather
than list comprehension.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort Strings in String list

# using map() + sorted() + join() + lambda

 

# initialize list 

test_list = ['gfg', 'is', 'good']

 

# printing original list 

print("The original list : " + str(test_list))

 

# Sort Strings in String list

# using map() + sorted() + join() + lambda

res = list(map(lambda ele: "".join(sorted(ele)),
test_list))

 

# printing result

print("List after string sorting : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : ['gfg', 'is', 'good']
    List after string sorting : ['fgg', 'is', 'dgoo']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

