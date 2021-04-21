Python – Elements frequency in Tuple Matrix



Sometimes, while working with Python Tuple Matrix, we can have a problem in
which we need to get frequency of each element in it. This kind of problem can
occur in domains such as day-day programming and web development domain. Let’s
discuss certain ways in which this problem can be solved.

>  **Input** : test_list = [[(4, 5), (3, 2)], [(2, 2)]]  
>  **Output** : {4: 1, 5: 1, 3: 1, 2: 3}
>
>  **Input** : test_list = [[(4, 5), (3, 2)]]  
>  **Output** : {4: 1, 5: 1, 3: 1, 2: 1}

 **Method #1 : Using nestedchain() + "*" operator + Counter()**  
The combination of above functions can be used to solve this problem. In this,
we perform the task of getting frequency using Counter() and nested chain to
cater the nestings and “*” operator is used to perform unpacking and packing
of each element.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Elements frequency in Tuple Matrix

# Using nested chain() + "*" operator + Counter()

from itertools import chain

from collections import Counter

 

# initializing lists

test_list = [[(4, 5), (3, 2)], [(2, 2)], [(1,
2), (5, 5)]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Elements frequency in Tuple Matrix

# Using nested chain() + "*" operator + Counter()

res = dict(Counter(chain(*chain(*test_list))))

 

# printing result 

print("Elements frequency : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [[(4, 5), (3, 2)], [(2, 2)], [(1, 2), (5, 5)]]
    Elements frequency : {4: 1, 5: 3, 3: 1, 2: 4, 1: 1}
    

