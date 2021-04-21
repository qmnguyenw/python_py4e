Python – Sort by Rear Character in Strings List



Given a String list, perform sort by the rear character in Strings list.

>  **Input** : test_list = [‘gfg’, ‘is’, ‘for’, ‘geeks’]  
> **Output** : [‘gfg’, ‘for’, ‘is’, ‘geeks’]  
> **Explanation** : g < r < s = s, hence the order.
>
>  **Input** : test_list = [‘gfz’, ‘is’, ‘for’, ‘geeks’]  
> **Output** : [‘for’, ‘is’, ‘geeks’, ‘gfz’]  
> **Explanation** : r < s = s < z, hence the order.

**Method #1 : Using sort()**

In this, we perform the task of sorting using sort(), and external function is
used for the task of getting the rear element in string.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Rear Character in Strings List

# Using sort()

 

# sort key fnction

def get_rear(sub):

 return sub[-1]

 

# initializing list

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# using sort with key fnc. 

# performs inplace sort

test_list.sort(key = get_rear)

 

# printing result 

print("Sorted List : " + str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    Sorted List : ['gfg', 'for', 'is', 'geeks', 'best']
    

**Method #2 : Using** **sorted()** **+** **lambda**

In this, we use sorted() for performing sort, explicit, and use a lambda
function to perform the task of getting the rear element.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort by Rear Character in Strings List

# Using sorted() + lambda

 

# initializing list

test_list = ['gfg', 'is', 'best', 'for', 'geeks']

 

# printing original list

print("The original list is : " + str(test_list))

 

# lambda function for rear element 

# performs non-inplace sort

res = sorted(test_list, key = lambda sub : sub[-1])

 

# printing result 

print("Sorted List : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : ['gfg', 'is', 'best', 'for', 'geeks']
    Sorted List : ['gfg', 'for', 'is', 'geeks', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

