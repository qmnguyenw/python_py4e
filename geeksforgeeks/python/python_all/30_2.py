Python – Convert Integer Matrix to String Matrix



Given a Matrix with integer values, convert each element to String.

>  **Input** : test_list = [[4, 5, 7], [10, 8, 3], [19, 4, 6]]  
>  **Output** : [[‘4’, ‘5’, ‘7’], [’10’, ‘8’, ‘3’], [’19’, ‘4’, ‘6’]]  
>  **Explanation** : All elements of Matrix converted to Strings.
>
>  **Input** : test_list = [[4, 5, 7], [10, 8, 3]]  
>  **Output** : [[‘4’, ‘5’, ‘7’], [’10’, ‘8’, ‘3’]]  
>  **Explanation** : All elements of Matrix converted to Strings.

 **Method #1 : Using str() + list comprehension**

The combination of above methods can be used to solve this problem. In this,
we perform conversion using str() and list comprehension is used to iterate
for all the elements.

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Integer Matrix to String Matrix

# Using str() + list comprehension

 

# initializing list

test_list = [[4, 5, 7], [10, 8, 3], [19,
4, 6], [9, 3, 6]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using str() to convert each element to string 

res = [[str(ele) for ele in sub] for sub in
test_list]

 

# printing result 

print("The data type converted Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[4, 5, 7], [10, 8, 3], [19, 4, 6], [9, 3, 6]]
    The data type converted Matrix : [['4', '5', '7'], ['10', '8', '3'], ['19', '4', '6'], ['9', '3', '6']]
    

**Method #2 : Using str() + map()**

The combination of above functions can also be used to solve this problem. In
this, we use map() to extend the string conversion to all row elements.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert Integer Matrix to String Matrix

# Using str() + map()

 

# initializing list

test_list = [[4, 5, 7], [10, 8, 3], [19,
4, 6], [9, 3, 6]]

 

# printing original list

print("The original list : " + str(test_list))

 

# using map() to extend all elements as string 

res = [list(map(str, sub)) for sub in test_list]

 

# printing result 

print("The data type converted Matrix : " + str(res))  
  
---  
  
 __

 __

 **Output**

    
    
    The original list : [[4, 5, 7], [10, 8, 3], [19, 4, 6], [9, 3, 6]]
    The data type converted Matrix : [['4', '5', '7'], ['10', '8', '3'], ['19', '4', '6'], ['9', '3', '6']]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

