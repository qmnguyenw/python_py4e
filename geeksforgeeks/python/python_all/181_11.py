Python Program for compound interest



 **Compound Interest formula:**

> Formula to calculate compound interest annually is given by:  
>  **  
> A = P(1 + R/100) t**  
>  **Compound Interest = A – P**  
>  Where,  
> A is amount  
> P is principle amount  
> R is the rate and  
> T is the time span

 **Example:**

    
    
    Input : Principle (amount): 1200
            Time: 2
            Rate: 5.4
    Output : Compound Interest = 1333.099243
    

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to find compound

# interest for given values.

 

def compound_interest(principle, rate, time):

 

 # Calculates compound interest 

 Amount = principle * (pow((1 + rate / 100),
time))

 CI = Amount - principle

 print("Compound interest is", CI)

 

# Driver Code 

compound_interest(10000, 10.25, 5)

 

# This code is contributed by Abhishek Agrawal.  
  
---  
  
 __

 __

 **Output:**

    
    
    Compound interest is 6288.946267774416

Please refer complete article on Program to find compound interest for more
details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

