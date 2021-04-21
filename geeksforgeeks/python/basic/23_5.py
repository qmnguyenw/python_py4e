append() and extend() in Python



 **Append:** Adds its argument as a single element to the end of a list. The
length of the list increases by one.

    
    
    **syntax:** 
    # Adds an object (a number, a string or a 
    # another list) at the end of my_list
    my_list.append(object)
    

__

__  
__

__

__  
__  
__

my_list= ['geeks', 'for']

my_list.append('geeks')

print my_list  
  
---  
  
 __

 __

Output:

    
    
    ['geeks', 'for', 'geeks']
    

**NOTE:** A list is an object. If you append another list onto a list, the
parameter list will be a single object at the end of the list.

 __

 __  
 __

 __

 __  
 __  
 __

my_list= ['geeks', 'for', 'geeks']

another_list = [6, 0, 4, 1]

my_list.append(another_list)

print my_list  
  
---  
  
 __

 __

Output:

    
    
    ['geeks', 'for', 'geeks', [6, 0, 4, 1]]
    

  

  

**extend():** Iterates over its argument and adding each element to the list
and extending the list. The length of the list increases by number of elements
in it’s argument.

    
    
    **syntax:** 
    # Each element of an iterable gets appended 
    # to my_list
    my_list.extend(iterable) 
    

__

__  
__

__

__  
__  
__

my_list= ['geeks', 'for']

another_list = [6, 0, 4, 1]

my_list.extend(another_list)

print my_list  
  
---  
  
 __

 __

Output:

    
    
    ['geeks', 'for', 6, 0, 4, 1]
    

**NOTE:** A string is an iterable, so if you extend a list with a string,
you’ll append each character as you iterate over the string.

 __

 __  
 __

 __

 __  
 __  
 __

my_list= ['geeks', 'for', 6, 0, 4, 1]

my_list.extend('geeks')

print my_list  
  
---  
  
 __

 __

Output:

    
    
    ['geeks', 'for', 6, 0, 4, 1, 'g', 'e', 'e', 'k', 's']
    

**Time Complexity:**  
 **Append** has constant time complexity i.e.,O(1).  
 **Extend** has time complexity of O(k). Where k is the length of list which
need to be added.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

