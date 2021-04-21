Python Program for Tower of Hanoi



Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
The objective of the puzzle is to move the entire stack to another rod,
obeying the following simple rules:  
1) Only one disk can be moved at a time.  
2) Each move consists of taking the upper disk from one of the stacks and
placing it on top of another stack i.e. a disk can only be moved if it is the
uppermost disk on a stack.  
3) No disk may be placed on top of a smaller disk.  
Note: Transferring the top n-1 disks from source rod to Auxiliary rod can
again be thought of as a fresh problem and can be solved in the same manner.  

![faq.disk3](https://media.geeksforgeeks.org/wp-content/uploads/tower-of-
hanoi.png)

## Python

 __

 __  
 __

 __

 __  
 __  
 __

# Recursive Python function to solve the tower of hanoi

 

def TowerOfHanoi(n , source, destination, auxiliary):

 if n==1:

 print "Move disk 1 from source",source,"to
destination",destination

 return

 TowerOfHanoi(n-1, source, auxiliary, destination)

 print "Move disk",n,"from source",source,"to
destination",destination

 TowerOfHanoi(n-1, auxiliary, destination, source)

 

# Driver code

n = 4

TowerOfHanoi(n,'A','B','C') 

# A, C, B are the name of rods

 

# Contributed By Dilip Jain  
  
---  
  
 __

 __

Output:

    
    
     Move disk 1 from rod A to rod B
     Move disk 2 from rod A to rod C
     Move disk 1 from rod B to rod C
     Move disk 3 from rod A to rod B
     Move disk 1 from rod C to rod A
     Move disk 2 from rod C to rod B
     Move disk 1 from rod A to rod B
     Move disk 4 from rod A to rod C
     Move disk 1 from rod B to rod C
     Move disk 2 from rod B to rod A
     Move disk 1 from rod C to rod A
     Move disk 3 from rod B to rod C
     Move disk 1 from rod A to rod B
     Move disk 2 from rod A to rod C
     Move disk 1 from rod B to rod C
    
    

Please refer complete article on Program for Tower of Hanoi for more details!  

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

