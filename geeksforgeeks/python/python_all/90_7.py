Python | Sum of number digits in List



The problem of finding summation of digit of number is quite common. This can
sometimes come in form of list and we need to perform that. This has
application in many domains such as school programming and web development.
Let’s discuss certain ways in which this problem can be solved.

 **Method #1 : Using loop +str()**  
This is brute force method to perform this particular task. In this, we run a
loop for each element, convert each digit to string and perform the count of
sum of each digits.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sum of number digits in List

# using loop + str()

 

# Initializing list

test_list = [12, 67, 98, 34]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Sum of number digits in List

# using loop + str()

res = []

for ele in test_list:

 sum = 0

 for digit in str(ele):

 sum += int(digit)

 res.append(sum)

 

# printing result 

print ("List Integer Summation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [12, 67, 98, 34]
    List Integer Summation : [3, 13, 17, 7]
    

**Method #2 : Usingsum() \+ list comprehension**  
This task can also be performed using shorthand using above functionalities.
The sum() is used to compute summation and list comprehension is used to
compute iterations.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Sum of number digits in List

# using sum() + list comprehension

 

# Initializing list

test_list = [12, 67, 98, 34]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Sum of number digits in List

# using sum() + list comprehension

res = list(map(lambda ele: sum(int(sub) for sub
in str(ele)), test_list))

 

# printing result 

print ("List Integer Summation : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [12, 67, 98, 34]
    List Integer Summation : [3, 13, 17, 7]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

