Python – Mapping Matrix with Dictionary



Given a Matrix, map its values with dictionary values.

>  **Input** : test_list = [[4, 2, 1], [1, 2, 3]], sub_dict = {1 : “gfg”, 2:
> “best”, 3 : “CS”, 4 : “Geeks”}  
>  **Output** : [[‘Geeks’, ‘best’, ‘gfg’], [‘gfg’, ‘best’, ‘CS’]]  
>  **Explanation** : Matrix elements are substituted using dictionary.
>
>  **Input** : test_list = [[4, 2, 1]], sub_dict = {1 : “gfg”, 2: “best”, 4 :
> “Geeks”}  
>  **Output** : [[‘Geeks’, ‘best’, ‘gfg’]]  
>  **Explanation** : Matrix elements are substituted using dictionary.

 **Method #1 : Using loop**

This is brute way in which this task can be performed. In this, we iterate for
all the elements of Matrix and map from dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mapping Matrix with Dictionary

# Using loop

 

# initializing list

test_list = [[4, 2, 1], [1, 2, 3], [4, 3,
1]]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing dictionary

sub_dict = {1 : "gfg", 2: "best", 3 : "CS", 4
: "Geeks"}

 

# Using loop to perform required mapping

res = []

for sub in test_list:

 temp = []

 for ele in sub:

 

 # mapping values from dictionary

 temp.append(sub_dict[ele])

 res.append(temp)

 

# printing result 

print("Converted Mapped Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[4, 2, 1], [1, 2, 3], [4, 3, 1]]
    Converted Mapped Matrix : [['Geeks', 'best', 'gfg'], ['gfg', 'best', 'CS'], ['Geeks', 'CS', 'gfg']]
    

**Method #2 : Using list comprehension**

This is yet another way in which this task can be performed. This is just
shorthand to above method.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mapping Matrix with Dictionary

# Using list comprehension

 

# initializing list

test_list = [[4, 2, 1], [1, 2, 3], [4, 3,
1]]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing dictionary

sub_dict = {1 : "gfg", 2: "best", 3 : "CS", 4
: "Geeks"}

 

# Using list comprehension to perform required mapping

# in one line 

res = [[sub_dict[val] for val in sub] for sub in
test_list]

 

# printing result 

print("Converted Mapped Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[4, 2, 1], [1, 2, 3], [4, 3, 1]]
    Converted Mapped Matrix : [['Geeks', 'best', 'gfg'], ['gfg', 'best', 'CS'], ['Geeks', 'CS', 'gfg']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

