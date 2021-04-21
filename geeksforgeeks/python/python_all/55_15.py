Python – Order Tuples by List



Sometimes, while working with Python tuples, we can have a problem in which we
need to perform ordering of all the tuples keys using external list. This
problem can have application in data domains such as Data Science. Let’s
discuss certain ways in which this task can be performed.

>  **Input** : test_list = [(‘Gfg’, 10), (‘best’, 3), (‘CS’, 8), (‘Geeks’,
> 7)], ord_list = [‘Geeks’, ‘best’, ‘CS’, ‘Gfg’]  
>  **Output** : [(‘Geeks’, 7), (‘best’, 3), (‘CS’, 8), (‘Gfg’, 10)]
>
>  **Input** : test_list = [(‘best’, 3), (‘CS’, 8), (‘Geeks’, 7)], ord_list =
> [‘Geeks’, ‘best’, ‘CS’]  
>  **Output** : [(‘Geeks’, 7), (‘best’, 3), (‘CS’, 8)]

 **Method #1 : Usingdict() \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we perform this task by converting tuple list to dictionaries, and as a second
step use list comprehension to iterate through list and map the dictionary
keys with values.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Order Tuples by List

# Using dict() + list comprehension

 

# initializing list

test_list = [('Gfg', 3), ('best', 9), ('CS', 10),
('Geeks', 2)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing order list 

ord_list = ['Geeks', 'best', 'CS', 'Gfg']

 

# Order Tuples by List

# Using dict() + list comprehension

temp = dict(test_list)

res = [(key, temp[key]) for key in ord_list]

 

# printing result 

print("The ordered tuple list : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]
    The ordered tuple list : [('Geeks', 2), ('best', 9), ('CS', 10), ('Gfg', 3)]
    

