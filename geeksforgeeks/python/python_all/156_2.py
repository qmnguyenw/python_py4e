Python | Equate two list index elements



Sometimes we need to link two list from the point of view of their index
elements and this kind of problem comes mostly in places where we need to
display in formatted form the linkage of two lists with one another. This a
very specific problem, but can be useful whenever we need a possible solution.
Let’s discuss certain ways in which this can be done.

 **Method #1 : Using formatting +tuple()**  
The string formatting can be used to specify the way we need to output the
list and the task of pairing the like indices can be done with the help of
tuple function.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Equate two list index elements

# using formatting + tuple()

 

# initializing lists 

test_list1 = ['GeeksforGeeks', 'is', 'best']

test_list2 = ['1', '2', '3']

 

# printing original lists 

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# using formatting + tuple() to

# Equate two list index elements

temp = len(test_list1) * '% s = %% s, '

res = temp % tuple(test_list1) % tuple(test_list2)

 

# printing result

print ("The paired elements string is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['GeeksforGeeks', 'is', 'best']
    The original list 2 is : ['1', '2', '3']
    The paired elements string is : GeeksforGeeks = 1, is = 2, best = 3, 
    

**Method #2 : Usingjoin() + zip()**  
These two methods can also combine to achieve this particular task, the join
function can be used to extend the format logic to all indices and construct a
string, zip function pairs the like index elements from both the tuples.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Equate two list index elements

# using join() + zip()

 

# initializing lists 

test_list1 = ['GeeksforGeeks', 'is', 'best']

test_list2 = ['1', '2', '3']

 

# printing original lists 

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# using join() + zip() to

# Equate two list index elements

res = ', '.join('% s = % s' % i for i in
zip(test_list1, test_list2))

 

# printing result

print ("The paired elements string is : " + res)  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 is : ['GeeksforGeeks', 'is', 'best']
    The original list 2 is : ['1', '2', '3']
    The paired elements string is : GeeksforGeeks = 1, is = 2, best = 3, 
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

