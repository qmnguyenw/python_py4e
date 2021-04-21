Python – Product of i^k in List



Python being the language of magicians can be used to perform many tedious and
repetitive tasks in a easy and concise manner and having the knowledge to
utilize this tool to the fullest is always useful. One such small application
can be finding product of i^k of list in just one line. Let’s discuss certain
ways in which this can be performed.

 **Method #1 : Usingreduce() + lambda + pow()**  
The power of lambda functions to perform lengthy tasks in just one line,
allows it combined with reduce which is used to accumulate the subproblem, to
perform this task as well. The pow() is used to perform task of computing
power. Works with only Python 2.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Product of i ^ k in List

# using reduce() + lambda + pow() 

 

# initializing list 

test_list = [1, 3, 5, 7, 9, 11] 

 

# printing original list 

print ("The original list is : " + str(test_list)) 

 

# initializing K 

K = 4

 

# using reduce() + lambda + pow() 

# Product of i ^ k in List 

res = reduce(lambda i, j: i * pow(j, K),
[pow(test_list[:1][0], K)] + test_list[1:]) 

 

# printing result 

print ("The product of i ^ k of list is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [1, 3, 5, 7, 9, 11]
    The product of i ^ k of list is : 11676104538800625
    

**Method #2 : Usingmap() + loop + pow()**  
The similar solution can also be obtained using the map function to integrate
and prod function to perform the product of the i^k number.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Product of i ^ k in List

# using map() + loop + pow() 

 

# getting Product 

def prod(val) : 

 res = 1

 for ele in val: 

 res *= ele 

 return res 

 

# initializing list 

test_list = [3, 5, 7, 9, 11] 

 

# printing original list 

print ("The original list is : " + str(test_list)) 

 

# initializing K 

K = 4

 

# using map() + loop + pow() 

# Product of i ^ k in List

res = prod(map(lambda i : pow(i, K), test_list)) 

 

# printing result 

print ("The product of i ^ k of list is : " + str(res))   
  
---  
  
__

__

**Output :**

    
    
    The original list is : [1, 3, 5, 7, 9, 11]
    The product of i ^ k of list is : 11676104538800625
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

