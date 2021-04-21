Python – Custom Pool Sorting



Given list and priority lists, sort the list elements on basis of their
occurrence in priority lists, i.e element occurring in list1, should occur 1st
and in other list should occur after that.

>  **Input** : test_list = [5, 6, 3, 7], prio1_list = [6, 3], prio2_list = [5,
> 7]  
>  **Output** : [6, 3, 5, 7]  
>  **Explanation** : 6, 3 occur in p1 list, followed by 5 and 7 which lie in
> p2 list.
>
>  **Input** : test_list = [5, 6], prio1_list = [6], prio2_list = [5]  
>  **Output** : [6, 5]  
>  **Explanation** : 6 occurs in 1st priority list than 5.

 **Method : Usingsort() \+ comparator key function**  
The generic sort() can be used to perform this task. The real algorithm lies
in comparator function passed in it. The assignment of appropriate return
value and its order is used to solve this problem.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Custom Pool Sorting

# Using sort() + comparator key function

 

# comparator function

def func(ele):

 

 # Returning 1 or 2 ro assign priority

 if ele in prio1_list:

 return 1

 elif ele in prio2_list:

 return 2

 

# initializing list

test_list = [5, 6, 3, 7, 4, 2, 9, 10] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing priority lists

prio1_list = [4, 6, 3, 8, 10]

prio2_list = [5, 7, 1, 2, 9]

 

# Using sort() + comparator key function

# key passed with function to manage priority

test_list.sort(key = func)

 

# printing result 

print("List after sorting : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [5, 6, 3, 7, 4, 2, 9, 10]
    List after sorting : [6, 3, 4, 10, 5, 7, 2, 9]
    

