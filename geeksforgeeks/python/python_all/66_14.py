Python – Remove keys with substring values



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to remove keys whose values have substring as argument we pass.
This problem can occur in cases of web development and day-day programming.
Lets discuss certain ways in which this task can be performed.

>  **Input** :  
> test_dict = {1 : ‘Gfg is best for geeks’}  
> sub_list = [‘love’, ‘good’] ( Strings to check in values )  
>  **Output** : {1: ‘Gfg is best for geeks’}
>
>  **Input** :  
> test_dict = {1 : ‘Gfg is love’, 2: ‘Gfg is good’}  
> sub_list = [‘love’, ‘good’] ( Strings to check in values )  
>  **Output** : {}

 **Method #1 : Usingany() \+ loop**  
The combination of above functionalities can be used to solve this problem. In
this, we extract all the items from dictionary which do not have desired
values, the filteration is performed using any() and generator expression.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove keys with substring values

# Using any() + generator expression

 

# initializing dictionary

test_dict = {1 : 'Gfg is best for geeks', 2 : 'Gfg is
good', 3 : 'I love Gfg'}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# initializing substrings

sub_list = ['love', 'good']

 

# Remove keys with substring values

# Using any() + generator expression

res = dict()

for key, val in test_dict.items():

 if not any(ele in val for ele in sub_list):

 res[key] = val

 

# printing result 

print("Filtered Dictionary : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {1: ‘Gfg is best for geeks’, 2: ‘Gfg is good’, 3:
> ‘I love Gfg’}  
> Filtered Dictionary : {1: ‘Gfg is best for geeks’}

