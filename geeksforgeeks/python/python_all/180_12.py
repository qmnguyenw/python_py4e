Python Program for focal length of a spherical mirror



Focal length is the distance between the center of the mirror to the principal
foci. In order to determine the focal length of a spherical mirror we should
know the radius of curvature of that mirror. The distance from the vertex to
the center of curvature is called radius of curvature.

The focal length is half the radius of curvature.  
 **Formula :**

    
    
    F =   ( R / 2 )      for concave mirror
    F = - ( R / 2 )      for convex mirror

Examples :

    
    
    For a convex mirror
    Input : R = 30 
    Output : F = 15
    
    
    For a convex mirror
    Input : R = 25
    Output : F = - 12.5
    

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to determine

# the focal length of a

# of a spherical mirrorr 

 

# Determines focal length of 

# a spherical concave mirror

def focal_length_concave(R):

 return R / 2

 

# Determines focal length of

# a spherical convex mirror

def focal_length_convex(R):

 return - ( R/ 2 ) 

 

# Driver function

R = 30 ;

print("Focal length of spherical concave mirror is :",

 focal_length_concave(R)," units")

print("Focal length of spherical convex mirror is : ",

 focal_length_convex(R)," units")  
  
---  
  
 __

 __

Output :

    
    
    Focal length of spherical concave mirror is 15 units
    Focal length of spherical convex mirror is -15 units

Please refer complete article on Program to determine focal length of a
spherical mirror for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

