Python Program for Program to calculate area of a Tetrahedron



A Tetrahedron is simply a pyramid with a triangular base. It is a solid object
with four triangular faces, three on the sides or lateral faces, one on the
bottom or the base and four vertices or corners. If the faces are all
congruent equilateral triangles, then the tetrahedron is called regular.

The volume of the tetrahedron can be found by using the following formula :

> Volume = a3/(6&Sqrt;2)

Examples :

    
    
    Input : side = 3
    Output : 3.18
    
    
    Input : side = 20
    Output : 942.81
    

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find the volume of a tetrahedron

import math

def vol_tetra(side):

 volume = (side ** 3 / (6 * math.sqrt(2)))

 return round(volume, 2)

 

# Driver Code

side = 3

vol = vol_tetra(side)

print(vol)  
  
---  
  
 __

 __

 **Output :**

    
    
    3.18
    

Please refer complete article on Program to calculate area of a Tetrahedron
for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

