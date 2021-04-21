Python Program for Program to find the sum of a Series 1/1! + 2/2! + 3/3! +
4/4! +…….+ n/n!



You have been given a series 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!, find out
the sum of the series till nth term.

 **Examples:**

    
    
    **Input :** n = 5
    **Output :** 2.70833
    
    **Input :** n = 7
    **Output :** 2.71806
    

__

__  
__

__

__  
__  
__

# Python code to find smallest K-digit

# number divisible by X

 

def sumOfSeries(num):

 

 # Computing MAX

 res = 0

 fact = 1

 

 for i in range(1, num+1):

 fact *= i

 res = res + (i/ fact)

 

 return res

 

 

n = 5

print("Sum: ", sumOfSeries(n))

 

# Code contributed by Mohit Gupta_OMG <(0_o)>  
  
---  
  
 __

 __

 **Output:**

    
    
    Sum: 2.70833
    

Please refer complete article on Program to find the sum of a Series 1/1! +
2/2! + 3/3! + 4/4! +…….+ n/n! for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

