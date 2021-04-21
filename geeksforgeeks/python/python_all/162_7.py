Python | Binary list to integer



The problem being discussed in this article is quite common that every
programmer would have come across it. Conversion of binary number list to its
integer value can be done using shorthands and knowledge of them can prove to
be quite useful. Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingjoin() \+ list comprehension**  
The combination of these two function can help to achieve this particular
task. In this method, the entire list is first converted to string and then
type conversion into int and then binary number is obtained.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# converting binary list to integer 

# using join() + list comprehension

 

# initializing list 

test_list = [1, 0, 0, 1, 1, 0]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using join() + list comprehension

# converting binary list to integer 

res = int("".join(str(x) for x in test_list), 2)

 

# printing result 

print ("The converted integer value is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 0, 0, 1, 1, 0]
    The converted integer value is : 38
    

**Method #2 : Using bit shift +| operator**  
This particular task can be performed by shifting the bits and taking the |
with each of the bits being processed. This is yet another elegant way in
which this can be performed.  

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# converting binary list to integer 

# using bit shift + | operator

 

# initializing list 

test_list = [1, 0, 0, 1, 1, 0]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# using bit shift + | operator

# converting binary list to integer 

res = 0

for ele in test_list:

 res = (res << 1) | ele

 

# printing result 

print ("The converted integer value is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 0, 0, 1, 1, 0]
    The converted integer value is : 38
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

