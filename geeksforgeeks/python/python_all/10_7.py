Python Program to convert Dictionary to List by Repeating keys corresponding
value times



Given a dictionary where keys are characters and their constituent values are
numbers, the task here is to write a python program that can convert it to a
list by repeating the key character value times.

>  **Input :** test_dict = {‘g’ : 2, ‘f’ : 3, ‘g’ : 1, ‘b’ : 4, ‘e’ : 1, ‘s’ :
> 4, ‘t’ : 3}
>
>  **Output :** [‘g’, ‘f’, ‘f’, ‘f’, ‘b’, ‘b’, ‘b’, ‘b’, ‘e’, ‘s’, ‘s’, ‘s’,
> ‘s’, ‘t’, ‘t’, ‘t’]
>
>  **Explanation :** f is added 3 times in list.
>
>  **Input :** test_dict = {‘g’ : 2, ‘f’ : 3, ‘g’ : 1, ‘b’ : 4, ‘e’ : 1}
>
>  
>
>
>  
>
>
>  **Output** : [‘g’, ‘f’, ‘f’, ‘f’, ‘b’, ‘b’, ‘b’, ‘b’, ‘e’]
>
>  **Explanation** : f is added 3 times in list.

 **Method 1 :** _Using_ _loop_ _and_ _* operator_

In this, elements are inserted using loop and occurrences are taken care using
* operator.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing dictionary

test_dict = {'g': 2, 'f': 3, 'g': 1, 'b':
4, 'e': 1, 's': 4, 't': 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

res = []

for key, val in test_dict.items():

 

 # getting values using * operator

 res += [key] * val

 

# printing result

print("The constructed list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘g’: 1, ‘f’: 3, ‘b’: 4, ‘e’: 1, ‘s’: 4, ‘t’:
> 3}
>
> The constructed list : [‘g’, ‘f’, ‘f’, ‘f’, ‘b’, ‘b’, ‘b’, ‘b’, ‘e’, ‘s’,
> ‘s’, ‘s’, ‘s’, ‘t’, ‘t’, ‘t’]
>
>  
>
>
>  
>

 **Method 2 :** _Using_ _list comprehension_

This uses nested loop approach using list comprehension as one liner to solve
this problem. Iterate the values as much as occurrence required.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing dictionary

test_dict = {'g': 2, 'f': 3, 'g': 1, 'b':
4, 'e': 1, 's': 4, 't': 3}

 

# printing original dictionary

print("The original dictionary is : " + str(test_dict))

 

# nested list comprehension to solve problem

res = [key for key, val in test_dict.items() for _ in
range(val)]

 

# printing result

print("The constructed list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

> The original dictionary is : {‘g’: 1, ‘f’: 3, ‘b’: 4, ‘e’: 1, ‘s’: 4, ‘t’:
> 3}
>
> The constructed list : [‘g’, ‘f’, ‘f’, ‘f’, ‘b’, ‘b’, ‘b’, ‘b’, ‘e’, ‘s’,
> ‘s’, ‘s’, ‘s’, ‘t’, ‘t’, ‘t’]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

