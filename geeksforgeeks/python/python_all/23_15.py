Python program to extract only the numbers from a list which have some
specific digits



Given Elements List, extract numbers with specific digits.

> **Input** : test_list = [3456, 23, 128, 235, 982], dig_list = [2, 3, 5, 4]  
> **Output** : [23, 235]  
> **Explanation** : 2, 3 and 2, 3, 5 are in digit list, hence extracted
> elements.  
>  **Input** : test_list = [3456, 23, 28, 235, 982], dig_list = [2, 3, 5, 4,
> 8]  
> **Output** : [23, 28, 235]  
> **Explanation** : 2, 3; 2, 8 and 2, 3, 5 are in digit list, hence extracted
> elements.

**Method #1 : Using** **list comprehension** **+** **all()**

In this, we check for each element in number against the elements from target
list to be present, if all are found in list, element is returned.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements with specific digits

# Using list comprehension + all()

 

# initializing list

test_list = [345, 23, 128, 235, 982]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing digit list 

dig_list = [2, 3, 5, 4]

 

# checking for all digits using all()

res = [sub for sub in test_list if all(int(ele) in
dig_list for ele in str(sub))]

 

# printing result 

print("Extracted elements : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list is : [345, 23, 128, 235, 982]
    Extracted elements : [345, 23, 235]

 **Method #2 : Using** **filter()** **+** **lambda** **\+ all()**

In this, filtering of elements is done using filter() + lambda, all() is used
to check for all the digits from other list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements with specific digits

# Using filter() + lambda + all()

 

# initializing list

test_list = [345, 23, 128, 235, 982]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing digit list 

dig_list = [2, 3, 5, 4]

 

# filter() used to filter from logic 

res = list(filter(lambda sub : all(int(ele) in
dig_list for ele in str(sub)), test_list))

 

# printing result 

print("Extracted elements : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [345, 23, 128, 235, 982]
    Extracted elements : [345, 23, 235]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

