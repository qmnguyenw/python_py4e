delattr() and del() in Python



 **delattr**

The **delattr()** method is used to delete the named attribute from the
object, with the prior permission of the object.  
 **Syntax:**

    
    
    **delattr(object, name)**
    
    The function takes only two parameter:
    
    **object :** from which 
    the name attribute is to be removed.
    **name :** of the attribute 
    which is to be removed.
    
    The function doesn't returns any value, 
    it just removes the attribute, 
    only if the object allows it.

 **The Working :** Suppose we have a class by name Geek and it has five
students as the attribute. So, using the delattr() method, we can remove any
one of the attributes.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate delattr()

class Geek:

 stu1 = "Henry"

 stu2 = "Zack"

 stu3 = "Stephen"

 stu4 = "Amy"

 stu5 = "Shawn"

 

names = Geek()

 

print('Students before delattr()--')

print('First = ',names.stu1)

print('Second = ',names.stu2)

print('Third = ',names.stu3)

print('Fourth = ',names.stu4)

print('Fifth = ',names.stu5)

 

# implementing the method

delattr(Geek, 'stu5')

 

print('After deleting fith student--')

print('First = ',names.stu1)

print('Second = ',names.stu2)

print('Third = ',names.stu3)

print('Fourth = ',names.stu4)

# this statement raises an error

print('Fifth = ',names.stu5)  
  
---  
  
 __

 __

Output:

    
    
    Students before delattr()--
    First =  Henry
    Second =  Zack
    Third =  Stephen
    Fourth =  Amy
    Fifth =  Shawn
    After deleting fith student--
    First =  Henry
    Second =  Zack
    Third =  Stephen
    Fourth =  Amy
    

When the execution moves to the last line of the program, i.e., when the fifth
attribute is called, the compiler raises an error:

  

  

    
    
    Traceback (most recent call last):
      File "/home/028e8526d603bccb30e9aeb7ece9e1eb.py", line 25, in 
        print('Fifth = ',names.stu5)
    AttributeError: 'Geek' object has no attribute 'stu5'
    

**del operator**

There is another operator in Python that does the similar work as the
delattr() method. It is the **del** operator. Let’s see how it works.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to illustrate del()

class Geek:

 stu1 = "Henry"

 stu2 = "Zack"

 stu3 = "Stephen"

 stu4 = "Amy"

 stu5 = "Shawn"

 

names = Geek()

 

print('Students before del--')

print('First = ',names.stu1)

print('Second = ',names.stu2)

print('Third = ',names.stu3)

print('Fourth = ',names.stu4)

print('Fifth = ',names.stu5)

 

# implementing the operator

del Geek.stu5

 

print('After deleting fith student--')

print('First = ',names.stu1)

print('Second = ',names.stu2)

print('Third = ',names.stu3)

print('Fourth = ',names.stu4)

# this statement raises an error

print('Fifth = ',names.stu5)  
  
---  
  
 __

 __

Output:

    
    
    Students before del--
    First =  Henry
    Second =  Zack
    Third =  Stephen
    Fourth =  Amy
    Fifth =  Shawn
    After deleting fith student--
    First =  Henry
    Second =  Zack
    Third =  Stephen
    Fourth =  Amy
    

The result is the same with an error:

    
    
    Traceback (most recent call last):
      File "/home/7c239eef9b897e964108c701f1f94c8a.py", line 26, in 
        print('Fifth = ',names.stu5)
    AttributeError: 'Geek' object has no attribute 'stu5'
    

**del vs** **delattr()**

  1.  **Dynamic deletion :** del is more explicit and efficient and delattr() allows dynamic attribute deleting.
  2.  **Speed :** If the above programs are considered and run then there is a slight difference between the speed of execution. del is slightly **faster** in comparison to delattr(), depending on the machine.
  3.  **byte-code Instructions :** del also takes less byte-code instructions in comparison to delattr().

So we conclude the comparison by saying that del is slightly faster than
delattr, but when it comes to dynamic deletion of attribute then delattr() has
advantage as it is not possible by del operator.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

