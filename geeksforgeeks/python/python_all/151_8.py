Python | Find the sublist with maximum value in given nested list



Given a list of list, the task is to find sublist with the maximum value in
second column.

 **Examples:**

    
    
     **Input :** [['Paras', 90], ['Jain', 32], ['Geeks', 120],
                            ['for', 338], ['Labs', 532]]
    **Output :** ['Labs', 532]
    
    **Input:** [['Geek', 90], ['For', 32], ['Geeks', 120]]
    **Output:** ['Geeks', 120]
    

Below are some tasks to achieve the above task.

 **Method #1: Using lambda**

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find maximum value

# in second column of list of list

 

# Input list initialization

Input = [['Paras', 90], ['Jain', 32], ['Geeks',
120],

 ['for', 338], ['Labs', 532]]

# Using lambda 

Output = max(Input, key = lambda x: x[1])

 

# printing output

print("Input List is :", Input)

print("Output list is : ", Output)  
  
---  
  
 __

 __

 **Output:**

  

  

> Input List is : [[‘Paras’, 90], [‘Jain’, 32], [‘Geeks’, 120], [‘for’, 338],
> [‘Labs’, 532]]  
> Output list is : [‘Labs’, 532]

