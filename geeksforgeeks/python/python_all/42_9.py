Python – Mirror Image of String



Given a String, perform its mirror imaging, return “Not Possible” if mirror
image not possible using english characters.

>  **Input** : test_str = ‘boid’  
>  **Output** : doib  
>  **Explanation** : d replaced by b and vice-versa as being mirror images.
>
>  **Input** : test_str = ‘gfg’  
>  **Output** : Not Possible  
>  **Explanation** : Valid Mirror image not possible.

 **Method : Using loop + loopup dictionary**

This is one way in which this task can be performed. In this, we construct
lookup dictionary for all valid mirrorable english characters, then perform
task of access from them.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Mirror Image of String

# Using Mirror Image of String

 

# initializing strings

test_str = 'void'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing mirror dictionary

mir_dict = {'b':'d', 'd':'b', 'i':'i',
'o':'o', 'v':'v', 'w':'w', 'x':'x'}

res = ''

 

# accessing letters from dictionary

for ele in test_str:

 if ele in mir_dict:

 res += mir_dict[ele]

 

 # if any character not present, flagging to be invalid 

 else:

 res = "Not Possible"

 break

 

# printing result 

print("The mirror string : " + str(res))   
  
---  
  
__

__

**Output**

    
    
    The original string is : void
    The mirror string : voib
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

