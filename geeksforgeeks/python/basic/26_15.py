Using else conditional statement with for loop in python



In most of the programming languages (C/C++, Java, etc), the use of else
statement has been restricted with the if conditional statements. But Python
also allows us to use the else condition with for loops.

> The else block just after for/while is executed only when the loop is NOT
> terminated by a break statement.

 **Else block is executed in below Python 3.x program:**

 __

 __  
 __

 __

 __  
 __  
 __

for i in range(1, 4):

 print(i)

else: # Executed because no break in for

 print("No Break")  
  
---  
  
 __

 __

Output :

    
    
    1
    2
    3
    No Break
    

**Else block is NOT executed in below Python 3.x program:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

for i in range(1, 4):

 print(i)

 break

else: # Not executed as there is a break

 print("No Break")  
  
---  
  
 __

 __

Output :

    
    
    1

Such type of else is useful only if there is an if condition present inside
the loop which somehow depends on the loop variable.

In the following example, the else statement will only be executed if no
element of the array is even, i.e. if statement has not been executed for any
iteration. Therefore for the array [1, 9, 8] the if is executed in third
iteration of the loop and hence the else present after the for loop is
ignored. In case of array [1, 3, 5] the if is not executed for any iteration
and hence the else after the loop is executed.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3.x program to check if an array consists

# of even number

def contains_even_number(l):

 for ele in l:

 if ele % 2 == 0:

 print ("list contains an even number")

 break

 

 # This else executes only if break is NEVER

 # reached and loop terminated after all iterations.

 else: 

 print ("list does not contain an even number")

 

# Driver code

print ("For List 1:")

contains_even_number([1, 9, 8])

print (" \nFor List 2:")

contains_even_number([1, 3, 5])  
  
---  
  
 __

 __

Output:

    
    
    For List 1:
    list contains an even number
    
    For List 2:
    list does not contain an even number
    

As an **exercise** , predict the output of following program.

 __

 __  
 __

 __

 __  
 __  
 __

count= 0

while (count < 1): 

 count = count+1

 print(count)

 break

else:

 print("No Break")  
  
---  
  
 __

 __

This article is contributed by **Harshit Agrawal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

