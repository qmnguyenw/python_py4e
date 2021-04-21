Python – Convert Index Dictionary to List



Sometimes, while working with Python dictionaries, we can have a problem in
which we have keys mapped with values, where keys represent list index where
value has to be placed. This kind of problem can have application in all data
domains such as web development. Let’s discuss certain ways in which this task
can be performed.

>  **Input** : test_dict = { 1 : ‘Gfg’, 3 : ‘is’, 5 : ‘Best’ }  
>  **Output** : [0, ‘Gfg’, 0, ‘is’, 0, ‘Best’, 0, 0, 0, 0, 0]
>
>  **Input** : test_dict = { 2 : ‘Gfg’, 6 : ‘Best’ }  
>  **Output** : [0, 0, ‘Gfg’, 0, 0, 0, ‘Best’, 0, 0, 0, 0]

 **Method #1 : Usinglist comprehension + keys()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of assigning values to list checking for index, by
extracting keys of dictionary for lookup.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Index Dictionary to List

# Using list comprehension + keys()

 

# initializing dictionary

test_dict = { 2 : 'Gfg', 4 : 'is', 6 : 'Best' } 

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# Convert Index Dictionary to List

# Using list comprehension + keys()

res = [test_dict[key] if key in test_dict.keys() else 0
for key in range(10)]

 

# printing result 

print("The converted list : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original dictionary is : {2: 'Gfg', 4: 'is', 6: 'Best'}
    The converted list : [0, 0, 'Gfg', 0, 'is', 0, 'Best', 0, 0, 0]
    

