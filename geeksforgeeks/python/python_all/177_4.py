Stormer Numbers



Given a number ‘n’, the task is to generate the first ‘n’ Stormer numbers.

A Stormer Number is a positive integer ‘i’ such that the greatest prime factor
of the term ![i*i + 1](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f97b2f6f39cc7136097591833f29bf36_l3.png) is greater than
or equal to ![2*i](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a9060543dc5ca5c15b9695c1d982239b_l3.png).  
For example, 5 is a Stormer number because the greatest prime factor of 26(i.e
5*5 + 1) is 13 which is greater than or equal to 10(i.e 2*5)

>  **Input :** 5  
>  **Output :** 1 2 4 5 6  
> Here 3 is not a Stormer number because the greatest prime  
> factor of 10(i.e 3*3 + 1) is 5, which is not greater than  
> or equal to 6(i.e 2*3)
>
>  **Input :** 10  
>  **Output :** 1 2 4 5 6 9 10 11 12 14

 **Approach:**

  

  

* For a number ‘i’, first find the largest prime factor of the number i*i + 1.
* Next, test whether that prime factor is greater than or equal to 2*i.
* If it is greater then ‘i’ is a Stormer number.

