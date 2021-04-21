Python | Truncate a list



Sometimes there is a requirement to restrict the list size to a particular
number and remove all the elements from list which occur after a certain
number as decided as list size. This is a useful utility for web development
using Python. Let’s discuss certain ways in which this can be performed.

 **Method #1 : Usingpop()**  
pop function can be repeated a number of times till size of the list reaches
the threshold required as the size of the list. This uses a whole loop and
hence is comparatively tedious.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to truncate list using pop()

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 3, 8, 9,
10]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# size desired

k = 5

 

# using pop()

# to truncate list 

n = len(test_list)

for i in range(0, n - k ):

 test_list.pop()

 

# printing result

print ("The truncated list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : [1, 4, 5, 6, 7, 3, 8, 9, 10]
    The truncated list is : [1, 4, 5, 6, 7]
    

  
**Method #2 : Using del + list slice**  
del operator can be used to delete all the elements that appear after the
specific index, which is handled by the list slicing technique.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to truncate list 

# using del + list slicing

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 3, 8, 9,
10]

 

# printing original list

print ("The original list is : " + str(test_list))

 

# size desired

k = 5

 

# using del + list slicing

# to truncate list 

del test_list[5:]

 

# printing result

print ("The truncated list is : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list is : [1, 4, 5, 6, 7, 3, 8, 9, 10]
    The truncated list is : [1, 4, 5, 6, 7]
    

