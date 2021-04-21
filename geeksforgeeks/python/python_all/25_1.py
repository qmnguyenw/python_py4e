Python – Sort by a partciular digit count in elements



Given a list of elements, sort by K digit in each element.

 **Examples:**

>  **Input** : test_list = [4322, 2122, 123, 1344], K = 2  
> **Output** : [1344, 123, 4322, 2122]  
> **Explanation** : 0 < 1 < 2 < 3, sorted by count of 2 in each element.
>
>  **Input** : test_list = [4322, 2122, 1344], K = 2  
> **Output** : [1344, 4322, 2122]  
> **Explanation** : 0 < 2 < 3, sorted by count of 2 in each element.

**Method #1: Using** **list comprehension** **+** **str()** **+** **count()**

  

  

In this, we perform the task of sorting using sort(), and the task of finding
frequency is done using count().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by digit count in elements

# Using list comprehension + count() + str()

 

def count_dig(ele):

 

 # returning digit count

 return str(ele).count(str(K))

 

# initializing list

test_list = [4322, 2122, 123, 1344]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# calling external sort

test_list.sort(key = count_dig)

 

# printing result 

print("Sorted list : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4322, 2122, 123, 1344]
    Sorted list : [1344, 123, 4322, 2122]
    

**Method #2 : Using** **sorted()** **\+ str() + count() +** **lambda**

In this, we perform the task of performing sort using sorted(), and use the
lambda fnction to get sort logic rather than the external function.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by digit count in elements

# Using sorted() + str() + count() + lambda

 

# initializing list

test_list = [4322, 2122, 123, 1344]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing K 

K = 2

 

# sorting using sorted()

# not inplace sort.

res = sorted(test_list, key = lambda ele :
str(ele).count(str(K)))

 

# printing result 

print("Sorted list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [4322, 2122, 123, 1344]
    Sorted list : [1344, 123, 4322, 2122]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

