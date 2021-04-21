Python – Row with Maximum Record Element



Sometimes, while working with Python Records, we can have a problem in which
we need to find the row with maximum record element. This kind of problem can
come in domains of web development and day-day programming. Let’s discuss
certain ways in which this task can be performed.

>  **Input** : test_list = [[(70, 4), (6, 7)], [(15, 2), (19, 3)]]  
>  **Output** : [(70, 4), (6, 7)]
>
>  **Input** : test_list = [[(20, 4)], [(15, 2)], [(34, 6)]]  
>  **Output** : [(34, 6)]

 **Method #1 : Using max() \+ key**  
The combination of above functions can be used to solve this problem. In this,
we extract maximum row using max() and key is used to check for initial
element of records.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Row with Maximum Record Element

# Using max() + key

 

# initializing list

test_list = [[(12, 4), (6, 7)], 

 [(15, 2), (19, 3)], 

 [(18, 3), (12, 4)], 

 [(17, 1), (11, 3)]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Row with Maximum Record Element

# Using max() + key

res = max(test_list, key = max)

 

# printing result 

print("The row with Maximum Value : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

> The original list is : [[(12, 4), (6, 7)], [(15, 2), (19, 3)], [(18, 3),
> (12, 4)], [(17, 1), (11, 3)]]  
> The row with Maximum Value : [(15, 2), (19, 3)]

