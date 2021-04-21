Python program to convert meters in yards and vice versa



Given the distance in either meter or yard, the task here is to generate a
Python program that converts distance given in meters to yards and vice versa.

 **Examples:**

    
    
     **Input** : Length in Meter: 245
           Length in Yard : 100
    
    **Output:** 245 Meter in Yard = 267.9344 
            100 Yards in Meter = 91.4403
    
    
    **Input:** Length in Meter: 5
           Length in Yard : 20
    
    **Output:** 5 Meter in Yard = 5.4680 
            20 Yards in Meter = 18.2881

 **Formula used –**

    
    
    1 Meter = 1.09361 Yard

So from the above formula, 1 Meter is equivalent to 1.09361 yards, hence to
convert meters to yards, simply multiply the distance given in meters by
1.09361, and to convert Yard to meter, we just have to divide length in Yard
by 1.09361.

Below is the implementation.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

meter= 5 # Length in Meter

yard = 20 # Length in Yard

 

# converting Meter to Yard

meter_to_yard = meter * 1.09361

 

# converting Yard to meter

yard_to_meter = yard / 1.09361

 

# printing the output

print("%d Meter in Yard = %.4f " % (meter, meter_to_yard))

print("%d Yard in Meter = %.4f " % (yard, yard_to_meter))  
  
---  
  
 __

 __

 **Output:**

> 5 Meter in Yard = 5.4680
>
> 20 Yard in Meter = 18.2881

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

