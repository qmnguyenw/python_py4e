Python Program to Compute Life Path Number



Given a String of date of format YYYYMMDD, our task is to compute the life
path number. **Life Path Number** is the number obtained by summation of
individual digits of each element repeatedly till single digit, of datestring.
Used in Numerology Predictions.

 **Examples:**

>  **Input :** test_str = “19970314”
>
>  **Output :** 7
>
>  **Explanation :** 1 + 9 + 9 + 7 = 26 , 2 + 6 = 8 [ year ] ; 0 + 3 = 3 [
> month ] ; 1 + 4 = 5 [ day ]. 5 + 3 + 8 = 16 ; 1 + 6 = 7.
>
>  
>
>
>  
>
>
>  **Input :** test_str = “19970104”
>
>  **Output :** 4
>
>  **Explanation :** 1 + 9 + 9 + 7 = 26 , 2 + 6 = 8 [ year ] ; 0 + 1 = 1 [
> month ] ; 0 + 4 = 4 [ day ]. 4 + 1 + 8 = 13 ; 1 + 3 = 4.

 **Method 1: Using loop**

The logic behind computing this is getting a summation of each digit and
perform %10 at each step. This way result curlers to single digit if it goes
to double-digit.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Life Path Number

# Using loop

 

# initializing string

test_str = "19970314"

 

# printing original string

print("The original string is : " + str(test_str))

 

res = 0

for num in test_str:

 res += int(num)

 

 # modulation in case of 2 digit number

 if res > 9:

 res = res % 10 + res // 10

 

# printing result

print("Life Path Number : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : 19970314
    Life Path Number  : 7

 **Method 2: Using recursion**

Similar way as above, the difference being the recursive function is used for
repeated modulation in case of digit count greater than 1.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Life Path Number

# Using recursion

 

# initializing string

test_str = "19970314"

 

# printing original string

print("The original string is : " + str(test_str))

 

# recursion function definition

def lpn(num): return num if num < 10 else lpn(num //
10 + num % 10)

 

# recursive function initial call

res = lpn(int(test_str))

 

# printing result

print("Life Path Number : " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original string is : 19970314
    Life Path Number  : 7

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

