Python | Sort a list according to the second element in sublist



In this article, we will learn how to sort any list, according to the second
element of the sublist present within the main list. We will see two methods
of doing this. We will learn three methods of performing this sort. One by the
use of Bubble Sort, second by using the sort() method and last but not the
least by the use of sorted() method. In this program, we have sorted the list
in ascending order.  
Examples:

    
    
    Input : [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
    Output : [['akash', 5], ['rishav', 10], ['gaurav', 15], ['ram', 20]]
    
    Input : [['452', 10], ['256', 5], ['100', 20], ['135', 15]]
    Output : [['256', 5], ['452', 10], ['135', 15], ['100', 20]]
    

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Method 1: Using the Bubble Sort technique**  
Here we have used the technique of Bubble Sort to perform the sorting. We have
tried to access the second element of the sublists using the nested loops.
This performs the in-place method of sorting. The time complexity is similar
to the Bubble Sort i.e., O(n^2)

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to sort the lists using the second element of sublists

# Inplace way to sort, use of third variable

def Sort(sub_li):

 l = len(sub_li)

 for i in range(0, l):

 for j in range(0, l-i-1):

 if (sub_li[j][1] > sub_li[j + 1][1]):

 tempo = sub_li[j]

 sub_li[j]= sub_li[j + 1]

 sub_li[j + 1]= tempo

 return sub_li

 

# Driver Code

sub_li =[['rishav', 10], ['akash', 5], ['ram',
20], ['gaurav', 15]]

print(Sort(sub_li))  
  
---  
  
 __

 __

Output:

    
    
    [['akash', 5], ['rishav', 10], ['gaurav', 15], ['ram', 20]]
    

**Method 2: Sorting by the use of sort() method**  
While sorting via this method the actual content of the tuple is changed, and
just like the previous method, in-place method of sort is performed.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to sort the tuples using second element

# of sublist Inplace way to sort using sort()

def Sort(sub_li):

 

 # reverse = None (Sorts in Ascending order)

 # key is set to sort using second element of 

 # sublist lambda has been used

 sub_li.sort(key = lambda x: x[1])

 return sub_li

 

# Driver Code

sub_li =[['rishav', 10], ['akash', 5], ['ram',
20], ['gaurav', 15]]

print(Sort(sub_li))  
  
---  
  
 __

 __

Output:

    
    
    [['akash', 5], ['rishav', 10], ['gaurav', 15], ['ram', 20]]
    

**Method 3: Sorting by the use of sorted() method**  
Sorted() sorts a list and always returns a list with the elements in a sorted
manner, without modifying the original sequence. It takes three parameters
from which two are optional, here we tried to use all of the three:

  1. Iterable : sequence (list, tuple, string) or collection (dictionary, set, frozenset) or any other iterator that needs to be sorted.
  2. Key(optional) : A function that would server as a key or a basis of sort comparison.
  3. Reverse(optional) : To sort this in ascending order we could have just ignored the third parameter, which we did in this program. If set true, then the iterable would be sorted in reverse (descending) order, by default it is set as false.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to sort the tuples using second element

# of sublist Function to sort using sorted()

def Sort(sub_li):

 

 # reverse = None (Sorts in Ascending order)

 # key is set to sort using second element of 

 # sublist lambda has been used

 return(sorted(sub_li, key = lambda x: x[1])) 

 

# Driver Code

sub_li =[['rishav', 10], ['akash', 5], ['ram',
20], ['gaurav', 15]]

print(Sort(sub_li))  
  
---  
  
 __

 __

Output:

    
    
    [['akash', 5], ['rishav', 10], ['gaurav', 15], ['ram', 20]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

