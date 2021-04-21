Python | Test if tuple is distinct



Sometimes, while working with records, we have a problem in which we need to
find if all elements of tuple are different. This can have applications in
many domains including web development. Let’s discuss certain ways in which
this task can be performed.

 **Method #1 : Using loop**  
This is a brute force way in which this task can be performed. In this, we
just iterate through all tuple elements and put it in set if it’s the first
occurrence. During the subsequence occurrence we check in set, if it exists,
we return False.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if tuple is distinct

# Using loop

 

# initialize tuple 

test_tup = (1, 4, 5, 6, 1, 4)

 

# printing original tuple 

print("The original tuple is : " + str(test_tup))

 

# Test if tuple is distinct

# Using loop

res = True

temp = set()

for ele in test_tup:

 if ele in temp:

 res = False

 break

 temp.add(ele)

 

# printing result

print("Is tuple distinct ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : (1, 4, 5, 6, 1, 4)
    Is tuple distinct ? : False
    

**Method #2 : Usingset() + len()**  
In this method, we convert the tuple into a set using set(), and then check it
with original tuple length, if matches, means that it was a distinct tuple and
returns True.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Test if tuple is distinct

# Using set() + len()

 

# initialize tuple 

test_tup = (1, 4, 5, 6)

 

# printing original tuple 

print("The original tuple is : " + str(test_tup))

 

# Test if tuple is distinct

# Using set() + len()

res = len(set(test_tup)) == len(test_tup)

 

# printing result

print("Is tuple distinct ? : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original tuple is : (1, 4, 5, 6)
    Is tuple distinct ? : True
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

