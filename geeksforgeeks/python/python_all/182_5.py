Python Program for Difference between sums of odd and even digits



Given a long integer, we need to find if the difference between sum of odd
digits and sum of even digits is 0 or not. The indexes start from zero (0
index is for leftmost digit).

 **Examples:**

    
    
    **Input :** 1212112
    **Output :** Yes
    **Explanation:-**
    the odd position element is 2+2+1=5
    the even position element is 1+1+1+2=5
    the difference is 5-5=0.so print yes.
    
    **Input :** 12345
    **Output :** No
    Explanation:-
    the odd position element is 1+3+5=9
    the even position element is 2+4=6
    the difference is 9-6=3 not  equal
    to zero. So print no.
    

**Method 1:** One by one traverse digits and find the two sums. If difference
between two sums is 0, print yes, else no.

 **Method 2 :** This can be easily solved using divisibility of 11. This
condition is only satisfied if the number is divisible by 11. So check the
number is divisible by 11 or not.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to check if difference between sum of

# odd digits and sum of even digits is 0 or not

 

def isDiff(n):

 return (n % 11 == 0)

 

# Driver code

n = 1243;

if (isDiff(n)):

 print("Yes")

else:

 print("No")

 

# Mohit Gupta_OMG <0_o>  
  
---  
  
 __

 __

 **Output:**

    
    
    Yes
    

Please refer complete article on Difference between sums of odd and even
digits for more details!

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready.

My Personal Notes _arrow_drop_up_

Save

