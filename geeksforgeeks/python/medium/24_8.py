Sort the values of first list using second list in Python



Given two lists, sort the values of one list using the second list.  

**Examples:**

    
    
    Input : list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
            list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
    
    Output :['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']
    
    
    Input : list1 = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
            list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
    
    Output : ['g', 'k', 'r', 'e', 'e', 'g', 's', 'f', 'o']
    
    
    
    
    
    
    

Recommended: Please try your approach on _**_{IDE}_**_ first, before moving on
to the solution.

 **Approach :**  

  1. Zip the two lists.
  2. Create a new, sorted list based on the zip using sorted().
  3. Using a list comprehension extract the first elements of each pair from the sorted, zipped list.

 **Concept :**  
The purpose of zip() is to map a similar index of multiple containers so that
they can be used just using as a single entity.  
Below is the implementation of the above approach:  

  

  

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to sort

# one list using

# the other list

def sort_list(list1, list2):

 zipped_pairs = zip(list2, list1)

 z = [x for _, x in sorted(zipped_pairs)]

 

 return z

 

# driver code

x = ["a", "b", "c", "d", "e", "f", "g",
"h", "i"]

y = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sort_list(x, y))

x = ["g", "e", "e", "k", "s", "f", "o",
"r", "g", "e", "e", "k", "s"]

y = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sort_list(x, y))  
  
---  
  
 __

 __

 **Output:**  

    
    
    ['a', 'd', 'h', 'b', 'c', 'e', 'i', 'f', 'g']
    ['g', 'k', 'r', 'e', 'e', 'g', 's', 'f', 'o']
    
    
    
    
    
    
    

In the above code, we have two lists, the first list is being sorted with
respect to the values of the second list.  

    
    
    y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
    
    
    
    
    
    

Here first the lowest value is checked. Like in this list, 0 is the lowest, so
starting from the first index, 0 is the lowest and it is at index 0. So the
value of index 0 is stored at index 0 in the first list. Similarly, 0 is again
found at index 3 and so the value of index 3 in the first list is index 1. The
same goes until the list is not completed.  

**Approach 2: By using Dictionary, list comprehension, lambda function**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def sorting_of_element(list1,list2):

 

 # initializing blank dictionary

 f_1 = {}

 

 # initializing blank list

 final_list = []

 

 # Addition of two list in one dictionary

 f_1 = {list1[i]: list2[i] for i in range(len(list2))}

 

 # sorting of dictionary based on value

 f_lst = {k: v for k, v in sorted(f_1.items(),
key=lambda item: item[1])}

 

 # Element addition in the list

 for i in f_lst.keys():

 final_list.append(i)

 return final_list

 

list1 = ["a", "b", "c", "d", "e", "f", "g",
"h", "i"]

list2 = [ 0, 1, 1, 0, 1, 2, 2, 0, 1]

sorting_of_element(list1,list2)  
  
---  
  
 __

 __

 **Output:**

    
    
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    
    
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

