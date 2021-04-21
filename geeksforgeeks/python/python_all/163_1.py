Python | Find maximum length sub-list in a nested list



Given a list of lists, write a Python program to find the list with maximum
length. The output should be in the form _(list, list_length)_.

 **Examples:**

    
    
    **Input :** [['A'], ['A', 'B'], ['A', 'B', 'C']]
    **Output :** (['A', 'B', 'C'], 3)
    
    **Input :** [[1, 2, 3, 9, 4], [5], [3, 8], [2]]
    **Output :** ([1, 2, 3, 9, 4], 5)
    

  
Let’s discuss different approaches to solve this problem.

 **Approach #1 :** Using for loop (Naive)  
This is a brute force method in which we iterate through each list item(list)
and find the list with maximum length. Similarly, we use the for loop to find
length of each list and output the maximum length.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program to Find maximum

# length list in a nested list

 

def FindMaxLength(lst):

 maxList = max((x) for x in lst)

 maxLength = max(len(x) for x in lst )

 

 return maxList, maxLength

 

# Driver Code

lst = [['A'], ['A', 'B'], ['A', 'B', 'C']]

print(FindMaxLength(lst))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    (['A', 'B', 'C'], 3)
    

