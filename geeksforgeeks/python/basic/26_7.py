Enumerate() in Python



A lot of times when dealing with iterators, we also get a need to keep a count
of iterations. Python eases the programmers’ task by providing a built-in
function enumerate() for this task.  
Enumerate() method adds a counter to an iterable and returns it in a form of
enumerate object. This enumerate object can then be used directly in for loops
or be converted into a list of tuples using list() method.  
 **Syntax:**

    
    
    enumerate(iterable, start=0)
    
    **Parameters:**
    **Iterable:** any object that supports iteration
    **Start:** the index value from which the counter is 
                  to be started, by default it is 0

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#python

# Python program to illustrate

# enumerate function

l1 = ["eat","sleep","repeat"]

s1 = "geek"

# creating enumerate objects

obj1 = enumerate(l1)

obj2 = enumerate(s1)

print ("Return type:",type(obj1))

print (list(enumerate(l1)))

# changing start index to 2 from 0

print (list(enumerate(s1,2)))  
  
---  
  
 __

 __

 **Output:**  

    
    
    Return type: < type 'enumerate' >
    [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
    [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

**Using Enumerate object in loops:**  

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to illustrate

# enumerate function in loops

l1 = ["eat","sleep","repeat"]

# printing the tuples in object directly

for ele in enumerate(l1):

 print (ele)

print

# changing index and printing separately

for count,ele in enumerate(l1,100):

 print (count,ele)  
  
---  
  
 __

 __

 **Output:**  

    
    
    (0, 'eat')
    (1, 'sleep')
    (2, 'repeat')
    
    100 eat
    101 sleep
    102 repeat

This article is contributed by **Harshit Agrawal**. If you like GeeksforGeeks
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

