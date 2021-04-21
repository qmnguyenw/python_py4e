Python – Tuple List intersection (Order irrespective)



Given list of tuples, perform tuple intersection of elements irrespective of
their order.

>  **Input** : test_list1 = [(3, 4), (5, 6)], test_list2 = [(5, 4), (4, 3)]  
>  **Output** : {(3, 4)}  
>  **Explanation** : (3, 4) and (4, 3) are common, hence intersection ( order
> irrespective).
>
>  **Input** : test_list1 = [(3, 4), (5, 6)], test_list2 = [(5, 4), (4, 5)]  
>  **Output** : set()  
>  **Explanation** : No intersecting element present.

 **Method #1 : Usingsorted() + set() + & operator \+ list comprehension**  
The combination of above functions can be used to solve this problem. In this,
we sort the tuples, and perform intersection using & operator.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Tuple List intersection [ Order irrespective ]

# Using sorted() + set() + & operator + list comprehension

 

# initializing lists

test_list1 = [(3, 4), (5, 6), (9, 10), (4,
5)]

test_list2 = [(5, 4), (3, 4), (6, 5), (9,
11)]

 

# printing original list

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Using sorted() + set() + & operator + list comprehension

# Using & operator to intersect, sorting before performing intersection

res = set([tuple(sorted(ele)) for ele in test_list1]) &
set([tuple(sorted(ele)) for ele in test_list2])

 

# printing result 

print("List after intersection : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list 1 is : [(3, 4), (5, 6), (9, 10), (4, 5)]
    The original list 2 is : [(5, 4), (3, 4), (6, 5), (9, 11)]
    List after intersection : {(4, 5), (3, 4), (5, 6)}
    

