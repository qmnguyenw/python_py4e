Python – Convert List of Lists to Tuple of Tuples



Sometimes, while working with Python data, we can have a problem in which we
need to perform interconversion of data types. This kind of problem can occur
in domains in which we need to get data in particular formats such as Machine
Learning. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_list = [[‘Best’], [‘Gfg’], [‘Gfg’]]  
>  **Output** : ((‘Best’, ), (‘Gfg’, ), (‘Gfg’, ))
>
>  **Input** : test_list = [[‘Gfg’, ‘is’, ‘Best’]]  
>  **Output** : ((‘Gfg’, ‘is’, ‘Best’), )

 **Method #1 : Usingtuple() \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we perform the conversion using tuple() and list comprehension is used to
extend logic to all the containers.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert List of Lists to Tuple of Tuples

# Using tuple + list comprehension

 

# initializing list

test_list = [['Gfg', 'is', 'Best'], ['Gfg', 'is',
'love'],

 ['Gfg', 'is', 'for', 'Geeks']]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert List of Lists to Tuple of Tuples

# Using tuple + list comprehension

res = tuple(tuple(sub) for sub in test_list)

 

# printing result 

print("The converted data : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [[‘Gfg’, ‘is’, ‘Best’], [‘Gfg’, ‘is’, ‘love’],
> [‘Gfg’, ‘is’, ‘for’, ‘Geeks’]]  
> The converted data : ((‘Gfg’, ‘is’, ‘Best’), (‘Gfg’, ‘is’, ‘love’), (‘Gfg’,
> ‘is’, ‘for’, ‘Geeks’))

