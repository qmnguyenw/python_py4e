Python – Consecutive Division in List



Given a List, perform consecutive division from each quotient obtained in the
intermediate step and treating consecutive elements as divisors.

>  **Input** : test_list = [1000, 50, 5, 10, 2]  
> **Output** : 0.2  
> **Explanation** : 1000 / 50 = 20 / 5 = 4 / 10 = 0.4 / 2 = 0.2. Hence
> solution.
>
>  **Input** : test_list = [100, 50]  
> **Output** : 2  
> **Explanation** : 100 / 50 = 2. Hence solution.  
>

**Approach: Using loop + “/” operator**

In this, we iterate for each element and store the quotient obtained to
process as a dividend for the next operation while in the loop. The end result
is the final quotient of list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Consecutive Division in List

# Using loop + / operator

 

# utility fnc.

def conc_div(test_list):

 

 res = test_list[0]

 for idx in range(1, len(test_list)):

 

 # Consecutive Division

 res /= test_list[idx]

 return res

 

# initializing list

test_list = [1000, 50, 5, 10, 2]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting conc. Division

res = conc_div(test_list)

 

# printing result 

print("The Consecutive Division quotient : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [1000, 50, 5, 10, 2]
    The Consecutive Division quotient : 0.2
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

