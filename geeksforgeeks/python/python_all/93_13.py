Python | Mean of consecutive Sublist



Some of the classical problems in programming domain comes from different
categories and one among them is finding the mean of subsets. This particular
problem is also common when we need to compute the average and store
consecutive group mean. Let’s try different approaches to this problem in
python language.

 **Method #1 : Using list comprehension +sum()**  
The list comprehension can be used to perform the this particular task to
filter out successive groups and sum function can be used to get the summation
of the filtered solution. We divide the sum by sublist size for average.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Mean of consecutive Sublist

# using list comprehension + sum()

 

# initializing list

test_list = [4, 7, 8, 10, 12, 15, 13, 17,
14]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using list comprehension + sum()

# Mean of consecutive Sublist

res = [ sum(test_list[x : x + 3]) / 3 for x in
range(0, len(test_list), 3)]

 

# printing result

print("The grouped average list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 7, 8, 10, 12, 15, 13, 17, 14]
    The grouped average list is : [6.333333333333333, 12.333333333333334, 14.666666666666666]
    

**Method #2 : Usingsum() + itertools.islice()**  
The task of slicing the list into chunks is done by islice method here and the
conventional task of getting the summation is done by the sum function as the
above method. We divide the sum by sublist size for average.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Mean of consecutive Sublist

# using itertools.islice() + sum()

import itertools

 

# initializing list

test_list = [4, 7, 8, 10, 12, 15, 13, 17,
14]

 

# printing original list 

print("The original list : " + str(test_list))

 

# using itertools.islice() + sum()

# Mean of consecutive Sublist 

res = [sum(list(itertools.islice(test_list, i, i + 3)))
/ 3 for i in range(0, len(test_list), 3)]

 

# printing result

print("The grouped average list is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [4, 7, 8, 10, 12, 15, 13, 17, 14]
    The grouped average list is : [6.333333333333333, 12.333333333333334, 14.666666666666666]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

