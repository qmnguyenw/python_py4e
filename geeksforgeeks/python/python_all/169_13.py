Sort numeric strings in a list in Python



Sorting list is an easy task and has been dealt with in many situations. With
Machine Learning and Data Science emerging, sometimes we can get the data in
the format of list of numbers but with string as data type. Generic Sort
functions give erroneous result in that case, hence, several other methods
have to employed to perform this particular task. Let’s discuss ways in which
this is performed.  

 **Method #1 : Naive Method**  
In the naive method requires the type conversion of all the elements into
integers of the list iterated through a loop. After that generic sort function
is employed to perform the task.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# numeric string sorting

# using naive method 

 

# initializing list 

test_list = [ '4', '6', '7', '2', '1']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using naive method 

# numeric string sorting

for i in range(0, len(test_list)) :

 test_list[i] = int(test_list[i])

test_list.sort()

 

# printing result

print ("The resultant sorted list : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

    
    
    The original list is : ['4', '6', '7', '2', '1']
    The resultant sorted list  : [1, 2, 4, 6, 7]
    

  
**Method #2 : Usingsort() using key**  
The generic sort() can be used to perform this particular task, but has to be
specified with the key as integer to convert it to integer while performing
sort function internally.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# numeric string sorting

# using sort() + key

 

# initializing list 

test_list = [ '4', '6', '7', '2', '1']

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using sort() + key

# numeric string sorting

test_list.sort(key = int)

 

# printing result

print ("The resultant sorted list : " + str(test_list))  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    The original list is : ['4', '6', '7', '2', '1']
    The resultant sorted list  : ['1', '2', '4', '6', '7']
    

