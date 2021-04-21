Python – Custom element repetition



Given list of elements and required occurrence list, perform repetition of
elements.

>  **Input** : test_list1 = [“Gfg”, “Best”], test_list2 = [4, 5]  
>  **Output** : [‘Gfg’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘Best’, ‘Best’, ‘Best’, ‘Best’,
> ‘Best’]  
>  **Explanation** : Elements repeated by their occurrence number.
>
>  **Input** : test_list1 = [“Gfg”], test_list2 = [5]  
>  **Output** : [‘Gfg’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘Gfg’]  
>  **Explanation** : Elements repeated by their occurrence number.

 **Method #1 : Using loop + extend()**

The combination of above functions provide one of the ways in which this task
can be performed. In this, we iterate using loop and perform extension of
elements with repetition using extend().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom elements repetition

# Using loop + extend()

 

# initializing lists

test_list1 = ["Gfg", "is", "Best"]

test_list2 = [4, 3, 5]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using loop to perform iteration

res = []

for idx in range(0, len(test_list1)):

 

 # using extend to perform element repetition

 res.extend([test_list1[idx]] * test_list2[idx])

 

# printing result 

print("The repeated list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : ['Gfg', 'is', 'Best']
    The original list 2 : [4, 3, 5]
    The repeated list : ['Gfg', 'Gfg', 'Gfg', 'Gfg', 'is', 'is', 'is', 'Best', 'Best', 'Best', 'Best', 'Best']
    

**Method #2 : Using loop + zip()**

This is yet another way in which this task can be performed. In this, we use
zip() to match element with its repetition occurrence and perform required
task of duplication.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom elements repetition

# Using loop + zip()

 

# initializing lists

test_list1 = ["Gfg", "is", "Best"]

test_list2 = [4, 3, 5]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# using zip() to intervene elements and occurrence

res = []

for ele, occ in zip(test_list1, test_list2):

 res.extend([ele] * occ)

 

# printing result 

print("The repeated list : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list 1 : ['Gfg', 'is', 'Best']
    The original list 2 : [4, 3, 5]
    The repeated list : ['Gfg', 'Gfg', 'Gfg', 'Gfg', 'is', 'is', 'is', 'Best', 'Best', 'Best', 'Best', 'Best']
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

