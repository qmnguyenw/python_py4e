Python | Series K divisible elements



The problem focused in this article is quite specific and may be less useful
in different domains. But the way this is going to solve may open doors to
solve potentially like problems, hence making it worth a read. This article
solves the problem of testing if a list contains series of K divisible. Let’s
discuss certain ways in which this problem can be solved.

 **Method #1 : Usingsum() + list comprehension + zip() + any()**  
This problem can be solved using the combination of above functions. This
method solves problem in 2 steps. In 1st step, we compute all the possible
pairs of N using list comprehension and zip function and in the second step we
use sum and any function to test for N divisible result, if we find any one of
it, we return positive.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Series K divisible elements

# using sum() + zip() + any() + list comprehension

 

# initializing list

test_list = [1, 5, 6, 4, 8, 12]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing N 

N = 3

 

# initializing K 

K = 4

 

# using sum() + zip() + any() + list comprehension

# Series K divisible elements

temp = ( test_list[i : i + N] for i in
range(len(test_list) - N + 1) )

res = any( sum(ele % K for ele in temps) % N
== 0 for temps in temp )

 

# print result

print("Does list contain the desired consecution : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 5, 6, 4, 8, 12]
    Does list contain the desired consecution : True
    

**Method #2 : Usinggroupby() + any()**  
The whole logic of doing the 1st step in the above method can be managed using
the groupby function in which we perform the grouping and any function can be
used later for checking the consecution.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Series K divisible elements

# using groupby() + any()

from itertools import groupby

 

# initializing list

test_list = [1, 5, 6, 4, 8, 12]

 

# printing original list

print("The original list : " + str(test_list))

 

# initializing N 

N = 3

 

# initializing K 

K = 4

 

# using groupby() + any()

# Series K divisible elements

res = any(len(list(sub)) == N for idx, sub in
groupby([sub % K for sub in test_list]))

 

# print result

print("Does list contain the desired consecution : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [1, 5, 6, 4, 8, 12]
    Does list contain the desired consecution : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

