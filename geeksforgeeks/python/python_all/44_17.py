Python – List Elements with given digit



Given list of elements and a digit K, extract all the numbers which contain K
digit.

>  **Input** : test_list = [56, 72, 875, 9, 173], K = 5  
>  **Output** : [56, 875]  
>  **Explanation** : 56 and 875 has “5” as digit, hence extrated.
>
>  **Input** : test_list = [56, 72, 875, 9, 173], K = 4  
>  **Output** : []  
>  **Explanation** : No number has 4 as digit.

 **Method #1 : Using list comprehension + str()**

This is one of the ways in which this task can be performed. In this, we
convert digit and element to string and then check if its inside that element.
The element iteration is done inside list comprehension to get one-liner
solution.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements with K digit

# Using list comprehension + str()

 

# initializing list

test_list = [56, 72, 875, 9, 173] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 7

 

# extracting all elements with digit K using 

# in operator after string conversion using str()

res = [ele for ele in test_list if str(K) in
str(ele)]

 

# printing result 

print("Elements with digit K : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [56, 72, 875, 9, 173]
    Elements with digit K : [72, 875, 173]
    
    

**Method #2 : Using filter() + lambda + str()**

This is yet another way to solve this problem. In this, we use filter() +
lambd along with str() to check conditionals and extract required elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements with K digit

# Using filter() + lambda + str()

 

# initializing list

test_list = [56, 72, 875, 9, 173] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K

K = 7

 

# using filter() and lambda to perform conditionals

# using str() to perform data type conversions

res = list(filter(lambda ele: str(K) in str(ele),
test_list))

 

# printing result 

print("Elements with digit K : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [56, 72, 875, 9, 173]
    Elements with digit K : [72, 875, 173]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

