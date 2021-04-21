Python | Replace tuple according to Nth tuple element



Sometimes, while working with data, we might have a problem in which we need
to replace the entry in which a particular entry of data is matching. This can
be a matching phone no, id etc. This has it’s application in web development
domain. Let’s discuss certain ways in which this task can be performed.

 **Method #1 : Using loop +enumerate()**  
This task can be performed using the combination of loops and enumerate
function which can help to access to the Nth element and then check and
replace when the condition is satisfied.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace tuple according to Nth tuple element

# Using loops + enumerate()

 

# Initializing list

test_list = [('gfg', 1), ('was', 2), ('best',
3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing change record

repl_rec = ('is', 2)

 

# Initializing N 

N = 1

 

# Replace tuple according to Nth tuple element

# Using loops + enumerate()

for key, val in enumerate(test_list):

 if val[N] == repl_rec[N]:

 test_list[key] = repl_rec

 break

 

# printing result

print("The tuple after replacement is : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('gfg', 1), ('was', 2), ('best', 3)]
    The tuple after replacement is : [('gfg', 1), ('is', 2), ('best', 3)]
    

**Method #2 : Using list comprehension**  
This is the one-liner approach to solve this particular problem. In this, we
just iterate the list element and keep matching the matching Nth element of
tuple and perform replacement.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace tuple according to Nth tuple element

# Using list comprehension

 

# Initializing list

test_list = [('gfg', 1), ('was', 2), ('best',
3)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Initializing change record

repl_rec = ('is', 2)

 

# Initializing N 

N = 1

 

# Replace tuple according to Nth tuple element

# Using list comprehension

res = [repl_rec if sub[N] == repl_rec[N] else sub for
sub in test_list]

 

# printing result

print("The tuple after replacement is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [('gfg', 1), ('was', 2), ('best', 3)]
    The tuple after replacement is : [('gfg', 1), ('is', 2), ('best', 3)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

