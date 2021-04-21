Python – Extract elements with equal frequency as value



Given a list, extract all the elements having same frequency as its value.

 **Examples:**

>  **Input** : test_list = [4, 3, 2, 2, 3, 4, 1, 3, 2, 4, 4]  
> **Output** : [1, 3, 4]  
> **Explanation** : All elements occur equal times as their value.  
>
>
> **Input** : test_list = [4, 3, 2, 2, 3, 4, 1, 3, 2, 4]  
> **Output** : [1, 3]  
> **Explanation** : All elements occur equal times as their value.

**Method #1 : Using** **list comprehension** **+** **count()**

  

  

In this, task of getting frequency is done using count(), list comprehension
is used to iterate for each element, compare and extract.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract elements with equal frequency as value

# Using list comprehension + count()

 

# initializing list

test_list = [4, 3, 2, 2, 3, 4, 1, 3,
2, 4, 4]

 

# printing original list

print("The original list is : " + str(test_list))

 

# removing duplicates using set()

# count() for computing frequency

res = list(set([ele for ele in test_list if
test_list.count(ele) == ele]))

 

# printing result 

print("Filtered elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 3, 2, 2, 3, 4, 1, 3, 2, 4, 4]
    Filtered elements : [1, 3, 4]
    

**Method #2 : Using** **filter()** **+** **lambda** **\+ count()**

In this, we perform task of filtering elements using filter() and lambda,
count() again is used to get count of all the elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Extract elements with equal frequency as value

# Using filter() + lambda + count()

 

# initializing list

test_list = [4, 3, 2, 2, 3, 4, 1, 3,
2, 4, 4]

 

# printing original list

print("The original list is : " + str(test_list))

 

# removing duplicates using set()

# count() for computing frequency

# filter used to perform filtering 

res = list(set(list(filter(lambda ele :
test_list.count(ele) == ele, test_list))))

 

# printing result 

print("Filtered elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4, 3, 2, 2, 3, 4, 1, 3, 2, 4, 4]
    Filtered elements : [1, 3, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

