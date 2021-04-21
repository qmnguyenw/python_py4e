Python – 3D Matrix to Coordinate List



Given a Matrix, row’s each element is list, pair each column to form
coordinates.

>  **Input** : test_list = [[[9, 2], [10, 3]], [[13, 6], [19, 7]]]  
>  **Output** : [(9, 10), (2, 3), (13, 19), (6, 7)]  
>  **Explanation** : Column Mapped Pairs.
>
>  **Input** : test_list = [[[13, 6], [19, 7]]]  
>  **Output** : [(13, 19), (6, 7)]  
>  **Explanation** : Column Mapped Pairs.

 **Method #1 : Using loop + zip()**

In this, we iterate for all the paired elements in inner tuples list, which is
paired using zip(), and append the result list.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# 3D Matrix to Coordinate List

# Using loop + zip()

 

# initializing list

test_list = [[[5, 6, 7], [2, 4, 6]], [[9,
2], [10, 3]], [[13, 6], [19, 7]]]

 

# printing original list

print("The original list is : " + str(test_list))

 

res = []

for sub1, sub2 in test_list:

 

 # zip() used to form pairing

 for ele in zip(sub1, sub2):

 res.append(ele)

 

# printing result 

print("Constructed Pairs : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[[5, 6, 7], [2, 4, 6]], [[9, 2], [10, 3]], [[13, 6], [19, 7]]]
    Constructed Pairs : [(5, 2), (6, 4), (7, 6), (9, 10), (2, 3), (13, 19), (6, 7)]
    

**Method #2 : Using list comprehension**

In this, we perform task of of above method in shorthand using list
comprehension.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# 3D Matrix to Coordinate List

# Using loop + zip()

 

# initializing list

test_list = [[[5, 6, 7], [2, 4, 6]], [[9,
2], [10, 3]], [[13, 6], [19, 7]]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# list comprehension to perform task in shorthand

res = [ele for sub1, sub2 in test_list for ele in
zip(sub1, sub2)]

 

# printing result 

print("Constructed Pairs : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [[[5, 6, 7], [2, 4, 6]], [[9, 2], [10, 3]], [[13, 6], [19, 7]]]
    Constructed Pairs : [(5, 2), (6, 4), (7, 6), (9, 10), (2, 3), (13, 19), (6, 7)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

