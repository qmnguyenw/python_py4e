Python – Maximum frequency in Tuple



Sometimes, while working with Python tuples, we can have a problem in which we
need to find the maximum frequency element in tuple. Tuple, being quite
popular container, this type of problems are common across web development
domain. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_tuple = (6, 7, 10, 11, 10)  
>  **Output** : 10
>
>  **Input** : test_tuple = (5, 5, 5)  
>  **Output** : 5

 **Method #1 : Usingcount() \+ loop**  
The combination of above functions can be used to solve this problem. This is
brute force approach to solve this problem. In this, we use count() to perform
counting of elements.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Maximum frequency in Tuple

# Using loop + count()

 

# initializing tuple

test_tuple = (6, 7, 8, 6, 7, 10)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Maximum frequency in Tuple

# Using loop + count()

cnt = 0

res = test_tuple[0] 

for ele in test_tuple: 

 curr_freq = test_tuple.count(ele) 

 if(curr_freq> cnt): 

 cnt = curr_freq 

 res = ele 

 

# printing result 

print("Maximum element frequency tuple : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : (6, 7, 8, 6, 7, 10)
    Maximum element frequency tuple : 6
    

