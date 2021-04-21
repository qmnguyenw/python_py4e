Output of Python program | Set 5



Predict the output of the following programs:

 **Program 1:**

 __

 __  
 __

 __

 __  
 __  
 __

def gfgFunction():

 "Geeksforgeeks is cool website for boosting up technical skills"

 return 1

 

print (gfgFunction.__doc__[17:21])  
  
---  
  
 __

 __

 **Output:**

    
    
    cool
    

**Explanation:**  
There is a docstring defined for this method, by putting a string on the first
line after the start of the function definition. The docstring can be
referenced using the __doc__ attribute of the function.  
And hence it prints the indexed string.

 **Program 2:**

  

  

 __

 __  
 __

 __

 __  
 __  
 __

class A(object):

 val = 1

 

class B(A):

 pass

 

class C(A):

 pass

 

print (A.val, B.val, C.val)

B.val = 2

print (A.val, B.val, C.val)

A.val = 3

print (A.val, B.val, C.val)  
  
---  
  
 __

 __

 **Output:**

    
    
    1 1 1
    1 2 1
    3 2 3
    

**Explanation:**  
In Python, class variables are internally handled as dictionaries. If a
variable name is not found in the dictionary of the current class, the class
hierarchy (i.e., its parent classes) are searched until the referenced
variable name is found, if the variable is not found error is being thrown.  
So, in the above program the first call to print() prints the initialized
value i.e, 1.  
In the second call since B. val is set to 2, the output is 1 2 1.  
The last output 3 2 3 may be surprising. Instead of 3 3 3, here B.val reflects
2 instead of 3 since it is overridden earlier.

 **Program 3:**

 __

 __  
 __

 __

 __  
 __  
 __

check1= ['Learn', 'Quiz', 'Practice', 'Contribute']

check2 = check1

check3 = check1[:]

 

check2[0] = 'Code'

check3[1] = 'Mcq'

 

count = 0

for c in (check1, check2, check3):

 if c[0] == 'Code':

 count += 1

 if c[1] == 'Mcq':

 count += 10

 

print (count)  
  
---  
  
 __

 __

 **Output:**

    
    
    12
    

**Explanation:**  
When assigning check1 to check2, we create a second reference to the same
list. Changes to check2 affects check1. When assigning the slice of all
elements in check1 to check3, we are creating a full copy of check1 which can
be modified independently (i.e, any change in check3 will not affect check1).  
So, while checking check1 ‘Code’ gets matched and count increases to 1, but
Mcq doest gets matched since its available only in check3.  
Now checking check2 here also ‘Code’ gets matched resulting in count value to
2.  
Finally while checking check3 which is separate than both check1 and check2
here only Mcq gets matched and count becomes 12.

 **Program 4:**

 __

 __  
 __

 __

 __  
 __  
 __

def gfg(x,l=[]):

 for i in range(x):

 l.append(i*i)

 print(l) 

 

gfg(2)

gfg(3,[3,2,1])

gfg(3)  
  
---  
  
 __

 __

 **Output:**

    
    
    [0, 1]
    [3, 2, 1, 0, 1, 4]
    [0, 1, 0, 1, 4]
    

**Explanation:**  
The first function call should be fairly obvious, the loop appends 0 and then
1 to the empty list, l. l is a name for a variable that points to a list
stored in memory. The second call starts off by creating a new list in a new
block of memory. l then refers to this new list. It then appends 0, 1 and 4 to
this new list. So that’s great. The third function call is the weird one. It
uses the original list stored in the original memory block. That is why it
starts off with 0 and 1.

This article is contributed by **Harsh Agarwal**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
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

