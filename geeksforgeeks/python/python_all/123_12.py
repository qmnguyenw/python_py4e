Python | List of float to string conversion



Sometimes, while working with Python list, we can have a problem in which we
have to transform the list elements to string. This is easier in case of
integral list, as they can be joined easily with join(), and their contents
can be displayed. But the case with floats is different, there are additional
undesired spaces among it’s values that can cause it’s unsuccess. Let’s
discuss a ways in which this error situation can be handled.

 **Method #1 : Using list comprehension +join() + str()**  
This task can be performed using combination of above functions. In this, we
firstly convert each element of list i.e float point number to string and then
join the resultant strings using the join().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List of float to string conversion

# using list comprehension + str() + join()

 

# initialize list

test_list = [5.8, 9.6, 10.2, 45.3, 6.0]

 

# printing original list

print("The original list is : " + str(test_list))

 

# List of float to string conversion

# using list comprehension + str() + join()

res = " ".join([str(i) for i in test_list])

 

# printing result

print("Conversion of float list to string : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5.8, 9.6, 10.2, 45.3, 6.0]
    Conversion of float list to string : 5.8 9.6 10.2 45.3 6.0
    

**Method #2 : Usingjoin() + map() + str()**  
The root method is similar by using the combination of join() + str(), but
important function which helps to perform this task is map(). This first
converts each element to string and then constructs the master string.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# List of float to string conversion

# using join() + map() + str()

 

# initialize list

test_list = [5.8, 9.6, 10.2, 45.3, 6.0]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert float list to string

# using join() + map() + str()

res1 = " ".join(str(test_list))

 

# List of float to string conversion

# using join() + map() + str()

res2 = " ".join(map(str, test_list))

 

# printing result

print("Conversion using join + str : " + str(res1))

print("Conversion using join + str + map : " + str(res2))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [5.8, 9.6, 10.2, 45.3, 6.0]
    Conversion using join + str : [ 5 . 8,   9 . 6,   1 0 . 2,   4 5 . 3,   6 . 0 ]
    Conversion using join + str + map : 5.8 9.6 10.2 45.3 6.0
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

