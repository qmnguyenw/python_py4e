Python – Similar other index element of K



Given List of elements, other list and K, extract all the similar other list
index elements if element is K in List.

> Input : test_list = [6, 4, 6, 3, 6], arg_list = [7, 5, 4, 6, 3], K = 6
>
> Output : [7, 4, 3]
>
> Explanation : 7, 4 and 3 correspond to occurrences of 6 in first list.
>
> Input : test_list = [2, 3], arg_list = [4, 6], K = 3
>
>  
>
>
>  
>
>
> Output : [6]
>
> Explanation : 6 corresponds to only occurrence of 3.

 **Method #1 : Using enumerate() + list comprehension**

The combination of above methods provide a way in which this task can be
solved. In this, we check for like index from other list using enumerate() and
create new list using list comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Similar other index element if K

# Using list comprehension + enumerate()

 

# initializing list

test_list = [5, 7, 3, 2, 3, 8, 6]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing arg. list

arg_list = [4, 5, 8, 3, 7, 9, 3]

 

# initializing K

K = 3

 

# Using enumerate() to locate similar index in other list and extract
element

res = [ele for idx, ele in enumerate(arg_list) if
test_list[idx] == K]

 

# printing result

print("Extracted elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 7, 3, 2, 3, 8, 6]
    Extracted elements : [8, 7]
    
    

**Method #2 : Using list comprehension + zip()**

The combination of above functions can be used to solve this problem. In this,
we performing combining each element with other among both lists using zip().

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Similar other index element if K

# Using list comprehension + zip()

 

# initializing list

test_list = [5, 7, 3, 2, 3, 8, 6]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing arg. list

arg_list = [4, 5, 8, 3, 7, 9, 3]

 

# initializing K

K = 3

 

# Using zip() to lock both the lists, with similar indices mapping

res = [ele for ele, ele1 in zip(arg_list, test_list) if
ele1 == K]

 

# printing result

print("Extracted elements : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [5, 7, 3, 2, 3, 8, 6]
    Extracted elements : [8, 7]
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

