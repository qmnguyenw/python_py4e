All palindrome numbers in a list



Given a list, count and print all the palindrome numbers in it.

 **Examples:**

    
    
    **Input:** 10 121 133 155 141 252
    **Output:** 121 141 252
    Total palindrome nos. are 3
    
    **Input:** 111 220 784 565 498 787 363
    **Output:** 111 565 787 363
    Total palindrome nos. are 4
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **1.** Access an element from the list.  
 **2.** Now, in a temporary variable get its reverse value.  
 **3.** Now, compare the list element value by its reverse value, if both are
same print the list element and increase the counter c by 1.  
 **4.** Carry on this procedure till list becomes empty.  
 **5.** Now, print the counter value i.e total number of palindrome numbers in
given list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to count and

# print all palindrome numbers in a list. 

 

def palindromeNumbers(list_a): 

 

 c = 0

 

 # loop till list is not empty 

 for i in list_a: 

 

 # Find reverse of current number 

 t = i 

 rev = 0

 while t > 0: 

 rev = rev * 10 + t % 10

 t = t // 10

 

 # compare rev with the current number 

 if rev == i: 

 print (i) 

 c = c + 1

 

 print()

 print ("Total palindrome nos. are", c )

 print()

 

# Driver code 

def main(): 

 

 list_a = [10, 121, 133, 155, 141, 252] 

 palindromeNumbers(list_a) 

 

 list_b = [ 111, 220, 784, 565, 498, 787,
363] 

 palindromeNumbers(list_b) 

 

if __name__=="__main__": 

 main() # main function call   
  
---  
  
__

__

**Output:**

    
    
    121
    141
    252
    
    Total palindrome nos. are 3
    
    111
    565
    787
    363
    
    Total palindrome nos. are 4
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

