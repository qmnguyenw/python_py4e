Python – Maximum consecutive elements percentage change



Sometimes, while working with Python lists, we can have a problem in which we
need to extract the maximum change of consecutive elements. This kind of
problem can have application in domains such as Data Science. Let’s discuss
certain ways in which this task can be performed.

>  **Input** : test_list = [4, 6, 7]  
>  **Output** : 50.0
>
>  **Input** : test_list = [7, 7, 7, 7]  
>  **Output** : 0.0

 **Method #1 : Using loop + zip()**  
The combination of above functions can be used to solve this problem. In this,
we combine elements with its successive element using zip(). The loop is used
to perform computation in brute manner.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum consecutive elements percentage change

# Using zip() + loop

 

# initializing list

test_list = [4, 6, 7, 4, 2, 6, 2, 8]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Maximum consecutive elements percentage change

# Using zip() + loop

res = 0

for x, y in zip(test_list, test_list[1:]):

 res = max((abs(x - y) / x) * 100, res)

 

# printing result 

print("The maximum percentage change : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [4, 6, 7, 4, 2, 6, 2, 8]
    The maximum percentage change : 300.0
    

