Python | Split list into lists by particular value



The splitting of lists is quite common utility nowadays and there can be many
applications and use cases of the same. Along with these always come the
variations. One such variation can be split the list by particular value.
Let’s discuss a certain way in which list split can be performed.

 **Method : Using list comprehension +zip() + slicing + enumerate()**

This problem can be solved in two parts, in first part we get the index list
by which split has to be performed using enumerate function. And then we can
join the values according to the indices using zip and list slicing.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Split list into lists by particular value

# Using list comprehension + zip() + slicing + enumerate()

 

# initializing list

test_list = [1, 4, 5, 6, 4, 5, 6, 5,
4]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + zip() + slicing + enumerate()

# Split list into lists by particular value

size = len(test_list)

idx_list = [idx + 1 for idx, val in

 enumerate(test_list) if val == 5]

 

 

res = [test_list[i: j] for i, j in

 zip([0] + idx_list, idx_list +

 ([size] if idx_list[-1] != size else []))]

 

# print result

print("The list after splitting by a value : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 4, 5, 6, 4, 5, 6, 5, 4]
    The list after splitting by a value : [[1, 4, 5], [6, 4, 5], [6, 5], [4]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

