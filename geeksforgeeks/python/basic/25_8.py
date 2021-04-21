Lambda expression in Python to rearrange positive and negative numbers



Given an array of positive and negative numbers, arrange them such that all
negative integers appear before all the positive integers in the array. The
order of appearance should be maintained.

Examples:

    
    
    Input :  arr[] = [12, 11, -13, -5, 6, -7, 5, -3, -6]
    Output : arr[] = [-13, -5, -7, -3, -6, 12, 11, 6, 5]
    
    Input :  arr[] = [-12, 11, 0, -5, 6, -7, 5, -3, -6]
    Output : arr[] =  [-12, -5, -7, -3, -6, 11, 0, 6, 5]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

This problem has many solutions please refer Rearrange positive and negative
numbers link, but we will solve this problem with single line of code in
python using Lambda Expression.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to rearrange positive and negative elements

def Rearrange(arr):

 

 # First lambda expression returns list of negative numbers

 # in arr.

 # Second lambda expression returns list of positive numbers

 # in arr.

 return [x for x in arr if x < 0] + [x for x
in arr if x >= 0]

 

# Driver function

if __name__ == "__main__":

 arr = [12, 11, -13, -5, 6, -7, 5,
-3, -6]

 print (Rearrange(arr))  
  
---  
  
 __

 __

Output:

  

  

    
    
    arr[] = [-13, -5, -7, -3, -6, 12, 11, 6, 5]
    

This article is contributed by **Shashank Mishra (Gullu)**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
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

