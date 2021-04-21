Python – Average digits count in a List



Given a list of elements extract the average digit count in List.

>  **Input** : test_list = [34, 2345, 23, 456, 2, 23, 456787]  
> **Output** : 2.857142857142857  
> **Explanation** : Average of all digit count. [2+4+2+3+1+2+6 = 20, 20/7 =
> 2.857142857142857]
>
>  **Input** : test_list = [34, 1, 456]  
>  **Output** : 2.0  
> **Explanation** : Average of all digit count. [1 + 2 + 3 = 6, 6 / 3 = 2]  
>

**Method #1 : Using** **len()** **\+ loop +** **str()**

In this, we iterate each element, convert to string, and find its length,
perform summation using counter, and then divide the result with the total
element in the list to get results.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Average digits count

# Using len() + loop + str()

 

# initializing list

test_list = [34, 2345, 23, 456, 2, 23,
456787]

 

# printing original list

print("The original list is : " + str(test_list))

 

sumd = 0

for ele in test_list:

 

 # summing digits length 

 sumd += len(str(ele))

 

# getting result after dividing total digits by elements 

res = sumd / len(test_list)

 

# printing result 

print("Average digits length : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [34, 2345, 23, 456, 2, 23, 456787]
    Average digits length : 2.857142857142857
    

**Method #2 : Using len() +** **sum()** **\+ str()**

In this, the task of getting a sum is done using sum(), extends a compact way
to solve the problem.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Average digits count

# Using len() + sum() + str()

 

# initializing list

test_list = [34, 2345, 23, 456, 2, 23,
456787]

 

# printing original list

print("The original list is : " + str(test_list))

 

# getting summation and dividing by total length

res = sum([len(str(ele)) for ele in test_list]) /
len(test_list)

 

# printing result 

print("Average digits length " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [34, 2345, 23, 456, 2, 23, 456787]
    Average digits length 2.857142857142857
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

