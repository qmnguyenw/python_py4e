Python – Group first elements by second elements in Tuple list



Given List of tuples, group 1st elements on basis of 2nd elements.

>  **Input** : test_list = [(6, 5), (2, 7), (2, 5), (8, 7), (3, 7)]  
>  **Output** : {5: [6, 2], 7: [2, 8, 3]}  
>  **Explanation** : 5 occurs along with 6 and 2 in tuple list, hence
> grouping.
>
>  **Input** : test_list = [(6, 5), (2, 7), (2, 5), (8, 7)]  
>  **Output** : {5: [6, 2], 7: [2, 8]}  
>  **Explanation** : 5 occurs along with 6 and 2 in tuple list, hence
> grouping.

 **Method #1 : Using loop + groupby() + sorted() + list comprehension +
lambda**

In this, the elements are sorted for grouping, function provided by lambda,
then only first elements are extracted using list comprehension out of result.
And final dictionary formation using loop.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group first elements by second elements in Tuple list

# Using loop + groupby() + sorted() + list comprehension + lambda

from itertools import groupby

 

# initializing list

test_list = [(6, 5), (2, 7), (2, 5), (8,
7), (9, 8), (3, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = dict()

 

# forming equal groups

for key, val in groupby(sorted(test_list, key = lambda ele:
ele[1]), key = lambda ele: ele[1]):

 res[key] = [ele[0] for ele in val] 

 

# printing results

print("Grouped Dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
    Grouped Dictionary : {5: [6, 2], 7: [2, 8, 3], 8: [9]}
    
    

**Method #2 : Using dictionary comprehension**

This is method similar to above, just a one-liner shorthand handled using
dictionary comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Group first elements by second elements in Tuple list

# Using dictionary comprehension 

from itertools import groupby

 

# initializing list

test_list = [(6, 5), (2, 7), (2, 5), (8,
7), (9, 8), (3, 7)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# shorthand to solve problem

res = {key : [v[0] for v in val] for key, val in
groupby(sorted(test_list, key = lambda ele: ele[1]), key =
lambda ele: ele[1])}

 

# printing results

print("Grouped Dictionary : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [(6, 5), (2, 7), (2, 5), (8, 7), (9, 8), (3, 7)]
    Grouped Dictionary : {5: [6, 2], 7: [2, 8, 3], 8: [9]}
    
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

