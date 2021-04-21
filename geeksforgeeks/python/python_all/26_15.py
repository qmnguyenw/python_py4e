Python Program to extracts elements from the list with digits in increasing
order



Given List of elements, extract all elements which have digits that are
increasing in order.

>  **Input** : test_list = [1234, 7373, 3643, 3527, 148, 49]  
> **Output** : [1234, 148, 49]  
> **Explanation** : All elements have increasing digits.  
>  **Input** : test_list = [12341, 7373, 3643, 3527, 1481, 491]  
> **Output** : []  
> **Explanation** : No elements have all increasing digits.

**Method 1 :** _Using_ _loop_ _and_ _str()_

In this, we convert each element to string and then check if their each digit
is greater than previous one using loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [1234, 7373, 3643, 3527, 148]

 

# printing original list

print("The original list is : " + str(test_list))

 

# loop to check for each element

res = []

for ele in test_list:

 flag = True

 

 for idx in range(len(str(ele)) - 1):

 

 # checking for each next digit

 if str(ele)[idx + 1] <= str(ele)[idx]:

 flag = False

 

 if flag:

 res.append(ele)

 

# printing result 

print("Extracted increasing digits : " + str(res))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list is : [1234, 7373, 3643, 3527, 148]
    Extracted increasing digits : [1234, 148]

 **Method 2 :** _Using_ _sorted()_ _,_ _list comprehension_ _and_ _str()_

In this, we test for each digit of an element to be increasing by sorting each
element and compare it with original version. If they are same, the element is
added to desired list.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [1234, 7373, 3643, 3527, 148]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sorting and comparing for equality

res = [ele for ele in test_list if
''.join(sorted(str(ele))) == str(ele)]

 

# printing result 

print("Extracted increasing digits : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1234, 7373, 3643, 3527, 148]
    Extracted increasing digits : [1234, 148]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

