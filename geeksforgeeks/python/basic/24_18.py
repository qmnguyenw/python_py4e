Python Membership and Identity Operators



 **Membership Operators**

Membership operators are operators used to validate the membership of a value.
It test for membership in a sequence, such as strings, lists, or tuples.

  1.  **in operator :** The ‘in’ operator is used to check if a value exists in a sequence or not. Evaluates to true if it finds a variable in the specified sequence and false otherwise.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# Finding common member in list 

# using 'in' operator

list1=[1,2,3,4,5]

list2=[6,7,8,9]

for item in list1:

 if item in list2:

 print("overlapping") 

else:

 print("not overlapping")  
  
---  
  
 __

 __

Output:

    
    
    not overlapping
    

**Same example without using in operator:**

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# Finding common member in list 

# without using 'in' operator

 

# Define a function() that takes two lists

def overlapping(list1,list2): 

 

 c=0

 d=0

 for i in list1:

 c+=1

 for i in list2:

 d+=1

 for i in range(0,c):

 for j in range(0,d):

 if(list1[i]==list2[j]):

 return 1

 return 0

list1=[1,2,3,4,5]

list2=[6,7,8,9]

if(overlapping(list1,list2)):

 print("overlapping")

else:

 print("not overlapping")  
  
---  
  
 __

 __

Output:

  

  

    
    
    not overlapping
    

  2. **‘not in’ operator-** Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# not 'in' operator

x = 24

y = 20

list = [10, 20, 30, 40, 50 ];

 

if ( x not in list ):

 print("x is NOT present in given list")

else:

 print("x is present in given list")

 

if ( y in list ):

 print("y is present in given list")

else:

 print("y is NOT present in given list")  
  
---  
  
 __

 __

 **Identity operators**

In Python are used to determine whether a value is of a certain class or type.
They are usually used to determine the type of data a certain variable
contains.  
There are different identity operators such as

  1.  **‘is’ operator –** Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate the use

# of 'is' identity operator

x = 5

if (type(x) is int):

 print("true")

else:

 print("false")  
  
---  
  
 __

 __

Output:

    
    
       true
    

  2. **‘is not’ operator –** Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate the

# use of 'is not' identity operator

x = 5.2

if (type(x) is not int):

 print("true")

else:

 print("false")  
  
---  
  
 __

 __

Output:

    
    
      true
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

