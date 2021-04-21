Python Program to Print the Natural Numbers Summation Pattern



Given a natural number n, the task is to write a Python program to first find
the sum of first n natural numbers and then print each step as a pattern.

>  **Input:** 5
>
>  **Output:**
>
> 1 = 1  
> 1 + 2 = 3  
> 1 + 2 + 3 = 6  
> 1 + 2 + 3 + 4 = 10  
> 1 + 2 + 3 + 4 + 5 = 15
>
>  **Input:** 10
>
>  
>
>
>  
>
>
>  **Output:**
>
> 1 = 1
>
> 1 + 2 = 3
>
> 1 + 2 + 3 = 6
>
> 1 + 2 + 3 + 4 = 10
>
> 1 + 2 + 3 + 4 + 5 = 15
>
> 1 + 2 + 3 + 4 + 5 + 6 = 21
>
> 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
>
> 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36
>
> 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
>
> 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

 **Approach:**

  * Take Input n.
  * Use two loops:
    * j ranging between 1 to n.
    * i ranging between 1 to j.
  * Print the value of i and ‘+’ operator while appending the value of i to a list.
  * Then Find the Sum of Elements in the List.
  * Print “=” with Total Sum.
  * Exit.

 **Program:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Inputing Natural Number

number = int(input("Enter the Natural Number: "))

 

# j ranges from 1 to n

for j in range(1, number+1):

 

 # Initializing List

 a = []

 

 # i loop ranges from 1 to j

 for i in range(1, j+1):

 print(i, sep=" ", end=" ")

 if(i < j):

 print("+", sep=" ", end=" ")

 a.append(i)

 print("=", sum(a))

 

print()  
  
---  
  
 __

 __

 **Output:**

> Enter the Natural Number: 5
>
> 1 = 1
>
> 1 + 2 = 3
>
> 1 + 2 + 3 = 6
>
> 1 + 2 + 3 + 4 = 10
>
> 1 + 2 + 3 + 4 + 5 = 15

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

