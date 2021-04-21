Python program to find the string weight



Given a String, each character mapped with a weight( number), compute the
total weight of the string.

>  **Input** : test_str = ‘GeeksforGeeks’, {“G” : 1, “e” : 2, “k” : 5, “f” :
> 3, “s” : 15, “o” : 4, “r” : 6}  
> **Output** : 63  
> **Explanation** : 2 (G*2) + 8(e*4) + 30(s*2) + 10(k*2) + 4(o) + 6(r) +3(f) =
> 63.
>
>  **Input** : test_str = ‘Geeks’, {“G” : 1, “e” : 2, “k” : 5, “s” : 15}  
> **Output** : 25

**Method#1 : Using loop**

This is one of the ways in which this task can be performed. In this, we
iterate for all the characters and sum all the weights mapped from dictionary.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String Weight

# Using loop

 

# initializing string

test_str = 'GeeksforGeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing sum dictionary

sum_dict = {"G" : 5, "e" : 2, "k" : 10,

 "f" : 3, "s" : 15, "o" : 4, "r" : 6}

 

# refering dict for sum 

# iteration using loop

res = 0

for ele in test_str:

 res += sum_dict[ele]

 

# printing result 

print("The weighted sum : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : GeeksforGeeks
    The weighted sum : 81
    

**Method #2 : Using sum()**

This is one more way in which this task can be performed. In this, we use
generator expression, and sum() is used to compute the summation of individual
weights.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String Weight

# Using sum()

 

# initializing string

test_str = 'GeeksforGeeks'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing sum dictionary

sum_dict = {"G" : 5, "e" : 2, "k" : 10, "f" :
3, 

 "s" : 15, "o" : 4, "r" : 6}

 

# sum() used to get summation

res = sum(sum_dict[ele] for ele in test_str)

 

# printing result 

print("The weighted sum : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : GeeksforGeeks
    The weighted sum : 81
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

