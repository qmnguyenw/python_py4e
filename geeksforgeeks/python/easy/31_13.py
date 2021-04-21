Bisect Algorithm Functions in Python



The purpose of Bisect algorithm is to find a position in list where an element
needs to be inserted to keep the list sorted.

Python in its definition provides the bisect algorithms using the module “
**bisect** ” which allows to keep the list in sorted order after insertion of
each element. This is essential as this reduces overhead time required to sort
the list again and again after insertion of each element.

 **Important Bisection Functions**

 **1\. bisect(list, num, beg, end)** :- This function returns the **position**
in the **sorted** list, where the number passed in argument can be placed so
as to **maintain the resultant list in sorted order**. If the element is
already present in the list, the **right most position** where element has to
be inserted is returned. **This function takes 4 arguments, list which has to
be worked with, number to insert, starting position in list to consider,
ending position which has to be considered**.

 **2\. bisect_left(list, num, beg, end)** :- This function returns the
**position** in the **sorted** list, where the number passed in argument can
be placed so as to **maintain the resultant list in sorted order**. If the
element is already present in the list, the **left most position** where
element has to be inserted is returned. **This function takes 4 arguments,
list which has to be worked with, number to insert, starting position in list
to consider, ending position which has to be considered**.

  

  

 **3\. bisect_right(list, num, beg, end)** :- This function works similar to
the “ **bisect()** ” and mentioned above.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# bisect(), bisect_left() and bisect_right()

 

# importing "bisect" for bisection operations

import bisect

 

# initializing list

li = [1, 3, 4, 4, 4, 6, 7]

 

# using bisect() to find index to insert new element

# returns 5 ( right most possible index )

print ("The rightmost index to insert, so list remains sorted is : ",
end="")

print (bisect.bisect(li, 4))

 

# using bisect_left() to find index to insert new element

# returns 2 ( left most possible index )

print ("The leftmost index to insert, so list remains sorted is : ",
end="")

print (bisect.bisect_left(li, 4))

 

# using bisect_right() to find index to insert new element

# returns 4 ( right most possible index )

print ("The rightmost index to insert, so list remains sorted is : ",
end="")

print (bisect.bisect_right(li, 4, 0, 4))  
  
---  
  
 __

 __

Output:

    
    
    The rightmost index to insert, so list remains sorted is  : 5
    The leftmost index to insert, so list remains sorted is  : 2
    The rightmost index to insert, so list remains sorted is  : 4
    

Time Complexity:

    
    
    O(log(n)) -> Bisect method works on the concept of binary search

 **4\. insort(list, num, beg, end)** :- This function returns the **sorted
list after inserting number in appropriate position** , if the element is
already present in the list, the element is inserted at the **rightmost
possible position.** **This function takes 4 arguments, list which has to be
worked with, number to insert, starting position in list to consider, ending
position which has to be considered**.

 **5\. insort_left(list, num, beg, end)** :- This function returns the
**sorted list after inserting number in appropriate position** , if the
element is already present in the list, the element is inserted at the
**leftmost possible position.** **This function takes 4 arguments, list which
has to be worked with, number to insert, starting position in list to
consider, ending position which has to be considered**.

 **6\. insort_right(list, num, beg, end)** :- This function works similar to
the “insort()” as mentioned above.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate the working of

# insort(), insort_left() and insort_right()

 

# importing "bisect" for bisection operations

import bisect

 

# initializing list

li1 = [1, 3, 4, 4, 4, 6, 7]

 

# initializing list

li2 = [1, 3, 4, 4, 4, 6, 7]

 

# initializing list

li3 = [1, 3, 4, 4, 4, 6, 7]

 

# using insort() to insert 5 at appropriate position

# inserts at 6th position

bisect.insort(li1, 5)

 

print ("The list after inserting new element using insort() is : ")

for i in range(0, 7):

 print(li1[i], end=" ")

 

# using insort_left() to insert 5 at appropriate position

# inserts at 6th position

bisect.insort_left(li2, 5)

 

print("\r")

 

print ("The list after inserting new element using insort_left() is :
")

for i in range(0, 7):

 print(li2[i], end=" ")

 

print("\r")

 

# using insort_right() to insert 5 at appropriate position

# inserts at 5th position

bisect.insort_right(li3, 5, 0, 4)

 

print ("The list after inserting new element using insort_right() is :
")

for i in range(0, 7):

 print(li3[i], end=" ")  
  
---  
  
 __

 __

Output:

    
    
    The list after inserting new element using insort() is : 
    1 3 4 4 4 5 6 
    The list after inserting new element using insort_left() is : 
    1 3 4 4 4 5 6 
    The list after inserting new element using insort_right() is : 
    1 3 4 4 5 4 6 
    

Time Complexity:

    
    
    O(n) -> Inserting an element in sorted array requires traversal

This article is contributed by **Manjeet Singh**. If you like GeeksforGeeks
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

