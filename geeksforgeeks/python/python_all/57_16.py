Python – Remove Similar Rows from Tuple Matrix



Sometimes, while working with Tuple Matrix, we can have a problem in which we
get lots of data, which are similar, i.e elements are same in rows, just the
ordering of tuples is different, it’s sometimes, desired to get them removed.
This kind of problem can have application in domains such as web development
and day-day programming. Let’s discuss certain ways in which this task can be
performed.

>  **Input** : test_list = [[(4, 5), (3, 2)], [(3, 2), (4, 5)], [(3, 2), (4,
> 5)]]  
>  **Output** : {((4, 5), (3, 2))}
>
>  **Input** : test_list = [[(4, 6), (3, 2)], [(3, 2), (4, 5)], [(3, 2), (4,
> 5)]]  
>  **Output** : {((3, 2), (4, 6)), ((4, 5), (3, 2))}

 **Method #1 : Usingset() + tuple() + sorted() \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we first, perform the sorting, and then convert the rows to set, which
automatically removes the duplicates.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Remove Similar Rows from Tuple Matrix

# Using set() + tuple() + sorted() + list comprehension

 

# initializing lists

test_list = [[(4, 5), (3, 2)], [(2, 2), (4,
6)], [(3, 2), (4, 5)]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Remove Similar Rows from Tuple Matrix

# Using set() + tuple() + sorted() + list comprehension

res = set([tuple(set(sub)) for sub in test_list])

 

# printing result 

print("Tuple matrix after removal : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [[(4, 5), (3, 2)], [(2, 2), (4, 6)], [(3, 2), (4, 5)]]
    Tuple matrix after removal : {((4, 6), (2, 2)), ((4, 5), (3, 2))}
    

