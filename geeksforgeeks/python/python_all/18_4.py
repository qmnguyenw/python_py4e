Python Program to find Sum of Negative, Positive Even and Positive Odd numbers
in a List



Given a list. The task is to find the sum of Negative, Positive Even, and
Positive Odd numbers present in the List.

 **Examples:**

    
    
     **Input:** -7 5 60 -34 1 
    **Output:**
    Sum of negative numbers is  -41 
    Sum of even positive numbers is  60 
    Sum of odd positive numbers is  6
    
    **Input:** 1 -1 50 -2 0 -3
    **Output:**
    Sum of negative numbers is  -6
    Sum of even positive numbers is  50
    Sum of odd positive numbers is  1

Negative numbers are the numbers less than 0 while positive even numbers are
numbers greater than 0 and also divisible by 2. 0 is assumed to be a positive
even number, in this case.

**Approach:**

  * The first approach input a list of numbers from the user.
  * Two loops are run, one for the positive numbers and the other for the negative numbers, computing the numbers’ summation.
  * If n is the size of the list of numbers,
  * it takes O(2n) time complexity, for iterating over the list of numbers twice.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

class Sumofnumbers:

 

 # find sum of negative numbers

 def negSum(self, list):

 

 # counter for sum of

 # negative numbers

 neg_sum = 0

 

 for num in list:

 

 # converting number

 # to integer explicitly

 num = int(num)

 

 # if negative number

 if(num < 0):

 

 # simply add to the

 # negative sum

 neg_sum + = num

 

 print("Sum of negative numbers is ", neg_sum)

 

 # find sum of positive numbers

 # according to categories

 def posSum(self, list):

 

 # counter for sum of

 # positive even numbers

 pos_even_sum = 0

 

 # counter for sum of

 # positive odd numbers

 pos_odd_sum = 0

 for num in list:

 

 # converting number

 # to integer explicitly

 num = int(num)

 

 # if negative number

 if(num >= 0):

 

 # if even positive

 if(num % 2 == 0):

 

 # add to positive

 # even sum

 pos_even_sum + = num

 else:

 

 # add to positive odd sum

 pos_odd_sum + = num

 

 print("Sum of even positive numbers is ",

 pos_even_sum)

 

 print("Sum of odd positive numbers is ",

 pos_odd_sum)

 

 

# input a list of numbers

list_num = [-7, 5, 60, -34, 1]

 

# creating an object of class

obj = Sumofnumbers()

 

# calling method for sum

# of all negative numbers

obj.negSum(list_num)

 

# calling method for

# sum of all positive numbers

obj.posSum(list_num)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Sum of negative numbers is  -41
    Sum of even positive numbers is  60
    Sum of odd positive numbers is  6
    

The second approach computes the sum of respective numbers in a single loop.
It maintains three counters for each of the three conditions, checks the
condition and accordingly adds the value of the number in the current sum .
**If n is the size of the list of numbers, it takes O(n) time complexity, for
iterating over the list of numbers once.**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

class Sumofnumbers:

 # find sum of numbers

 # according to categories

 def Sum(self, list):

 

 # counter for sum

 # of negative numbers

 neg_sum = 0

 

 # counter for sum of

 # positive even numbers

 pos_even_sum = 0

 

 # counter for sum of

 # positive odd numbers

 pos_odd_sum = 0

 

 for num in list:

 

 # converting number

 # to integer explicitly

 num = int(num)

 

 # if negative number

 if(num < 0):

 

 # simply add

 # to the negative sum

 neg_sum += num

 # if positive number

 else:

 

 # if even positive

 if(num % 2 == 0):

 

 # add to positive even sum

 pos_even_sum + = num

 else:

 

 # add to positive odd sum

 pos_odd_sum + = num

 print("Sum of negative numbers is ",

 neg_sum)

 print("Sum of even positive numbers is ",

 pos_even_sum)

 print("Sum of odd positive numbers is ",

 pos_odd_sum)

 

 

# input a list of numbers

list_num = [1, -1, 50, -2, 0, -3]

 

# creating an object of class

obj = Sumofnumbers()

 

# calling method for

# largest sum of all numbers

obj.Sum(list_num)  
  
---  
  
 __

 __

 **Output:**

    
    
    Sum of negative numbers is  -6
    Sum of even positive numbers is  50
    Sum of odd positive numbers is  1
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

