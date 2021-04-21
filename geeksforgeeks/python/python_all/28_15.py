Python – Sort by Units Digit in List



Given a Integer list, sort by unit digits.

> **Input** : test_list = [76, 434, 23, 22342]  
> **Output** : [22342, 23, 434, 76]  
> **Explanation** : 2 < 3 < 4 < 6, sorted by unit digits.
>
>  **Input** : test_list = [76, 4349, 23, 22342]  
> **Output** : [22342, 23, 76, 4349]  
> **Explanation** : 2 < 3 < 6 < 9, sorted by unit digits.

**Method #1 : Using sort() + str()**

In this, we perform sort using _sort()_ and _str()_ is used to convert
integers to string, and then sort by last digit.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Units Digit in List

# Using sort() + str()

 

# helpr_fnc to sort

 

 

def unit_sort(ele):

 

 # get last element

 return str(ele)[-1]

 

 

# initializing lists

test_list = [76, 434, 23, 22342]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# inplace sort by unit digits

test_list.sort(key=unit_sort)

 

# printing result

print("The unit sorted list : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [76, 434, 23, 22342]
    The unit sorted list : [22342, 23, 434, 76]
    

**Method #2 : Using sorted() + lambda + str()**

In this, we perform task of sorting using _sorted()_ and lambda function is
used to avoid external function call.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Units Digit in List

# Using sorted() + lambda + str()

 

# initializing lists

test_list = [76, 434, 23, 22342]

 

# printing original lists

print("The original list is : " + str(test_list))

 

# inplace sort by unit digits

res = sorted(test_list, key=lambda sub: str(sub)[-1])

 

# printing result

print("The unit sorted list : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [76, 434, 23, 22342]
    The unit sorted list : [22342, 23, 434, 76] 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

