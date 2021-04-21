Python – Add list elements to tuples list



Sometimes, while working with Python tuples, we can have a problem in which we
need to add all the elements of a particular list to all tuples of a list.
This kind of problem can come in domains such as web development and day-day
programming. Let’s discuss certain ways in which this task can be done.

>  **Input** : test_list = [(5, 6), (2, 4), (5, 7), (2, 5)], sub_list = [5, 4]  
>  **Output** : [(5, 6, 5, 4), (2, 4, 5, 4), (5, 7, 5, 4), (2, 5, 5, 4)]
>
>  **Input** : test_list = [(5, 6), (2, 4), (5, 7), (2, 5)], sub_list = [5]  
>  **Output** : [(5, 6, 5), (2, 4, 5), (5, 7, 5), (2, 5, 5)]

 **Method #1 : Using list comprehension +"+" operator**  
The combination of above functionalities can be used to solve this problem. In
this, we perfrom task of adding tuple to list using “+” operator and iteration
over all tuples is done using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Add list elements to tuples list

# Using list comprehension + "+" operator

 

# initializing list

test_list = [(5, 6), (2, 4), (5, 7), (2,
5)]

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing list 

sub_list = [7, 2, 4, 6]

 

# Add list elements to tuples list

# Using list comprehension + "+" operator

res = [sub + tuple(sub_list) for sub in test_list]

 

# printing result 

print("The modified list : " + str(res))   
  
---  
  
__

__

**Output :**

  

  

    
    
    The original list is : [(5, 6), (2, 4), (5, 7), (2, 5)]
    The modified list : [(5, 6, 7, 2, 4, 6), (2, 4, 7, 2, 4, 6), (5, 7, 7, 2, 4, 6), (2, 5, 7, 2, 4, 6)]
    

