Python – Alternate List elements



Given 2 lists, print element in zig-zag manner, i.e print similar indices of
lists and then proceed to next.

>  **Input** : test_list1 = [5, 3, 1], test_list2 = [6, 4, 2]  
>  **Output** : [5, 6, 3, 4, 1, 2, 4]  
>  **Explanation** : 5 and 6, as in 0th index are printed first, then 3 and 4
> on 1st index, and so on.
>
>  **Input** : test_list1 = [5, 3, 1, 9], test_list2 = [6, 4, 2, 10]  
>  **Output** : [5, 6, 3, 4, 1, 2, 4, 9, 10]  
>  **Explanation** : 5 and 6, as in 0th index are printed first, then 3 and 4
> on 1st index, and so on.

 **Method #1 : Using loop**

This is one of the ways in which this task can be performed. In this we
plainly perform iteration and append the similar index elements one after
another in result list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate List elements

# Using loop

 

# initializing lists

test_list1 = [5, 3, 1, 4, 7]

test_list2 = [6, 4, 2, 5, 1]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Using loop to print elements in criss cross manner

res = []

for idx in range(0, len(test_list1)):

 res.append(test_list1[idx])

 res.append(test_list2[idx])

 

# printing result

print("The zig-zag printing of elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [5, 3, 1, 4, 7]
    The original list 2 : [6, 4, 2, 5, 1]
    The zig-zag printing of elements : [5, 6, 3, 4, 1, 2, 4, 5, 7, 1]
    

**Method #2 : Using zip() + loop**

The combination of above functions can be used to solve this problem. In this,
we pair each element with similar index using zip() and then each element is
fed into result list using loop.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Alternate List elements

# Using zip() + loop

 

# initializing lists

test_list1 = [5, 3, 1, 4, 7]

test_list2 = [6, 4, 2, 5, 1]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Using zip() to perform pairing and loop to 

# get elements into result list

res = []

for ele1, ele2 in zip(test_list1, test_list2):

 res.append(ele1)

 res.append(ele2)

 

# printing result 

print("The zig-zag printing of elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : [5, 3, 1, 4, 7]
    The original list 2 : [6, 4, 2, 5, 1]
    The zig-zag printing of elements : [5, 6, 3, 4, 1, 2, 4, 5, 7, 1]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

