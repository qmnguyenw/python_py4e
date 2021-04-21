Python – Interlist Perfect Square Pairs



Sometimes, while working in Mathematics domain, we can have a problem in which
we need to check if product of elements from different lists can lead to
perfect square or not. This can have application in many domains including
mathematics and web development. Lets discuss certain ways in which this task
can be performed.

 **Method #1 : Using loop**  
This task can be performed using loop. This is brute force way in which we can
perform this task. In this, we multiple each element with other and check if
it is perfect square.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Interlist Perfect Square Pairs

# using loop

 

# Initializing lists

test_list1 = [4, 5, 6, 7, 3, 4]

test_list2 = [6, 4, 2, 8, 9, 4]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Flatten List to individual elements

# using chain() + isinstance()

res = []

idx = 0

while(idx < len(test_list1)):

 j = 0

 while(j < len(test_list2)):

 sub = test_list1[idx] * test_list2[j]

 n = sub**0.5

 temp = int(n)

 if n == temp:

 res.append((test_list1[idx], test_list2[j]))

 j = j + 1

 idx = idx + 1

 

# printing result 

print ("The perfect square pairs are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [4, 5, 6, 7, 3, 4]  
> The original list 2 is : [6, 4, 2, 8, 9, 4]  
> The perfect square pairs are : [(4, 4), (4, 9), (4, 4), (6, 6), (4, 4), (4,
> 9), (4, 4)]

  

  

**Method #2 : UsingCounter() + set() + loop + product()**  
This task can also be performed using combination of these functions. In this
we use the fact that the perfect square with always factors in pairs that is
each element factor would be even.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Interlist Perfect Square Pairs

# using Counter() + set() + loop + product()

from itertools import product

from collections import Counter

 

def prime_factors(n):

 i = 2

 factors = []

 while i * i <= n:

 if n % i:

 i += 1

 else:

 n //= i

 factors.append(i)

 if n > 1:

 factors.append(n)

 return Counter(factors)

 

# Initializing lists

test_list1 = [4, 5, 6, 7, 3, 4]

test_list2 = [6, 4, 2, 8, 9, 4]

 

# printing original lists

print("The original list 1 is : " + str(test_list1))

print("The original list 2 is : " + str(test_list2))

 

# Flatten List to individual elements

# using Counter() + set() + loop + product()

prime_fac = {idx: prime_factors(idx) for idx in set(test_list1)
| set(test_list2)}

res = set()

for a, b in product(test_list1, test_list2):

 combined_counts = prime_fac[a] + prime_fac[b]

 if all(v % 2 == 0 for v in
combined_counts.values()):

 res.add(tuple(sorted([a, b])))

 

# printing result 

print ("The perfect square pairs are : " + str(res))  
  
---  
  
 __

 __

 **Output :**

> The original list 1 is : [4, 5, 6, 7, 3, 4]  
> The original list 2 is : [6, 4, 2, 8, 9, 4]  
> The perfect square pairs are : {(4, 4), (4, 9), (6, 6)}

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

