Python – Unique Tuple Frequency (Order Irrespective)



Given tuple list, extract the frequency of unique tuples in list order
irrespective.

>  **Input** : test_list = [(3, 4), (1, 2), (4, 3), (3, 4)]  
>  **Output** : 2  
>  **Explanation** : (3, 4), (4, 3), (3, 4) makes 1 and (1, 2) is 2nd unique
> element.
>
>  **Input** : test_list = [(3, 7), (1, 2), (4, 3), (5, 6)]  
>  **Output** : 4  
>  **Explanation** : All are different in any order.

 **Method #1 : Usingtuple() + generator expression + sorted() + len()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of sorting using sorted(), to remove order constraint. The
len() is used to compute size.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Unique Tuple Frequency [ Order Irrespective ]

# Using tuple() + list comprehension + sorted() + len()

 

# initializing lists

test_list = [(3, 4), (1, 2), (4, 3), (5,
6)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Using tuple() + list comprehension + sorted() + len()

# Size computed after conversion to set

res = len(list(set(tuple(sorted(sub)) for sub in
test_list)))

 

# printing result 

print("Unique tuples Frequency : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(3, 4), (1, 2), (4, 3), (5, 6)]
    Unique tuples Frequency : 3
    

