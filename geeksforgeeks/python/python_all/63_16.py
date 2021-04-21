Python – Check whether the given List forms Contiguous Distinct Sub-Array or
Not



You are given an array consisting of elements in the form A1, A2,
A3.......An. The task is to find whether the array can be formed as a
**Contiguous Distinct Sub Array** or Not. You need to find whether the array
can be converted to contiguous sub-arrays that consist of similar elements and
there are a distinct number of each element.

The elements once encountered should not appear later in the array as it would
not be contiguous

 **Example:**

>  **Input:** _ **[** 1 1 3 6 6 6 ]_  
>  **Output:** _YES_  
>  **Explanation:**  
>  **** _The given elements of the can be converted to Contiguous Distinct Set
> Array in the form of [1, 1] [3] [6, 6, 6]and also_  
>  _no. of 1’s = 2_  
>  _no. of 3’s = 1_  
>  _no. of 6’s = 3_  
>  _which are distinct_
>
>  **Input:** _[ 1 1 3 5 2 2 2 3 ]_  
>  **Output:** _NO_  
>  **Explanation:**  
>  _The given elements of the cannot be converted to Contiguous Distinct Set
> Array as sub arrray [3 5 2 2 2 3]_  
>  _violates the condition(elements need to be contiguous) 3 again appears
> after 5 and 2._
>
>  **Input** _ **:** [9 9 4 4 4 1 6 6]_  
>  **Output:** _NO_  
>  **Explanation:**  
>  _The given elements of the cannot be converted to Contiguous Distinct Set
> Array_  
>  _It is of the form [9, 9] [4, 4, 4] [1] [6, 6] So the elements are present
> contiguous_  
>  _But the no. of 9’s=2 which is also equal to the no. of 6’s=2_  
>  _Hence the no.s of different elements of the array are not Distinct_  
>  _hence the Answer is NO_

 **Solution:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

from collections import Counter

 

# function to check contiguous 

# distinct set arrray

def contig_distinct_setarr(l, n):

 

 c = Counter(l)

 a = list(set(l))

 

 b =[]

 flag = True

 

 for j in c.values():

 

 # iterating and moving it to another

 # array if already present we print NO

 # when it finds no. of different elements 

 # to be equal if no. of x's = no. of y's

 # So we break of the loop

 if j not in b:

 b.append(j)

 else:

 print("NO")

 flag = False

 break

 

 # If already there are similar elements

 # in c.values()- the count of elements

 # flag = False and we dont need to check

 # the below condition If not flag = False 

 # then the iterate through the array loop

 if (flag != False):

 i, k = 0, 0

 

 # for each elements in set a

 # cou stores the count of a[i]

 while k<len(a):

 cou = c[a[i]]

 x = l.index(a[i])

 

 # here we extract thecontiguous

 # sub array of length equal to 

 # the count of the element 

 temp =(l[x:x + cou])

 

 # if the number of elements of

 # subsequences is not equal to

 # the value of element in the 

 # dictionary print NO

 if len(temp) != c[a[i]]:

 print("NO")

 flag = False

 break

 

 k+= 1

 i+= 1

 

 # if we have iterated all over the array 

 # and the condition is satisfied we print

 # YES

 if flag == True:

 print("YES")

# initialize the array and its length

n = 6

l =[1, 1, 3, 6, 6, 6]

contig_distinct_setarr(l, n)  
  
---  
  
 __

 __

 **Output:**

    
    
    YES

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

