Python | Print list elements in circular range



Given a list of elements, the task is to print element in group of _k_ till
_n-iteration_ in circular range.

 **Examples:**

    
    
     **Input:** list = [1, 2, 3, 4, 5, 6, 7], k = 3, n =10
    **Output:** 
    [1, 2, 3]
    [4, 5, 6]
    [7, 1, 2]
    [3, 4, 5]
    [6, 7, 1]
    [2, 3, 4]
    [5, 6, 7]
    [1, 2, 3]
    [4, 5, 6]
    [7, 1, 2]
    
    **Input:** list = [10, 20, 30, 40, 50, 60, 70], k = 4, n = 5
    **Output:** 
    [10, 20, 30, 40]
    [50, 60, 70, 10]
    [20, 30, 40, 50]
    [60, 70, 10, 20]
    [30, 40, 50, 60]
    

  
We can use itertools with zip

