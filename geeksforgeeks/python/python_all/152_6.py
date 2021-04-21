Python | Find sum of frequency of given elements in the list



Given two lists containing integers, the task is to find sum of frequency of
element of first list in second list.

 **Example:**

    
    
     **Input:** list1 = [1, 2, 3]
           list2 = [2, 1, 2, 1, 3, 5, 2, 3]
    
    **Output:** 7
    
    **Explanation:**
    No of time 1 occurring in list2 is :2
    No of time 2 occurring in list2 is :3
    No of time 3 occurring in list2 is :2
    Sum = 2+3+2 = 7
    

Below are some ways to achieve the above tasks.

 **Method #1:** Using sum()

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to find sum of frequency of

# element of first list in second list.

 

# List initialization

Input1 = [1, 2, 3]

Input2 = [2, 1, 2, 1, 3, 5, 2, 3]

 

# Using sum

Output = sum(Input2.count(elem) for elem in Input1)

 

# Printing output

print("Initial list are:", Input1, Input2)

print("Frequency is:", Output)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Initial list are: [1, 2, 3] [2, 1, 2, 1, 3, 5, 2, 3]
    Frequency is: 7
    

