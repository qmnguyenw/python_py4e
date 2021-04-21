Python | Triple Product to K



The problem of getting the product number of pairs that lead to a particular
solution has been dealt many times, this articles aims at extending that to 3
numbers and discussing several ways in which this particular problem can be
solved. Let’s discuss certain ways in which this can be performed.

 **Method #1 : Using Nested loops**  
This is the naive method in which this particular problem can be solved and
takes outer loop to iterate for each elements and inner loop checks for the
remaining difference multiplying the pairs to the result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# 3 element product

# using nested loops

 

# initializing list

test_list = [4, 1, 3, 2, 6, 12]

 

# initializing product

product = 24

 

# printing original list

print("The original list : " + str(test_list))

 

# using nested loops

# 3 element product

res = []

for i in range(0, len(test_list)-2):

 for j in range(i + 1, len(test_list)-1):

 for k in range(j + 1, len(test_list)):

 if test_list[i] * test_list[j] * test_list[k] == product:

 temp = []

 temp.append(test_list[i])

 temp.append(test_list[j])

 temp.append(test_list[k])

 res.append(tuple(temp))

 

# print result

print("The 3 product element list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 1, 3, 2, 6, 12]
    The 3 product element list is : [(4, 1, 6), (4, 3, 2), (1, 2, 12)]
    

**Method #2 : Usingitertools.combination()**  
This particular problem can also be done in a concise manner using the inbuilt
function of function. The combination function finds all the combination
taking K arguments leading to particular product.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Triple Product to K

# using itertools.combination()

from itertools import combinations

 

# function to get the product

def test(val):

 prod = 1

 for ele in val:

 prod *= ele

 return (prod == 24)

 

# initializing list

test_list = [4, 1, 3, 2, 6, 12]

 

# initializing product

product = 24

 

# printing original list

print("The original list : " + str(test_list))

 

# using itertools.combination()

# 3 element product 

res = list(filter(test, list(combinations(test_list, 3))))

 

# print result

print("The 3 product element list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 1, 3, 2, 6, 12]
    The 3 product element list is : [(4, 1, 6), (4, 3, 2), (1, 2, 12)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

