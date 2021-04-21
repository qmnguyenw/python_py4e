Python Program for Program to Print Matrix in Z form



Given a square matrix of order n*n, we need to print elements of the matrix in
Z form

    
    
    **Examples:**
    **Input :** mat[][] =  {1, 2, 3,
                        4, 5, 6,
                        7, 8, 9}
    **Output :** 1 2 3 5 7 8 9
    
    **Input :** mat[][] = {5, 19, 8, 7,
                       4, 1, 14, 8,
                       2, 20, 1, 9,
                       1, 2, 55, 4}
    **Output:** 5 19 8 7 14 20 1 2 55 4
    

__

__  
__

__

__  
__  
__

# Python program to print a

# square matrix in Z form

 

arr = [[4, 5, 6, 8], 

 [1, 2, 3, 1], 

 [7, 8, 9, 4], 

 [1, 8, 7, 5]]

 

n = len(arr[0])

 

i=0

for j in range(0, n-1):

 print(arr[i][j], end =" ") 

 

k = 1

for i in range(0, n):

 for j in range(n, 0, -1):

 if(j==n-k):

 print(arr[i][j], end = " ") 

 break; 

 k+=1

 

# Print last row

i=n-1; 

for j in range(0, n):

 print(arr[i][j], end = " ")

 

# Code contributed by Mohit Gupta_OMG <(0_o)>  
  
---  
  
 __

 __

 **Output:**

    
    
     4 5 6 8 3 8 1 8 7 5 

Please refer complete article on Program to Print Matrix in Z form for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

  
  

  

My Personal Notes _arrow_drop_up_

Save

