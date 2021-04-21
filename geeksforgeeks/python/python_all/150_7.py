Python | Three element sum in list



The problem of getting the number of pairs that lead to a particular solution
has been dealt many times, this article aims at extending that to 3 numbers
and discussing several ways in which this particular problem can be solved.
Let’s discuss certain ways in which this can be performed.

 **Method #1 : Using Nested loops**

This is the naive method in which this particular problem can be solved and
takes outer loop to iterate for each elements and inner loop checks for the
remaining difference adding the pairs to the result.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# 3 element sum 

# using nested loops

 

# initializing list

test_list = [4, 1, 3, 2, 6, 5]

 

# initializing sum 

sum = 9

 

# printing original list

print("The original list : " + str(test_list))

 

# using nested loops

# 3 element sum 

res = []

for i in range(0, len(test_list)-2):

 for j in range(i + 1, len(test_list)-1):

 for k in range(j + 1, len(test_list)):

 if test_list[i] + test_list[j] + test_list[k] == sum:

 temp = []

 temp.append(test_list[i])

 temp.append(test_list[j])

 temp.append(test_list[k])

 res.append(tuple(temp))

 

# print result

print("The 3 sum element list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 1, 3, 2, 6, 5]
    The 3 sum element list is : [(4, 3, 2), (1, 3, 5), (1, 2, 6)]
    

  

  

**Method #2 : Usingitertools.combination()**  
This particular problem can also be done in a concise manner using the inbuilt
function of function. The combination function finds all the combination
taking K arguments leading to particular sum.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# 3 element sum 

# using itertools.combination()

from itertools import combinations

 

# function to get the sum 

def test(val):

 return sum(val) == 9

 

# initializing list

test_list = [4, 1, 3, 2, 6, 5]

 

# initializing sum 

summation = 9

 

# printing original list

print("The original list : " + str(test_list))

 

# using itertools.combination()

# 3 element sum 

res = list(filter(test, list(combinations(test_list, 3))))

 

# print result

print("The 3 sum element list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 1, 3, 2, 6, 5]
    The 3 sum element list is : [(4, 3, 2), (1, 3, 5), (1, 2, 6)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

