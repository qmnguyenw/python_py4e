Set update() in Python to do union of n arrays



We are given n arrays of any size which may have common elements, we need to
combine all these arrays in such a way that each element should occurs only
once and elements should be in sorted order?

Examples:

    
    
    Input : arr = [[1, 2, 2, 4, 3, 6],
                  [5, 1, 3, 4],
                  [9, 5, 7, 1],
                  [2, 4, 1, 3]]
    Output : [1, 2, 3, 4, 5, 6, 7, 9]
    
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

A **simple solution** for this problem is to create a empty **hash** and
traverse each array one by one, this hash contains frequency of each element
in list of arrays. Now traverse hash from start and print each index which has
non zero value.

Here we solve this problem in python very quickly using properties of Set()
data structure and **Update()** method in python.

  

  

 **How does Update() method works for set ?**

 **anySet.update(iterable)** , this method does union of set named as
**anySet** with any given **iterable** and it does not return any shallow copy
of set like **union()** method, it updates the result into prefix set i.e;
**anySet**.

 __

 __  
 __

 __

 __  
 __  
 __

# Function to combine n arrays

 

def combineAll(input): 

 

 # cast first array as set and assign it 

 # to variable named as result 

 result = set(input[0]) 

 

 # now traverse remaining list of arrays 

 # and take it's update with result variable 

 for array in input[1:]: 

 result.update(array) 

 

 return list(result) 

 

# Driver program 

if __name__ == "__main__": 

 input = [[1, 2, 2, 4, 3, 6],

 [5, 1, 3, 4],

 [9, 5, 7, 1],

 [2, 4, 1, 3]] 

 print (combineAll(input))  
  
---  
  
 __

 __

Output:

    
    
    [1, 2, 3, 4, 5, 6, 7, 9]
    

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

