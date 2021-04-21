String slicing in Python to rotate a string



Given a string of size n, write functions to perform following operations on
string.

  1. Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
  2. Right (Or clockwise) rotate the given string by d elements (where d <= n).

Examples:

    
    
    Input : s = "GeeksforGeeks"
            d = 2
    Output : Left Rotation  : "eksforGeeksGe" 
             Right Rotation : "ksGeeksforGee"  
    
    
    Input : s = "qwertyu" 
            d = 2
    Output : Left rotation : "ertyuqw"
             Right rotation : "yuqwert"
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

We have existing solution for this problem please refer Left Rotation and
Right Rotation of a String link. We will solve this problem quickly in python
using String Slicing. Approach is very simple,

  1. Separate string in two parts **first & second**, for **Left rotation** Lfirst = str[0 : d] and Lsecond = str[d :]. For **Right rotation** Rfirst = str[0 : len(str)-d] and Rsecond = str[len(str)-d : ].
  2. Now concatenate these two parts **second + first** accordingly.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to rotate string left and right by d length

 

def rotate(input,d): 

 

 # slice string in two parts for left and right 

 Lfirst = input[0 : d] 

 Lsecond = input[d :] 

 Rfirst = input[0 : len(input)-d] 

 Rsecond = input[len(input)-d : ] 

 

 # now concatenate two parts together 

 print ("Left Rotation : ", (Lsecond + Lfirst) )

 print ("Right Rotation : ", (Rsecond + Rfirst)) 

 

# Driver program 

if __name__ == "__main__": 

 input = 'GeeksforGeeks'

 d=2

 rotate(input,d)   
  
---  
  
__

__

Output:

    
    
    Left Rotation  : eksforGeeksGe 
    Right Rotation : ksGeeksforGee
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

