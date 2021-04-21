Python – Sort on basis of reverse Strings



Given a String list, sort list on basis of reverse of strings.

>  **Input** : test_list = [“gfg”, “is”, “best”, “geeks”]  
>  **Output** : [‘gfg’, ‘is’, ‘geeks’, ‘best’]  
>  **Explanation** : g < is < ks < t [elements from rear], hence the order.
>
>  **Input** : test_list = [“gfg”, “is”, “best”]  
>  **Output** : [‘gfg’, ‘is’, ‘best’]  
>  **Explanation** : g < s < t [elements from rear], hence the order.

 **Method #1 : Using sort() + reverse()**

This is one of the ways in which this task can be performed. In this, we first
reverse each element, perform sort and then again reverse each string to get
resultant ordering.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort on basis of reverse Strings

# Using reverse() + sort()

 

# initializing list

test_list = ["gfg", "is", "best", "for", "geeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# reverse() to reverse each string 

res = []

for ele in test_list:

 res.append("".join(reversed(ele))) 

 

# sorting to get required ordering 

res.sort()

 

# reverse each element again

test_list = []

for ele in res:

 test_list.append("".join(reversed(ele))) 

 

# printing result 

print("List after sorting on reversed strings : " +
str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    List after sorting on reversed strings : ['gfg', 'for', 'is', 'geeks', 'best']
    

**Method #2 : Using list slicing + sort()**

This is yet another way in which this task can be performed. in this list
slicing is used to perform reverse operation and sort() is used to sort, in
one liner.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort on basis of reverse Strings

# Using list slicing + sort()

 

# initializing list

test_list = ["gfg", "is", "best", "for", "geeks"]

 

# printing original list

print("The original list : " + str(test_list))

 

# [::-1] to reverse each string 

# sort() to sort

test_list.sort(key = lambda sub: sub[::-1])

 

# printing result 

print("List after sorting on reversed strings : " +
str(test_list))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : ['gfg', 'is', 'best', 'for', 'geeks']
    List after sorting on reversed strings : ['gfg', 'for', 'is', 'geeks', 'best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

