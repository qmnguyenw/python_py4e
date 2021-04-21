Python – Alternate Elements operation on Tuple



Sometimes, while working with Python Tuples, we can have problem in which we
need to perform operations of extracted alternate chains of tuples. This kind
of operation can have application in many domains such as web development.
Lets discuss certain ways in which this task can be performed.

>  **Input** : test_tuple = (5, 6, 3)  
>  **Output** :  
> The alternate chain sum 1 : 6  
> The alternate chain sum 2 : 8
>
>  **Input** : test_tuple = (5, 6)  
>  **Output** :  
> The alternate chain sum 1 : 6  
> The alternate chain sum 2 : 5

 **Method #1 : Using loop +enumerate()**  
The combination of above functions provide brute force solution to this
problem. In this, we extract the elements along with indices using enumerate()
and perform chaining using condition.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate Elements operation on Tuple

# Using loop + enumerate()

 

# initializing tuple

test_tuple = (5, 6, 3, 6, 10, 34)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Alternate Elements operation on Tuple

# Using loop + enumerate()

sum1 = 0

sum2 = 0

for idx, ele in enumerate(test_tuple):

 if idx % 2:

 sum1 += ele

 else :

 sum2 += ele

 

# printing result 

print("The alternate chain sum 1 : " + str(sum1))

print("The alternate chain sum 2 : " + str(sum2))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original tuple : (5, 6, 3, 6, 10, 34)
    The alternate chain sum 1 : 46
    The alternate chain sum 2 : 18
    

