Different Input and Output Techniques in Python3



In this Article, we will learn some basic input-output techniques with the
help of which we can easily follow the input and output format mentioned in
the questions that we face in either daily coding life or in competitive
programming.

##  **Input Techniques**

 **1.** _ ****_**Taking a single Input:** A single input in Python can be
taken using the input() method.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# For integers

n = int(input())

 

# For floating or decimal numbers

n = float(input())

 

# For Strings

n = input()  
  
---  
  
 __

 __

  

  

 **2\. Taking Multiple Input:** Multiple inputs in Python can be taken with
the help of map() and split() method. The split() method splits the space
separated inputs and returns an iterable whereas when this function is used
with the map() function it can convert the inputs to float and int
accordingly.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# For Strings

x, y = input().split()

 

# For integers and floating point

# numbers

m, n = map(int, input().split()) 

m, n = map(float, input().split())  
  
---  
  
 __

 __

 **3\. Taking variable number of input as list or tuple:** For this the
split() and map() functions can be used. As these functions return an iterable
we can convert the given iterable to the list, tuple or set accordingly.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# For Input - 4 5 6 1 56 21

# (Space separated inputs)

n = list(map(int, input().split()))

print(n)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    [4, 5, 6, 1, 56, 21]
    

**4\. Taking Fixed and variable number of input:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Input: geeksforgeeks 2 0 2 0

str, *lst = input().split()

lst = list(map(int, lst))

 

print(str, lst)  
  
---  
  
 __

 __

 **Output:**

    
    
    geeksforgeeks [2, 0, 2, 0]

## Output Techniques

 **1\. Output on different line:**print() method is used in python for
printing to console.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

lst= ['geeks', 'for', 'geeks']

 

for i in lst:

 print(i)  
  
---  
  
 __

 __

 **Output:**

    
    
    geeks
    for
    geeks
    

**2\. Output on same line:**end parameter in Python can be used to print on
the same line.

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

lst= ['geeks', 'for', 'geeks']

 

for i in lst:

 print(i, end='')  
  
---  
  
 __

 __

 **Output:**

    
    
    geeksforgeeks

 **Example 2:** Printing with space.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

lst= ['geeks', 'for', 'geeks']

 

for i in lst:

 print(i,end=' ')  
  
---  
  
 __

 __

 **Output:**

    
    
    geeks for geeks
    

**3\. Output Formatting:** If you want to format your output then you can do
it with {} and format() function. {} is a placeholder for a variable that is
provided in the format() like we have %d in C programming.

 **Example:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

print('I love {}'.format('geeksforgeeks.'))

 

print("I love {0} {1}".format('Python', 'programming.')  
  
---  
  
 __

 __

 **Output:**

    
    
    I love geeksforgeeks.
    I love Python programming.
    

**Note:** For Formatting the integers or floating numbers the original method
can be used in the {}. like ‘{%5.2f}’ or with the numbers we can write it as
‘{0:5.2f}’. We can also use string module ‘%’ operator to format our output.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

