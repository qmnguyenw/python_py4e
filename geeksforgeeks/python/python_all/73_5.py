Python Program to find volume, surface area and space diagonal of a cuboid



Given the length, base, and height of a cuboid. The task is to find the
Surface Area, Volume and space diagonal of the cuboid.

![Cuboid-Diagram-1626191](https://media.geeksforgeeks.org/wp-
content/uploads/20200427221020/Cuboid-Diagram-1626191.png)

 **Examples:**

    
    
    **Input :** 
    length = 9
    bradth = 6
    height = 10 
    **Output :**
    Surface area = 408 
    volume = 540
    space diagonal = 14.73 
    
    **Input :**
    length = 5
    breadth = 4
    height = 3 
    **Output :**
    surface area = 94 
    volume = 60 
    space diagonal = 7.07 
    

**Formulae Used:**

  * Surface Area = ![\[2 * \(l*b + b*h + h*l\)\]](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-588338574131c4a820ab74533364333e_l3.png)
  * Volume = ![\[\(l*b*h\)\]](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-67167737bac8d62397e73d430449e072_l3.png)
  * Spacle diagonal = ![\[sqrt{\( l**2 + b**2 + h**2\)}\] ](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f55e1f4c3012bc0e9aedc55797223144_l3.png)

Below is the implementation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find the

# Surface area, volume and

# space diagonal of rectangular

# prism

 

import math

 

 

# function to calculate

# Surface area

def find_surafce_area(l, b, h):

 

 # formula of surface_area = 2(lb + bh + hl)

 Surface_area = 2 * ( l * b + b * h + h * l)

 

 # Display surface area

 print(Surface_area)

 

# function to find the

# Volume of rectangular 

# prism

def find_volume(l, b, h):

 

 # formula to calculate

 # volume = (l * b*h)

 Volume = (l * b * h)

 

 # Display volume

 print(Volume)

 ategories Most Used

 School Programming

 Aptitude

 Re

def find_space_diagonal(l, b, h):

 

 # formula to calculate

 # Space diagonal = square_root(l**2 + b**2 + h**2)

 Space_diagonal = math.sqrt(l**2 + b**2 +
h**2)

 

 # display space diagonal

 print(Space_diagonal)

 

# Driver Code

l = 9

b = 6

h = 10

 

# surface area

# function call

find_surafce_area(l, b, h)

 

# volume function call

find_volume(l, b, h)

 

# Space diagonal function call

find_space_diagonal(l, b, h)

   
  
---  
  
__

__

**Output:**

    
    
    408
    540
    14.730919862656235

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

