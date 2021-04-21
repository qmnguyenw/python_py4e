Python – Replace K with Multiple values



Sometimes, while working with Python Strings, we can have a problem in which
we need to perform replace of single character/work with particular list of
values, based on occurrence. This kind of problem can have application in
school and day-day programming. Let’s discuss certain ways in which this task
can be performed.

>  **Input** : test_str = ‘* is * . It is recommended for *’, repl_char = ‘*’,  
> repl_list = [‘Gfg’, ‘Best’, ‘CS’]  
>  **Output** : Gfg is Best . It is recommended for CS
>
>  **Input** : test_str = ‘* is *’, repl_char = ‘*’,  
> repl_list = [‘Gfg’, ‘Best’]  
>  **Output** : Gfg is Best

 **Method #1 : Using loop +replace()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of replacing using replace() and increase the index
counter after each replacment.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Replace K with Multiple values

# Using loop + replace()

 

# initializing strings

test_str = '_ is _ . It is recommended for _'

 

# printing original string

print("The original string is : " + str(test_str))

 

# initializing repl_char

repl_char = '_'

 

# initializing repl_list 

repl_list = ['Gfg', 'Best', 'CS']

 

# Replace K with Multiple values

# Using loop + replace()

for ele in repl_list:

 test_str = test_str.replace(repl_char, ele, 1)

 

# printing result 

print("String after replacement : " + str(test_str))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original string is : _ is _ . It is recommended for _
    String after replacement : Gfg is Best . It is recommended for CS
    

