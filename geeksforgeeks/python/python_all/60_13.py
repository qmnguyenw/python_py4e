Python – Synchronized Split list with other



Sometimes, while working with Python data, we can have problem in which we
need to perform split of a String, which has mapping with an element on other
list, so need to perform mapping to different words formed due to split. This
type of problem is peculiar, but can have application in many domains. Let’S
discuss certain ways in which this task can be performed.

>  **Input** : test_list = [5, 6], str_list = [‘Gfg is best’, ‘I love Gfg’]  
>  **Output** : [5, 5, 5, 6, 6, 6]
>
>  **Input** : test_list = [5], str_list = [‘Gfg is best’]  
>  **Output** : [5, 5, 5]

 **Method #1 : Usingmap() + zip() + enumerate() + split()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of splitting values using split(), and corresponding
element mapping using zip() and map(). The iteration is carried using
enumerate().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Synchronized Split list with other

# Using map() + zip() + enumerate() + split()

 

# initializing list

test_list = [5, 6, 3, 7, 4] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing String list 

str_list = ['Gfg', 'is best', 'I love', 'Gfg', 'and
CS']

 

# Synchronized Split list with other

# Using map() + zip() + enumerate() + split()

temp = list(map(list, zip(*[(idx, sub) for idx, val
in

 enumerate(map(lambda x: x.split(), str_list), 1) for sub
in val])))

res = []

for ele in temp[0]:

 res.append(test_list[ele - 1])

 

# printing result 

print("Mapped list elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [5, 6, 3, 7, 4]
    Mapped list elements : [5, 6, 6, 3, 3, 7, 4, 4]
    

