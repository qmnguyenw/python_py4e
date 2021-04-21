Python – Find the frequency of numbers greater than each element in a list



Given a list, a new list is constructed that has frequency of elements greater
than or equal to it, corresponding to each element of the list.

>  **Input** : test_list = [6, 3, 7, 1, 2, 4]  
> **Output** : [2, 4, 1, 6, 5, 3]  
> **Explanation** : 6, 7 are greater or equal to 6 in list, hence 2.  
>  **Input** : test_list = [6, 3, 7]  
> **Output** : [2, 3, 1]  
> **Explanation** : 6, 7 are greater or equal to 6 in list, hence 2.

**Method 1 :** _Using_ _sum()_ _and_ _list comprehension_

Here, nested list comprehension is used to access each element of the list and
sum() is used to get summation of elements which are greater than or equal to
the indexed element.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [6, 3, 7, 1, 2, 4]

 

# printing original list

print("The original list is : " + str(test_list))

 

# sum() performs counts of element which are Greater or equal to 

res = [sum(1 for ele in test_list if sub <= ele)
for sub in test_list] 

 

# printing result 

print("Greater elements Frequency list : " + str(res))  
  
---  
  
 __

 __

