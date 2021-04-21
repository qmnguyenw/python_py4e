Python Program for Triangular Matchstick Number



Given a number X which represents the floor of a matchstick pyramid, write a
program to print the total number of matchstick required to form a pyramid of
matchsticks of x floors.

 **Examples:**

    
    
    **Input :** X = 1
    **Output :** 3
    **Input :** X = 2
    **Output :** 9
    

This is mainly an extension of triangular numbers. For a number X, the
matchstick required will be three times of X-th triangular numbers, i.e.,
(3*X*(X+1))/2

![](https://media.geeksforgeeks.org/wp-content/uploads/triangular-matchstick-
number.jpg)

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to find X-th triangular

# matchstick number

 

def numberOfSticks(x):

 return (3 * x * (x + 1)) / 2

 

# main()

print(int(numberOfSticks(7)))  
  
---  
  
 __

 __

 **Output:**

    
    
    84
    

Please refer complete article on Triangular Matchstick Number for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

