Check for balanced parentheses in Python



Given an expression string, write a python program to find whether a given
string has balanced parentheses or not.

 **Examples:**

    
    
    **Input :** {[]{()}}
    **Output :** Balanced
    
    **Input :** [{}{}(]
    **Output :** Unbalanced
    

**Approach #1 :** Using stack

One approach to check balanced parentheses is to use stack. Each time, when an
open parentheses is encountered push it in the stack, and when closed
parenthesis is encountered, match it with the top of stack and pop it. If
stack is empty at the end, return Balanced otherwise, Unbalanced.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to Check for

# balanced parentheses in an expression

open_list = ["[","{","("]

close_list = ["]","}",")"]

 

# Function to check parentheses

def check(myStr):

 stack = []

 for i in myStr:

 if i in open_list:

 stack.append(i)

 elif i in close_list:

 pos = close_list.index(i)

 if ((len(stack) > 0) and

 (open_list[pos] == stack[len(stack)-1])):

 stack.pop()

 else:

 return "Unbalanced"

 if len(stack) == 0:

 return "Balanced"

 else:

 return "Unbalanced"

 

 

# Driver code

string = "{[]{()}}"

print(string,"-", check(string))

 

string = "[{}{})(]"

print(string,"-", check(string))

 

string = "((()"

print(string,"-",check(string))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    {[]{()}} - Balanced
    [{}{})(] - Unbalanced
    ((() - Unbalanced
    

