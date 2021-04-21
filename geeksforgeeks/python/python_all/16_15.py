Python program to multiply all the items in a dictionary



Python program to illustrate multiply all the items in a dictionary could be
done by creating a dictionary which will store all the key-value pairs,
multiplying the value of all the keys and storing it in a variable.

 **Example:**

>  **Input:** dict = {‘value1’:5, ‘value2’:4, ‘value3’:3, ‘value4’:2,
> ‘value5’:1}  
>  **Output:** ans = 120
>
>  **Input:** dict **=** {‘v1’:10, ‘v2’:7, ‘v3’:2}  
>  **Output:** ans = 140

 **Approach:**

  

  

  * Create a dictionary d and store key-value pairs in it.
  * Create a variable answer initialized to 1.
  * Run a loop to traverse through the dictionary d
  * Multiply each value of key with answer and store the result in answer itself.
  * Print answer.

Below are the examples of above approach.

 **Example 1:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# create a dictionary

d = {

 'value1': 5,

 'value2': 4,

 'value3': 3,

 'value4': 2,

 'value5': 1,

}

 

# create a variable to store result

answer = 1

 

# run a loop

for i in d:

 answer = answer*d[i]

 

# print answer

print(answer)  
  
---  
  
 __

 __

 **Output**

    
    
    120
    

**Example 2:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# create a dictionary

d = {

 'a': 10,

 'b': 7,

 'c': 2,

}

 

# create a variable to store result

answer = 1

 

# run a loop

for i in d:

 answer = answer*d[i]

 

# print answer

print(answer)  
  
---  
  
 __

 __

 **Output**

    
    
    140
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

