Python – Get Even indexed elements in Tuple



Sometimes, while working with Python data, one can have a problem in which we
need to perform the task of extracting just even indexed elements in tuples.
This kind of problem is quite common and can have possible application in many
domains such as day-day programming. Let’s discuss certain ways in which this
task can be performed.

>  **Input** : test_tuple = (1, 2, 4, 5, 6)  
>  **Output** : (1, 4, 6)
>
>  **Input** : test_tuple = (1, 2, 4)  
>  **Output** : (1, 4)

 **Method #1 : Usingtuple() + generator expression + enumerate()**  
The combination of above functions can be used to solve this problem. In this,
we perform task of iteration using generator expression, checking for even
index using enumerate() and converting result to tuple using tuple().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract Even indexed elements in Tuple

# Using tuple() + generator expression + enumerate()

 

# initializing tuples

test_tuple = (5, 'Gfg', 2, 8.8, 1.2, 'is')

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Extract Even indexed elements in Tuple

# Using tuple() + generator expression + enumerate()

res = tuple(ele for idx, ele in enumerate(test_tuple) if
idx % 2 == 0)

 

# printing result 

print("The even indexed elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : (5, 'Gfg', 2, 8.8, 1.2, 'is')
    The even indexed elements : (5, 2, 1.2)
    

