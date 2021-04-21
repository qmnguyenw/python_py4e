Python | Find the equivalent discount in successive discounts in percentages



You are given n successive discounts in percentages. Your task is to find the
equivalent discount in percentage. Input will contain a list in which each
element of the list will be discount in percentage that will be negative in
sign.

 **Examples:**

    
    
    **Input :**  a = [-10, -35, -60, -75]
    **Output :**  -94.14
    
    **Input :**  a = [-5, -20, -10.-23]
    **Output :**  -49.08
    

SUCCESSIVE CHANGES = A + B + (A*B) / 100  
 **How does this formula work?**  
Let x be the initial value. After A% change, value of x becomes (x + x*A/100).
After successive B% change, value of x becomes (x + x*A/100) + (x +
x*A/100)*B/100. So increment in x’s value is x*(A + B + A*B/100)/100. In terms
of percentage, we can say that the value is incremented by (A + B + A*B/100)%

 **Approach:**

  * Simply, apply sucessive change formula between arr[0] and arr[1] and store the result in result variable.
  * Now, calculate successive change between result and arr[2] using the above formula and store the result in result variable and so on.

 **Code: Python program for finding the equivalent discount in successive
discounts in percentages.**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Function to find the equivalent discount in

# successive discounts in percentages

def equivalentdis(a):

 if(len(a)== 1):

 return(a[0])

 else:

 # succesive change from two = a[0] + a[1]+ (a[0]*a[1])/100

 change =(a[0] + a[1]+
(a[0]*a[1])/100)

 for i in range(2, len(a)): 

 # iterating a[0] + a[1]+ (a[0]*a[1])/100 

 # len(a)-2 times

 change = (change + a[i]+(change * a[i]) / 100)

 return change; 

# Driver code

print(equivalentdis([-10, -20, -30, -40]))

   
  
---  
  
__

__

**Output :**

    
    
    -69.75999999999999

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

