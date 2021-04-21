Python | Decimal to binary list conversion



The conversion of a binary list to a decimal number has been dealt in a
previous article. This article aims at presenting certain shorthand to do the
opposite, i.e binary to decimal conversion. Let’s discuss certain ways in
which this can be done.  

 **Method #1 : Using list comprehension + format()**  
In this method, the conversion of the decimal to binary is handled by the
format function. The logic of conversion to the list is done by the list
comprehension function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# decimal to binary number conversion

# using format() + list comprehension

 

# initializing number 

test_num = 38

 

# printing original number

print ("The original number is : " + str(test_num))

 

# using format() + list comprehension

# decimal to binary number conversion 

res = [int(i) for i in
list('{0:0b}'.format(test_num))]

 

# printing result 

print ("The converted binary list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original number is : 38
    The converted binary list is : [1, 0, 0, 1, 1, 0]
    

  
**Method #2 : Usingbin() \+ list comprehension**  
The inbuilt function bin performs the function of conversion to binary and the
list comprehension handles the logic to convert the binary number to the list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# decimal to binary number conversion

# using bin() + list comprehension

 

# initializing number 

test_num = 38

 

# printing original number

print ("The original number is : " + str(test_num))

 

# using bin() + list comprehension

# decimal to binary number conversion 

res = [int(i) for i in bin(test_num)[2:]]

 

# printing result 

print ("The converted binary list is : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original number is : 38
    The converted binary list is : [1, 0, 0, 1, 1, 0]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

