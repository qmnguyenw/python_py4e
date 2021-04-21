Python | Sort the items alphabetically from given dictionary



Given a dictionary, write a Python program to get the alphabetically sorted
items from given dictionary and print it. Let’s see some ways we can do this
task.

 **Code #1:** Using dict.items()

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort the items alphabetically from given dictionary

 

# initialising _dictionary 

dict = {'key1' : 'AGeek', 'key2' : 'For', 'key3':
'IsGeeks', 'key4': 'ZGeeks'} 

 

# printing iniial_dictionary 

print ("Original dictionary", str(dict)) 

 

# getting items in sorted order 

print ("\nItems in sorted order") 

for key, value in sorted(dict.items()): 

 print(value)   
  
---  
  
__

__

**Output:**

> Original dictionary {‘key4’: ‘ZGeeks’, ‘key2’: ‘For’, ‘key1’: ‘AGeek’,
> ‘key3’: ‘IsGeeks’}
>
> Items in sorted order  
> AGeek  
> For  
> IsGeeks  
> ZGeeks
>
>  
>
>
>  
>

**Code #2:** Using sorted()

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort the items alphabetically from given dictionary

 

# initialising _dictionary 

dict = {'key1' : 'AGeek', 'key2' : 'For', 'key3':
'IsGeeks', 'key4': 'ZGeeks'} 

 

# printing iniial_dictionary 

print ("Original dictionary", str(dict)) 

 

# getting items in sorted order 

print ("\nItems in sorted order") 

for key in sorted(dict): 

 print (dict[key])   
  
---  
  
__

__

**Output:**

> Original dictionary {‘key4’: ‘ZGeeks’, ‘key2’: ‘For’, ‘key1’: ‘AGeek’,
> ‘key3’: ‘IsGeeks’}
>
> Items in sorted order  
> AGeek  
> For  
> IsGeeks  
> ZGeeks

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

