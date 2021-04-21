Python hash() method



In the new era of digital technology, Machine Learning, Artificial
Intelligence and Cyber Security are a rising phenomenon. Python stands out as
a language to implement much of the good sects of this.

Python offers **hash()** method to encode the data into unrecognisable
value.

>  **Syntax :** hash(obj)
>
>  **Parameters :**  
>  **obj :** The object which we need to convert into hash.
>
>  **Returns :** Returns the hashed value if possible.
>
>  
>
>
>  
>

 **Code #1 :** Demonstrating working of hash()

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# working of hash()

 

# initializing objects

int_val = 4

str_val = 'GeeksforGeeks'

flt_val = 24.56

 

# Printing the hash values.

# Notice Integer value doesn't change

# You'l have answer later in article.

print ("The integer hash value is : " + str(hash(int_val)))

print ("The string hash value is : " + str(hash(str_val)))

print ("The float hash value is : " + str(hash(flt_val)))  
  
---  
  
 __

 __

 **Output:**

    
    
    The integer hash value is : 4
    The string hash value is : -5570917502994512005
    The float hash value is : 1291272085159665688
    

**Properties of hash()**

  * Objects hashed using hash() are irreversible, leading to loss of information.
  * hash() returns hashed value only for immutable objects, hence can be used as an indicator to check for mutable/immutable objects.

 **Code #2 :** Demonstrating property of hash()

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# property of hash()

 

# initializing objects

# tuple are immutable

tuple_val = (1, 2, 3, 4, 5)

 

# list are mutable

list_val = [1, 2, 3, 4, 5]

 

# Printing the hash values.

# Notice exception when trying

# to convert mutable object

print ("The tuple hash value is : " + str(hash(tuple_val)))

print ("The list hash value is : " + str(hash(list_val)))  
  
---  
  
 __

 __

 **Output:**

    
    
    The tuple hash value is : 8315274433719620810

Exceptions :

    
    
    Traceback (most recent call last):
      File "/home/eb7e39084e3d151114ce5ed3e43babb8.py", line 15, in 
        print ("The list hash value is : " + str(hash(list_val)))
    TypeError: unhashable type: 'list'
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

