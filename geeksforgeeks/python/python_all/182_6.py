Python Program for Find minimum sum of factors of number



Given a number, find minimum sum of its factors.

Examples:

    
    
    Input : 12
    Output : 7
    **Explanation:**
    Following are different ways to factorize 12 and
    sum of factors in different ways.
    12 = 12 * 1 = 12 + 1 = 13
    12 = 2 * 6 = 2 + 6 = 8
    12 = 3 * 4 = 3 + 4 = 7
    12 = 2 * 2 * 3 = 2 + 2 + 3 = 7
    Therefore minimum sum is 7
    
    Input : 105
    Output : 15
    

__

__  
__

__

__  
__  
__

# Python program to find minimum

# sum of product of number

 

# To find minimum sum of

# product of number

def findMinSum(num):

 sum = 0

 

 # Find factors of number

 # and add to the sum

 i = 2

 while(i * i <= num):

 while(num % i == 0):

 sum += i

 num /= i

 i += 1

 sum += num

 

 # Return sum of numbers

 # having minimum product

 return sum

 

# Driver Code

num = 12

print findMinSum(num)

 

# This code is contributed by Sachin Bisht  
  
---  
  
 __

 __

 **Output:**

    
    
    7
    

Please refer complete article on Find minimum sum of factors of number for
more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

