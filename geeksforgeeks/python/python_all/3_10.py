Python Program to print sum of all key value pairs in a Dictionary



Given a dictionary **arr** consisting of **N** items, where key and value are
both of integer type, the task is to find the sum of all key value pairs in
the dictionary.

 **Examples:**

>  **Input:** arr = {1: 10, 2: 20, 3: 30}  
>  **Output:** 11 22 33  
>  **Explanation:**  
> Sum of key and value of the first item in the dictionary = 1 + 10 = 11.  
> Sum of key and value of the second item in the dictionary = 2 + 20 = 22.  
> Sum of key and value of the third item in the dictionary = 3 + 30 = 33.
>
>  **Input:** arr = {10 : -5, 5 : -10, 100 : -50}  
>  **Output:** 5 -5 50

 **Approach usingdictionary traversal technique: **The idea is to traverse
through the keys of dictionary using for loop. Follow the steps below to solve
the problem:

  

  

  * Initialize a list, say **l** , to store the result.
  * Traverse the dictionary **arr** and then append **i + arr[i]** into the list **l**.

