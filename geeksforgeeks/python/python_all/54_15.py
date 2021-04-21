Python – Row Summation of Like Index Product



Given a Matrix and elements list, For every row, extract the summation of
product of elements with argument list.

>  **Input** : test_list = [[4, 5], [1, 5], [8, 2]], mul_list = [5, 2, 3]  
>  **Output** : [30, 15, 44]  
>  **Explanation** : For 1st row, (4*5) + (5*2) = 30, as value of 1st element
> of result list. This way each element is computed.
>
>  **Input** : test_list = [[4, 5, 8, 2]], mul_list = [5, 2, 3, 9]  
>  **Output** : [72]  
>  **Explanation** : Similar computation as above method. Just 1 element as
> single Row.

 **Method #1 : Using loop**  
This is brute force way to solve this problem. In this, we perform iteration
of each row and perform required summation in product using brute force
approach using loop.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Row Summation of Like Index Product

# Using loop

 

# initializing list

test_list = [[3, 4, 5], [1, 7, 5], [8, 1,
2]] 

 

# printing original list

print("The original list is : " + str(test_list))

 

# initializing mul list 

mul_list = [5, 2, 3]

 

# Using loop

res = []

for sub in test_list:

 sum = 0

 for idx, ele in enumerate(sub):

 

 # performing summation of product with list elements

 sum = sum + (ele * mul_list[idx])

 

 # adding each row sum

 res.append(sum)

 

# printing result 

print("List after multiplication : " + str(res))  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    The original list is : [[3, 4, 5], [1, 7, 5], [8, 1, 2]]
    List after multiplication : [38, 34, 48]
    

