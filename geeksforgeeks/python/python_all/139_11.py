Python | Find closest number to k in given list



Given a list of numbers and a variable K, where K is also a number, write a
Python program to find the number in a list which is closest to the given
number K.

 **Examples:**

    
    
    **Input :** lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8], K = 9.1
    **Output :** 9.35
    
    **Input :** lst = [9, 11, 5, 3, 25, 18], K = 6
    **Output :** 5
    

  
**Method #1 :** Using min() method

In this approach, we use min method from Python and apply a key that finds
the absolute difference of each element with K, and returns the element having
minimum difference.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find Closest number in a list

 

def closest(lst, K):

 

 return lst[min(range(len(lst)), key = lambda i:
abs(lst[i]-K))]

 

# Driver code

lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8]

K = 9.1

print(closest(lst, K))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    9.35
    

