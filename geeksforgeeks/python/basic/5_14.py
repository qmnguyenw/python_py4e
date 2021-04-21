Remove all the occurrences of an element from a list in Python



The task is to perform the operation of removing all the occurrences of a
given item/element present in a list.

 **Examples :**

>  **Input :**  
>  1 1 2 3 4 5 1 2  
> 1  
>  **Output :**  
>  2 3 4 5 2
>
>  **Explanation :** The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item
> to be removed is 1.  
> After removing the item, the output list is [2, 3, 4, 5, 2]
>
>  **Input :**  
>  5 6 7 8 9 10  
> 7  
>  **Output :**  
>  5 6 8 9 10
>
>  
>
>
>  
>

In this article, we shall see how to execute this task in 3 ways :

  1. Using list comprehension
  2. Using filter() and __ne__
  3. Using remove()

 **Method 1 :** Using list comprehension  
The list comprehension can be used to perform this task in which we just check
for a match and reconstruct the list without the target element. We can create
a sublist of those elements in the list that satisfies a certain condition.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# the removal of all occurrences of a 

# given item using list comprehension

 

def remove_items(test_list, item):

 

 # using list comprehension to perform the task

 res = [i for i in test_list if i != item]

 

 return res

 

# driver code

if __name__=="__main__":

 

 # initializing the list

 test_list = [1, 3, 4, 6, 5, 1]

 

 # the item which is to be removed

 item = 1

 

 # printing the original list

 print ("The original list is : " + str(test_list))

 

 # calling the function remove_items()

 res = remove_items(test_list, item)

 

 # printing result

 print ("The list after performing the remove operation is : " +
str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [1, 3, 4, 6, 5, 1]
    The list after performing the remove operation is : [3, 4, 6, 5]
    

**Method 2 :** Using filter() and __ne__  
We filter those items of the list which are not equal __ne__ to the item.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# the removal of all occurrences of

# a given item using filter() and __ne__

 

def remove_items(test_list, item):

 

 # using filter() + __ne__ to perform the task

 res = list(filter((item).__ne__, test_list))

 

 return res

 

# driver code

if __name__=="__main__":

 

 # initializing the list

 test_list = [1, 3, 4, 6, 5, 1]

 

 # the item which is to be removed

 item = 1

 

 # printing the original list

 print ("The original list is : " + str(test_list))

 

 # calling the function remove_items()

 res = remove_items(test_list, item)

 

 # printing result

 print ("The list after performing the remove operation is : " +
str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [1, 3, 4, 6, 5, 1]
    The list after performing the remove operation is : [3, 4, 6, 5]
    

**Method 3 :** Using remove()  
In this method, we iterate through each item in the list, and when we find a
match for the item to be removed, we will call remove() function on the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# the removal of all occurrences of

# a given item using remove()

 

def remove_items(test_list, item):

 

 # remove the item for all its occurrences

 for i in test_list:

 if(i == item):

 test_list.remove(i)

 

 return test_list

 

# driver code

if __name__=="__main__":

 

 # initializing the list

 test_list = [1, 3, 4, 6, 5, 1]

 

 # the item which is to be removed

 item = 1

 

 # printing the original list

 print ("The original list is : " + str(test_list))

 

 # calling the function remove_items()

 res = remove_items(test_list, item)

 

 # printing result

 print ("The list after performing the remove operation is : " +
str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [1, 3, 4, 6, 5, 1]
    The list after performing the remove operation is : [3, 4, 6, 5]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

