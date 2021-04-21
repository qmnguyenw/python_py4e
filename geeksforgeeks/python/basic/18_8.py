Python setattr() method



setattr() is used to assign the object attribute its value. Apart from ways to
assign values to class variables, through constructors and object functions,
this method gives you an alternative way to assign value.

> Syntax : **setattr(obj, var, val)**  
>  
>  **Parameters :**  
>  **obj :** Object whose which attribute is to be assigned.  
>  **var :** object attribute which has to be assigned.  
>  **val :** value with which variable is to be assigned.  
>  
>  **Returns :**  
>  None  
>

 **Code #1 :** demonstrating working of setattr()

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# working of setattr()

 

# initializing class 

class Gfg:

 name = 'GeeksforGeeks'

 

# initializing object

obj = Gfg()

 

# printing object before setattr

print("Before setattr name : ", obj.name)

 

# using setattr to change name

setattr(obj, 'name', 'Geeks4Geeks')

 

# printing object after setattr

print("After setattr name : ", obj.name)  
  
---  
  
 __

 __

Output:

    
    
    Before setattr name : GeeksforGeeks
    After setattr name : Geeks4Geeks
    

**Properties of setattr()**

  * setattr() can be used to assign None to any object attribute.
  * setattr() can be used to initialize a new object attribute.

 **Code #2 :** demonstrating properties of setattr()

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# properties of setattr()

 

# initializing class 

class Gfg:

 name = 'GeeksforGeeks'

 

# initializing object

obj = Gfg()

 

# printing object before setattr

print("Before setattr name : ", str(obj.name))

 

# using setattr to assign None to name

setattr(obj, 'name', None)

 

# using setattr to initialize new attribute

setattr(obj, 'description', 'CS portal')

 

# printing object after setattr

print("After setattr name : " + str(obj.name))

print("After setattr description : ", str(obj.description))  
  
---  
  
 __

 __

Output:

    
    
    Before setattr name : GeeksforGeeks
    After setattr name : None
    After setattr description : CS portal
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

