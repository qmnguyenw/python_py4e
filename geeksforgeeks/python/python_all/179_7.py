Python Program for Number of jump required of given length to reach a point of
form (d, 0) from origin in 2D plane



Given three positive integers **a, b** and **d**. You are currently at origin
(0, 0) on infinite 2D coordinate plane. You are allowed to jump on any point
in the 2D plane at euclidean distance either equal to **a** or **b** from your
current position. The task is to find the minimum number of jump required to
reach (d, 0) from (0, 0).

 **Examples:**

    
    
    **Input :** a = 2, b = 3, d = 1 
    **Output :** 2
    First jump of length a = 2, (0, 0) -> (1/2, √15/2)
    Second jump of length a = 2, (1/2, √15/2) -> (1, 0)
    Thus, only two jump are required to reach 
    (1, 0) from (0, 0).
    
    **Input :** a = 3, b = 4, d = 11 
    **Output :** 3
    (0, 0) -> (4, 0) using length b = 4
    (4, 0) -> (8, 0) using length b = 4
    (8, 0) -> (11, 0) using length a = 3
    

__

__  
__

__

__  
__  
__

# Python code to find the minimum number

# of jump required to reach 

# (d, 0) from (0, 0)

 

def minJumps(a, b, d):

 

 temp = a

 a = min(a, b)

 b = max(temp, b)

 

 if (d >= b):

 return (d + b - 1) / b

 

 # if d is 0

 if (d == 0):

 return 0

 

 # if d is equal to a.

 if (d == a):

 return 1

 

 # else make triangle, and only 2 

 # steps required.

 return 2

 

# main()

a = 3

b = 4

d = 11

print (int(minJumps(a, b, d)))

 

# Contributed by _omg  
  
---  
  
 __

 __

 **Output**

    
    
    3

Please refer complete article on Number of jump required of given length to
reach a point of form (d, 0) from origin in 2D plane for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

