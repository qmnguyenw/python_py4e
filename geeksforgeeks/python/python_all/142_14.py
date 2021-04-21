Python | First N letters string construction



Sometimes, rather than initializing the empty string, we need to initialize a
string in a different way, vis., we may need to initialize a string with 1st N
characters in English alphabets. This can have application in competitive
Programming. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Usingjoin() \+ list comprehension**  
This task can be performed with the combination of the above functions. The
join function can be used to join the string and list comprehension can
perform the task of logic of adding N numbers.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# First N letters string construction

# using join() + list comprehension

 

# initializing N 

N = 15

 

# using join() + list comprehension

# First N letters string construction

res = ''.join(['% c' % x for x in range(97, 97
+ N)])

 

# print result

print("The string after construction : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The string after construction : abcdefghijklmno
    

**Method #2 : Usingord() + join() \+ list comprehension**  
This is yet another way in which this task can be performed, the ord function
performs the task of type casting of ascii number to a character, rest the
technique is similar to above method.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# First N letters string construction

# using join() + list comprehension + ord()

 

# initializing N 

N = 15

 

# using join() + list comprehension + ord()

# First N letters string construction

res = ''.join(chr(ord('a')+i) for i in range(N))

 

# print result

print("The string after construction : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The string after construction : abcdefghijklmno
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

