Python program to find the sum of all even and odd digits of an integer list



The following article shows how given an integer list, we can produce the sum
of all its odd and even digits.

>  **Input** : test_list = [345, 893, 1948, 34, 2346]  
> **Output** :  
> Odd digit sum : 36  
> Even digit sum : 40  
> **Explanation** : 3 + 5 + 9 + 3 + 1 + 9 + 3 + 3 = 36, odd summation.  
>  **Input** : test_list = [345, 893]  
> **Output** :  
> Odd digit sum : 20  
> Even digit sum : 12  
> **Explanation** : 4 + 8 = 12, even summation.

**Method 1 :** Using loop, str() and int()

In this, we first convert each element to string and then iterate for each of
its element, and add to respective summation by conversion to integer.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# initializing list

test_list = [345, 893, 1948, 34, 2346]

 

# printing original list

print("The original list is : " + str(test_list))

 

odd_sum = 0

even_sum = 0

 

for sub in test_list:

 for ele in str(sub):

 

 # adding in particular summation according to value 

 if int(ele) % 2 == 0:

 even_sum += int(ele)

 else:

 odd_sum += int(ele)

 

# printing result 

print("Odd digit sum : " + str(odd_sum))

print("Even digit sum : " + str(even_sum))  
  
---  
  
 __

 __

