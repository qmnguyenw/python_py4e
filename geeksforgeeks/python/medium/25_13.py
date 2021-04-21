Sum 2D array in Python using map() function



Given a 2-D matrix, we need to find sum of all elements present in matrix ?

Examples:

    
    
    Input  : arr = [[1, 2, 3], 
                    [4, 5, 6], 
                    [2, 1, 2]]
    Output : Sum = 26
    
    

This problem can be solved easily using two for loops by iterating whole
matrix but we can solve this problem quickly in python using map() function.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to calculate sum of all elements in matrix

# sum(arr) is a python inbuilt function which calculates

# sum of each element in a iterable ( array, list etc ).

# map(sum,arr) applies a given function to each item of 

# an iterable and returns a list of the results.

def findSum(arr):

 

 # inner map function applies inbuilt function 

 # sum on each row of matrix arr and returns 

 # list of sum of elements of each row

 return sum(map(sum,arr)) 

 

# Driver function

if __name__ == "__main__":

 arr = [[1, 2, 3], [4, 5, 6], [2, 1,
2]]

 print ("Sum = ",findSum(arr))  
  
---  
  
 __

 __

Output:

    
    
    26
    

**What does map() do?**  
The map() function applies a given function to each item of an iterable(list,
tuple etc.) and returns a list of the results. For example see given below
example :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of map()

 

# Function to calculate square of any number

def calculateSquare(n):

 return n*n

 

# numbers is a list of elements

numbers = [1, 2, 3, 4]

 

# Here map function is mapping calculateSquare 

# function to each element of numbers list.

# It is similar to pass each element of numbers 

# list one by one into calculateSquare function 

# and store result in another list

result = map(calculateSquare, numbers)

 

# resultant output will be [1,4,9,16]

print (result)  
  
---  
  
 __

 __

Output :

    
    
    [1, 4, 9, 16]

This article is contributed by **Shashank Mishra (Gullu)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

