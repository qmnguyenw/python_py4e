Python – Interconvert Tuple to Byte Integer



Sometimes, while working with Python data, we can have a problem in which we
need to perform conversion of tuple values, into combined byte and then to
integer and vice-versa. This kind of problem can have application in data
domains. Let’s discuss certain ways in which this task can be performed.

>  **Input** : test_tuple = (1, 2, 3, 4, 5)  
>  **Output** : 4328719365
>
>  **Input** : test_int = 4328719365  
>  **Output** : (1, 2, 3, 4, 5)

 **Method #1 : Tuple - > Byte Integer : Using int.from_bytes()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of conversion using internal function from_bytes() and
obtain the desired integer value.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Interconvert Tuple to Byte Integer

# Tuple -> Byte Integer : Using int.from_bytes()

 

# initializing tuples

test_tuple = (6, 8, 3, 2)

 

# printing original tuple

print("The original tuple : " + str(test_tuple))

 

# Interconvert Tuple to Byte Integer

# Tuple -> Byte Integer : Using int.from_bytes()

res = int.from_bytes(test_tuple, byteorder ='big')

 

# printing result 

print("Tuple after conversion : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original tuple : (6, 8, 3, 2)
    Tuple after conversion : 101188354
    

