Python – Ways to print longest consecutive list without considering duplicates
element



Given, a list of Numbers, the task is to print the longest consecutive
(Strictly) list, without considering duplicate elements. If there is more than
one answer, print anyone. These type of problem are quite common while working
on some web development projects in Django or flask.  
Below are some ways to solve the above task.

 **Note :** If there are multiple answers, print anyone

>  **Input:**  
>  [1, 2, 3, 5, 6, 6, 7, 9, 10, 11, 13, 14, 15, 16, 16, 17, 18, 20, 21]
>
>  **Output:**  
>  [13, 14, 15, 16]
>
>  **Explanation :**  
>  Original list = [1, 2, 3, 5, 6, 6, 7, 9, 10, 11, 13, 14, 15, 16, 16, 17,
> 18, 20, 21]  
> Calculated list = [13, 14, 15, 16, 16, ]  
> Unique elements = [13, 14, 15, 16, ]
>
>  
>
>
>  
>

 **Method 1: Using Iteration**  
The basic method that comes to mind while performing this operation is the
naive method of printing longest consecutive list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to print longest consecutive list.

 

# Input list initialization

Input = [12, 13, 14, 17, 18, 23, 24, 25,
25, 26, 27]

 

# Output list initialization

Output = [] 

temp = [] 

last = -1

 

# Iteration

for elem in Input:

 if elem - last == 1:

 temp.append(last)

 else:

 temp.append(last)

 Output.append(temp)

 temp = []

 last = elem

 

ans = []

most = 0

 

for elem in Output:

 if len(elem)> most:

 most = len(elem)

 ans = elem

 

# Printing output

print("Initial List is")

print(Input)

print("Longest Consecutive list is :")

print(ans)  
  
---  
  
 __

 __

 **Output:**

    
    
    Initial List is
    [12, 13, 14, 17, 18, 23, 24, 25, 25, 26, 27]
    Longest Consecutive list is :
    [23, 24, 25]
    

**Method 2: Using groupby and zip**  
Using Groupby and zip is the most elegant way to print the longest consecutive
list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to print longest consecutive list.

 

# Importing

from itertools import groupby

 

# List Initialization

Input = [1, 2, 3, 5, 6, 6, 7, 9, 10,
11, 13, 14, 15, 16, 16, 17, 18, 20,
21]

 

# Using zip

z = zip(Input, Input[1:])

 

# Using groupby

lis = [list(y) for i, y in groupby(z, key = lambda x:
(x[1] - x[0]) == 1)]

 

# Taking max according to keylength

out = max(lis, key = len)

 

# Output list Initialization

output = []

 

for elem in out:

 output.append(elem[0])

 output.append(elem[1])

 

# Converting to set

output = list(set(output))

 

# Sorting outpput

output.sort()

 

# Printing answer

print("Intial list is ")

print(Input)

print("Longest Consecutive list is:")

print(output)  
  
---  
  
 __

 __

    
    
    **Output:**
    Intial list is 
    [1, 2, 3, 5, 6, 6, 7, 9, 10, 11, 13, 14, 15, 16, 16, 17, 18, 20, 21]
    Longest Consecutive list is:
    [13, 14, 15, 16]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

