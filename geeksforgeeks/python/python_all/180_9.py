Python Program for Find the perimeter of a cylinder



Given diameter and height, find the perimeter of a cylinder.

Perimeter is the length of the outline of a two – dimensional shape. A
cylinder is a three – dimensional shape. So, technically we cannot find the
perimeter of a cylinder but we can find the perimeter of the cross-section of
the cylinder. This can be done by creating the projection on its base, thus,
creating the projection on its side, then the shape would be reduced to a
rectangle.

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/cylinder.png)

 **Formula :**  
Perimeter of cylinder ( P ) = ![ \( 2 * d \) + \( 2 * h \)
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a9cb28059813de89f9b08030d2c16a04_l3.png)  
here d is the diameter of the cylinder  
h is the height of the cylinder

Examples :

  

  

    
    
    Input : diameter = 5, height = 10 
    Output : Perimeter = 30
    
    Input : diameter = 50, height = 150 
    Output : Perimeter = 400
    

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Function to calculate

# the perimeter of a cylinder

def perimeter( diameter, height ) :

 return 2 * ( diameter + height ) 

 

# Driver function

diameter = 5 ;

height = 10 ;

print ("Perimeter = ",

 perimeter(diameter, height))  
  
---  
  
 __

 __

 **Output :**

    
    
    Perimeter = 30 units
    

Please refer complete article on Find the perimeter of a cylinder for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

