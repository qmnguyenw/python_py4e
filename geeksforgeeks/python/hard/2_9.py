Python program to calculate acceleration, final velocity, initial velocity and
time



Here we can find the acceleration (a), final velocity(v), initial velocity(u)
and time(t) using the formula a = (v-u)/t.

At first, functions are defined for all four types of calculations, in which
they will accept three inputs and assign the value in three different
variables. Then the fourth value is calculated using the acceleration formula
and the calculated value is returned. We are going to use the same
acceleration formula in different approaches.

 **Approach:**

  * In the first approach, we will find initial velocity by using the formula **“u = (v-a*t)”**
  * In the second approach, we will find final velocity by using formula **“v = u + a*t”**
  * In the third approach, we will find acceleration by using formula **“a = (v – u)/t”**
  * In the fourth approach, we will find time by using formula **“t = (v – v)/a”**

 **Example 1:** Initial velocity (u) is calculated.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

# Enter final velocity in m/s:

finalVelocity = 10

 

# Enter acceleration in m per second square

acceleration = 9.8

 

#Enter time taken in second

time = 1

initialVelocity = finalVelocity - acceleration * time

print("Initial velocity = ", initialVelocity)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Initial velocity =  0.1999999999999993

 ****

**Example 2:** Final velocity (v) is calculated.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

# initial velocity in m/s:

initialVelocity = 10

 

# acceleration in m per second square

acceleration = 9.8

 

# time taken in second

time = 1

finalVelocity = initialVelocity + acceleration * time

print("Final velocity = ", finalVelocity)  
  
---  
  
 __

 __

 **Output:**

    
    
    Final velocity =  19.8

 **Example 3:** Acceleration (a) is calculated.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#code

# initial velocity in m/s

initialVelocity = 0

 

# final velocity in m/s

finalVelocity = 9.8

 

# time in second

time = 1

 

acceleration = (finalVelocity - initialVelocity) / time

print("Acceleration = ", acceleration)  
  
---  
  
 __

 __

 **Output:**

    
    
    Acceleration =  9.8

 **Example 4:** Time (t) is calculated.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# code

#final velocity in m/s

finalVelocity = 10

 

#initial velocity in m/s

initialVelocity = 0

 

#acceleration in metre per second square

acceleration = 9.8

 

time = (finalVelocity - initialVelocity) / acceleration

print("Time taken = ", time)  
  
---  
  
 __

 __

 **Output:**

    
    
    Time taken =  1.0204081632653061

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

