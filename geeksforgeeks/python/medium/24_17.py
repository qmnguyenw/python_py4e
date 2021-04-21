Python | Print the initials of a name with last name in full



Given a name, print the initials of a name(uppercase) with last name(with
first alphabet in uppercase) written in full separated by dots.

 **Examples:**

    
    
    Input : geeks for geeks
    Output : G.F.Geeks
    
    Input : mohandas karamchand gandhi
    Output : M.K.Gandhi 
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **naive approach** of this will be to iterate for spaces and print the next
letter after every space except the last space. At last space we have to take
all the characters after the last space in a simple approach.

Using **Python in inbuilt functions** we can split the words into a list, then
traverse till the second last word and print the first character in capitals
using upper() function in python and then add the last word using title()
function in Python which automatically converts the first alphabet to capital.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# python program to print initials of a name

def name(s):

 

 # split the string into a list 

 l = s.split()

 new = ""

 

 # traverse in the list 

 for i in range(len(l)-1):

 s = l[i]

 

 # adds the capital first character 

 new += (s[0].upper()+'.')

 

 # l[-1] gives last item of list l. We

 # use title to print first character in

 # capital.

 new += l[-1].title()

 

 return new 

 

# Driver code 

s ="mohandas karamchand gandhi"

print(name(s))   
  
---  
  
__

__

**Output:**

    
    
    M.K.Gandhi
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

