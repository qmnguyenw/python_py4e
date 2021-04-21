Python | Print an Inverted Star Pattern



Here we are going to print inverted star pattern of desired sizes.  
 **Examples:**

    
    
    1) Below is the inverted star pattern of size n=5 
      (Because there are 5 horizontal lines
       or rows consist of stars). 
    
       *****
        ****
         ***
          **
           *
    
    2) Below is the inverted star pattern of size n=10 
      (Because there are 5 horizontal lines
       or rows consist of stars).
    
       **********
        *********
         ********
          *******
           ******
            *****
             ****
              ***
               **
                *
    

**Let’s see Python program to print inverted star pattern:**

 __

 __  
 __

 __

 __  
 __  
 __

# python 3 code to print inverted star

# pattern 

 

# n is the number of rows in which

# star is going to be printed.

n=11

 

# i is going to be enabled to

# range between n-i t 0 with a

# decrement of 1 with each iteration.

# and in print function, for each iteration,

# ” ” is multiplied with n-i and ‘*’ is

# multiplied with i to create correct

# space before of the stars.

for i in range (n, 0, -1):

 print((n-i) * ' ' + i * '*')  
  
---  
  
 __

 __

 **Explanation:**

  * The first number of rows is stored in variable n.
  * Then the for loop enables i to range between n-i to 0 with a decrement of 1 with each iteration.
  * After that, for each iteration, ” ” is multiplied with n-i and ‘*’ is multiplied with i to create correct space before of the stars.
  * And finally desired pattern will be printed.

 **Output:**

    
    
    ***********
     **********
      *********
       ********
        *******
         ******
          *****
           ****
            ***
             **
              *
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

