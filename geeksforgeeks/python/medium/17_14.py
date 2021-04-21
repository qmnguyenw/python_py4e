Python | Convert list of numerical string to list of Integers



Many times, the data we handle might not be in the desired form for any
application and has to go through the stage of preprocessing. One such kind of
form can be a number in form of string that too as a list in list and we need
to segregate it to be digit separated integers. Let’s discuss certain ways in
which this problem can be solved.

 **Method #1 : Using list comprehension**  
This problem can be dealt with list comprehension, as a shorthand to generic
loops that we would require to run to perform this particular task by
iterating each list’s each character of string and converting to integer.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# converting string list to integer list

# using list comprehension

 

# initializing list

test_list = [['24'], ['45'], ['78'], ['40']]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension

# converting string list to integer list

res = [[int(i) for i in sub] for i in test_list
for sub in i]

 

# print result

print("The list after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['24'], ['45'], ['78'], ['40']]
    The list after conversion : [[2, 4], [4, 5], [7, 8], [4, 0]]
    

**Method #2 : Using map() \+ list comprehension**  
The task performed in the above function can also be reduced to include the
map function which bind the conversion to integer to a function and rest of
task is performed by the list comprehension function itself.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# converting string list to integer list

# using list comprehension + map()

 

# initializing list

test_list = [['24'], ['45'], ['78'], ['40']]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension + map()

# converting string list to integer list

res = [list(map(int, list(sub[0]))) for sub in
test_list if sub ]

 

# print result

print("The list after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [['24'], ['45'], ['78'], ['40']]
    The list after conversion : [[2, 4], [4, 5], [7, 8], [4, 0]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

