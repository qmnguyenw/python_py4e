Python – Product and Inter Summation dictionary values



Sometimes, while working with Python dictionaries, we can have a problem in
which we need to perform product of entire value list and perform summation of
product of each list with other. This kind of application in web development
and day-day programming. Lets discuss certain ways in which this task can be
performed.

>  **Input** : test_dict = {‘gfg’ : [4], ‘is’ : [3], ‘best’ : [5]}  
>  **Output** : 60
>
>  **Input** : test_dict = {‘gfg’ : [0]}  
>  **Output** : 0

 **Method #1 : Usingzip() + map() + sum() \+ loop**  
The combination of above functions can be used to solve this problem. In this,
we perform the summation of values using sum(), the zip() binds all the
values. The map() is used to bind multiplication logic in all elements in
value list. All this is bound using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Product and Inter Summation dictionary values

# Using zip() + map() + sum() + loop 

 

# helper function

def mul(sub):

 res = 1

 for ele in sub:

 res *= int(ele)

 return res

 

# initializing dictionary

test_dict = {'gfg' : [4, 5, 6], 'is' : [1, 3,
4], 'best' : [7, 8, 9]}

 

# printing original dictionary

print("The original dictionary : " + str(test_dict))

 

# Product and Inter Summation dictionary values

# Using zip() + map() + sum() + loop 

temp = zip(*test_dict.values())

res = sum(map(mul, temp)) 

 

# printing result 

print("The summations of product : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original dictionary : {‘best’: [7, 8, 9], ‘is’: [1, 3, 4], ‘gfg’: [4, 5,
> 6]}  
> The summations of product : 364

