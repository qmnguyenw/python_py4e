Python | Split and Pass list as separate parameter



With the advent of programming paradigms, there has been need to modify the
way one codes. One such paradigm is OOPS. In this, we have a technique called
modularity, which stands for making different modules/functions which perform
independent tasks in program. In this, we need to pass more than just
variable, but a list as well. Let’s discuss certain ways in which this task
can be performed.

 **Method #1 : Usingtuple()**  
This task can be performed using the tuple(). In this, we convert the pair
list to tuple and by this way we separate individual elements as variables,
ready to be sent to function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split and Pass list as separate parameter

# using tuple()

 

# Helper function for demonstration

def pass_args(arg1, arg2):

 print("The first argument is : " + str(arg1))

 print("The second argument is : " + str(arg2))

 

# initialize list

test_list = [4, 5]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Split and Pass list as separate parameter

# using tuple()

one, two = tuple(test_list)

pass_args(one, two)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5]
    The first argument is : 4
    The second argument is : 5
    

**Method #2 : Using * operator**  
Using * operator is the most recommended method to perform this task. The *
operator unpacks the dual list into args and hence solving our problem.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Split and Pass list as separate parameter

# using * operator

 

# Helper function for demonstration

def pass_args(arg1, arg2):

 print("The first argument is : " + str(arg1))

 print("The second argument is : " + str(arg2))

 

# initialize list

test_list = [4, 5]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Split and Pass list as separate parameter

# using * operator

pass_args(*test_list)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [4, 5]
    The first argument is : 4
    The second argument is : 5
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

