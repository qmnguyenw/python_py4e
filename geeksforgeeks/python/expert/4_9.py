Python program to print the Inverted heart pattern



Let us see how to print an inverted heart pattern in Python.

 **Example:**

    
    
     **Input:** 11
    **Output:**
    
              *
             ***
            *****
           *******
          *********
         ***********
        *************
       ***************
      *****************
     *******************
    *********************
     *********  ********
      *******    ******
       *****      **** 
       
    **Input:** 15
    **Output:**
                  *
                 ***
                *****
               *******
              *********
             ***********
            *************
           ***************
          *****************
         *******************
        *********************
       ***********************
      *************************
     ***************************
    *****************************
     *************  ************
      ***********    **********
       *********      ********
        *******        ******

 **Approach:**

  1. Determine the size of the heart.
  2. Print an inverted triangle with size number of rows.
  3. Print the rest of the heart in 4 segments inside another loop.
  4. Print the white space right-triangle at the beginning.
  5. Print the first trapezium with stars.
  6. Print the white space triangle.
  7. Print the second trapezium with stars.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# determining the size of the heart

size = 15

 

# printing the inverted triangle

for a in range(0, size):

 for b in range(a, size):

 print(" ", end = "")

 for b in range(1, (a * 2)): 

 print("*", end = "") 

 print("")

 

# printing rest of the heart

for a in range(size, int(size / 2) - 1 , -2):

 

 # printing the white space right-triangle

 for b in range(1, size - a, 2): 

 print(" ", end = "")

 

 # printing the first trapezium

 for b in range(1, a + 1): 

 print("*", end = "")

 

 # printing the white space triangle

 for b in range(1, (size - a) + 1): 

 print(" ", end = "")

 

 # printing the seconf trapezium

 for b in range(1, a): 

 print("*", end = "")

 

 # new line

 print("")  
  
---  
  
 __

 __

 **Output:**

    
    
                  *
                 ***
                *****
               *******
              *********
             ***********
            *************
           ***************
          *****************
         *******************
        *********************
       ***********************
      *************************
     ***************************
    *****************************
     *************  ************
      ***********    **********
       *********      ********
        *******        ******

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

