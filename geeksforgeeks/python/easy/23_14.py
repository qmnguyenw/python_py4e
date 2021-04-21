Python Dictionary clear()



The clear() method removes all items from the dictionary.

 **Syntax:**

    
    
    dict.clear()
    

**Parameters:**

    
    
    The clear() method doesn't take any parameters.
    

**Returns:**

    
    
    The clear() method doesn't return any value.
    

**Examples:**

  

  

    
    
    Input : d = {1: "geeks", 2: "for"}
            d.clear()
    Output : d = {}
    

**Error:**

    
    
    As we are not passing any parameters there
    is no chance for any error.
    

__

__  
__

__

__  
__  
__

# Python program to demonstrate working of

# dictionary clear()

text = {1: "geeks", 2: "for"}

 

text.clear()

print('text =', text)  
  
---  
  
 __

 __

 **Output:**

    
    
    text = {}
    

**How is it different from assigning {} to a dictionary?**  
Please refer the below code to see the difference. When we assign {} to a
dictionary, a new empty dictionary is created and assigned to the reference.
But when we do clear on a dictionary reference, the actual dictionary content
is removed, so all references referring to the dictionary become empty.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate difference

# clear and {}.

 

text1 = {1: "geeks", 2: "for"}

text2 = text1

 

# Using clear makes both text1 and text2

# empty.

text1.clear()

 

print('After removing items using clear()')

print('text1 =', text1)

print('text2 =', text2)

 

text1 = {1: "one", 2: "two"}

text2 = text1

 

# This makes only text1 empty.

text1 = {}

 

print('After removing items by assigning {}')

print('text1 =', text1)

print('text2 =', text2)  
  
---  
  
 __

 __

Output:

    
    
    After removing items using clear()
    text1 = {}
    text2 = {}
    After removing items by assigning {}
    text1 = {}
    text2 = {1: 'one', 2: 'two'}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

