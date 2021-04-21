Python – Insertion at the beginning in OrderedDict



Given an ordered dict, write a programm to insert items in beginning of
ordered dict.

 **Examples –**

    
    
    **Input:**
    original_dict = {'a':1, 'b':2}
    item to be inserted ('c', 3)
    
    **Output:** {'c':3, 'a':1, 'b':2}
    
    **Input:**
    original_dict = {'akshat':1, 'manjeet':2}
    item to be inserted ('nikhil', 3)
    
    **Output:** {'nikhil':3, 'akshat':1, 'manjeet':2}
    

Below are various methods to insert items in starting of ordered dict.

 **Method #1: UsingOrderedDict.move_to_end()**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# insertion of items in beginning of ordered dict

from collections import OrderedDict

 

# initialising ordered_dict

iniordered_dict = OrderedDict([('akshat', '1'), ('nikhil',
'2')])

 

# inserting items in starting of dict 

iniordered_dict.update({'manjeet':'3'})

iniordered_dict.move_to_end('manjeet', last = False)

 

# print result

print ("Resultant Dictionary : "+str(iniordered_dict))  
  
---  
  
 __

 __

 **Output:**

> Resultant Dictionary : OrderedDict([(‘manjeet’, ‘3’), (‘akshat’, ‘1’),
> (‘nikhil’, ‘2’)])

  
**Method #2: Using Naive Approach**

This method only works in case of unique keys

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# insertion of items in beginning of ordered dict

from collections import OrderedDict

 

# initialising ordered_dict

ini_dict1 = OrderedDict([('akshat', '1'), ('nikhil',
'2')])

ini_dict2 = OrderedDict([("manjeet", '4'), ("akash",
'4')])

 

# adding in beginning of dict

both = OrderedDict(list(ini_dict2.items()) +
list(ini_dict1.items()))

 

# print result

print ("Resultant Dictionary :"+str(both))  
  
---  
  
 __

 __

 **Output:**

> Resultant Dictionary :OrderedDict([(‘manjeet’, ‘4’), (‘akash’, ‘4’),
> (‘akshat’, ‘1’), (‘nikhil’, ‘2’)])

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

