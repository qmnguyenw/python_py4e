Python Dictionary copy()



They copy() method returns a shallow copy of the dictionary.

 **Syntax:**

    
    
    dict.copy()

 **Parameters:**

    
    
    The copy() method doesn't take any parameters.

 **Returns:**

    
    
    This method doesn't modify the original
    dictionary just returns copy of the dictionary.

Examples:

  

  

    
    
    Input : original = {1:'geeks', 2:'for'}
            new = original.copy()
    Output : original:  {1: 'one', 2: 'two'}
             new:  {1: 'one', 2: 'two'}
    

**Error:**

    
    
    As we are not passing any parameters 
    there is no chance of any error.
    

__

__  
__

__

__  
__  
__

# Python program to demonstrate working

# of dictionary copy

original = {1:'geeks', 2:'for'}

 

# copying using copy() function

new = original.copy()

 

# removing all elements from the list

# Only new list becomes empty as copy()

# does shallow copy.

new.clear()

 

print('new: ', new)

print('original: ', original)  
  
---  
  
 __

 __

 **Output:**

    
    
    new:  {}
    original:  {1: 'geeks', 2: 'for'}
    

**How is it different from simple assignment “=”?**  
Unlike copy(), the assignment operator does deep copy.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to demonstrate difference

# between = and copy()

original = {1:'geeks', 2:'for'}

 

# copying using copy() function

new = original.copy()

 

# removing all elements from new list

# and printing both

new.clear()

print('new: ', new)

print('original: ', original)

 

original = {1:'one', 2:'two'}

 

# copying using =

new = original

 

# removing all elements from new list

# and printing both

new.clear()

print('new: ', new)

print('original: ', original)  
  
---  
  
 __

 __

Output:

    
    
    new:  {}
    original:  {1: 'geeks', 2: 'for'}
    new:  {}
    original:  {}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

