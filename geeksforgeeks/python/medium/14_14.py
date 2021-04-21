Python | Percentage increase in the total surface area of the cuboid



Given a cuboid of length **L** , breadth **B** and Height **H** , the task is
to find percentage increase in the total surface area of the cuboid if length,
breadth and height are increased by fixed percentages.

 **Examples:**

    
    
    **Input :**
    L = 20, B = 30, H = 50, l = 10 %, b = 12 %, h = 15 %
    **Output :**
    26.97 %
    
    **Input :**
    L = 40, B = 60, H = 15, l = 5 %, b = 7 %, h = 12 %
    **Output :**
    14.88 %
    

**Code : Python code to find the increase in the total surface area of the
cuboid.**

 __

 __  
 __

 __

 __  
 __  
 __

# Function to return the percentage increase

# in the total surface area of the cuboid 

# Total surface area of a cuboid = 2(L * B) + (L * H) + (B * H)

def increaseIntsa(L, B, H, l, b, h):

 oldsurfacearea = 2*((L * B) + (L * H) + (B *
H))

 newsurfacearea = 2*((L + (L * l * 0.01))*(B +
(B * b*0.01)) +

 (L + (L * l * 0.01))*(H + (H * h*0.01))
+

 (B + (B * b * 0.01))*(H + (H * h*0.01)))

 increase = (newsurfacearea - oldsurfacearea)

 increasepercent = (increase / oldsurfacearea) * 100

 return(increasepercent)

 

# Cuboid dimnesions

L = 20

B = 30

H = 50

 

# percentage increase

l = 10

b = 12

h = 15

print(increaseIntsa(L, B, H, l, b, h), "%")   
  
---  
  
__

__

**Output :**

    
    
    26.974193548387092 %

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

