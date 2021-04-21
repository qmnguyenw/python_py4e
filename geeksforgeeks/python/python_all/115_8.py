Python | Construct string from character frequency tuple



Sometimes, while working with data, we can have a problem in which we need to
perform construction of string in a way that we have a list of tuple having
character and it’s corresponding frequency and we require to construct a new
string from that. Let’s discuss certain ways in which this task can be
performed.

 **Method #1 : Using loop**  
This is brute force method in which this task can be performed. In this, we
iterate the list and perform string concatenation using * operator and keep
building string this way.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String construction from character frequency

# using loop

 

# initialize list 

test_list = [('g', 4), ('f', 3), ('g', 2)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# String construction from character frequency

# using loop

res = ''

for char, freq in test_list:

 res = res + char * freq

 

# printing result

print("The constructed string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('g', 4), ('f', 3), ('g', 2)]
    The constructed string is : ggggfffgg
    

**Method #2 : Usingjoin() \+ list comprehension**  
The combination of above functionalities can be used to perform this task. In
this, we perform the task of extraction using list comprehension and making
string using join().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# String construction from character frequency

# using join() + list comprehension

 

# initialize list 

test_list = [('g', 4), ('f', 3), ('g', 2)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# String construction from character frequency

# using join() + list comprehension

res = ''.join(char * freq for char, freq in test_list)

 

# printing result

print("The constructed string is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [('g', 4), ('f', 3), ('g', 2)]
    The constructed string is : ggggfffgg
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

