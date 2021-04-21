What Is Difference Between Del, Remove and Pop on Python Lists?



In python **del** is **** a keyword and **remove(), pop()** are in-built
methods. The purpose of these three are same but the behavior is different
**remove()** method delete values or object from the list using value and
**del** and **pop()** deletes values or object from the list using an index.

### del Keyword:

The _del_ keyword delete any variable, list of values from a list.

**Syntax:**

    
    
    del list_name[index]  # To delete single value
    del list_name        # To delete whole list

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# program to demonstrate use of del keyword

 

# assign list

numbers = [1, 2, 3, 2, 3, 4, 5]

 

# use del

del numbers[2]

 

# display list

print(numbers)

 

# use del

del numbers[-1]

 

# display list

print(numbers)

 

# use del

del numbers[0]

 

# display list

print(numbers)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [1, 2, 2, 3, 4, 5]
    [1, 2, 2, 3, 4]
    [2, 2, 3, 4]

###  **remove() Method:**

The _remove()_ method removes the first matching value from the list.

 **Syntax:**

    
    
    list_name.remove(value)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# program to demonstrate use of remove() method

 

# assign list

numbers = [1, 2, 3, 2, 3, 4, 5]

 

# use remove()

numbers.remove(3)

 

# display list

print(numbers)

 

# use remove()

numbers.remove(2)

 

# display list

print(numbers)

 

# use remove()

numbers.remove(5)

 

# display list

print(numbers)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 2, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4]

### pop() Method:

The pop() method like del deletes value at a particular index. But pop()
method returns deleted value from the list.

 **Syntax:**

    
    
    list_name.pop(index)

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# program to demonstrate use of pop() method

 

# assign list

numbers = [1, 2, 3, 2, 3, 4, 5]

 

# use remove()

numbers.pop(3)

 

# display list

print(numbers)

 

# use remove()

numbers.pop(-1)

 

# display list

print(numbers)

 

# use remove()

numbers.pop(0)

 

# display list

print(numbers)  
  
---  
  
 __

 __

 **Output:**

    
    
    [1, 2, 3, 3, 4, 5]
    [1, 2, 3, 3, 4]
    [2, 3, 3, 4]

###  del V/S remove() the V/Spop()

**del** |

**remove()** **** |

**pop()** **** | del is a keyword.| It is a method.| pop() is a method.| To
delete value it uses the index.| To delete value this method uses the value as
a parameter.| This method also uses the index as a parameter to delete.| The
del keyword doesn’t return any value.| The remove() method doesn’t return any
value.| pop() returns deleted value.| The del keyword can delete the single
value from a list or delete the whole list at a time.| At a time it deletes
only one value from the list.| At a time it deletes only one value from the
list.| It throws index error in case of the index doesn’t exist in the list.|
It throws value error in case of value doesn’t exist in the list.| It throws
index error in case of an index doesn’t exist in the list.  
---|---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

