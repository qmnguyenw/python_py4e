set add() in python



The set add() method adds a given element to a set if the element is not
present in the set.

 **Syntax:**

    
    
    set.add(elem)
    The add() method doesn't add an element to the
    set if it's already present in it otherwise it 
    will get added to the set.
    **Parameters:**
    add() takes single parameter **(elem)** which needs to 
    be added in the set.
    **Returns:**
    The add() method doesn't return any value.
    

__

__  
__

__

__  
__  
__

# set of letters

GEEK = {'g', 'e', 'k'}

 

# adding 's'

GEEK.add('s')

print('Letters are:', GEEK)

 

# adding 's' again

GEEK.add('s')

print('Letters are:', GEEK)  
  
---  
  
 __

 __

Output:

    
    
    ('Letters are:', set(['k', 'e', 's', 'g']))
    ('Letters are:', set(['k', 'e', 's', 'g'])
    

**Application:**

    
    
    It is used to add a new element to the set. 
    

__

__  
__

__

__  
__  
__

# set of letters

GEEK = {6, 0, 4}

 

# adding 1

GEEK.add(1)

print('Letters are:', GEEK)

 

# adding 0 

GEEK.add(0)

print('Letters are:', GEEK)  
  
---  
  
 __

 __

Output:

  

  

    
    
    ('Letters are:', set([0, 1, 4, 6]))
    ('Letters are:', set([0, 1, 4, 6]))
    

**  
Adding tuple to a set:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate addition of tuple to a set.

s = {'g', 'e', 'e', 'k', 's'}

t = ('f', 'o')

 

# adding tuple t to set s.

s.add(t)

 

print(s)  
  
---  
  
 __

 __

Output :

    
    
    {'k', 's', 'e', 'g', ('f', 'o')}
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

