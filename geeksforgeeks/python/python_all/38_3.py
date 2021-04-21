Python – Time Strings to Seconds in Tuple List



Given Minutes Strings, convert to total seconds in tuple list.

>  **Input** : test_list = [(“5:12”, “9:45”), (“12:34”, ), (“10:40”, )]  
>  **Output** : [(312, 585), (754, ), (640, )]  
>  **Explanation** : 5 * 60 + 12 = 312 for 5:12.
>
>  **Input** : test_list = [(“5:12”, “9:45”)]  
>  **Output** : [(312, 585)]  
>  **Explanation** : 5 * 60 + 12 = 312 for 5:12.

 **Method : Using loop + split()**

In this, we separate the minute and second components using split() and
perform mathematical computation to convert the value to required seconds,
strings converted to integers using int().

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Time Strings to Seconds in Tuple List

# Using loop + split()

 

# initializing list

test_list = [("5:12", "9:45"), ("12:34", "4:50"),
("10:40", )]

 

# printing original list

print("The original list is : " + str(test_list))

 

 

res = []

for sub in test_list:

 tup = tuple()

 

 # iterating each tuple

 for ele in sub:

 

 # perform conversion

 min, sec = ele.split(":")

 secs = 60 * int(min) + int(sec)

 tup += (secs, )

 res.append(tup)

 

# printing result 

print("The corresponding seconds : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list is : [('5:12', '9:45'), ('12:34', '4:50'), ('10:40', )]
    The corresponding seconds : [(312, 585), (754, 290), (640, )]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

