Python | Check whether two lists follow same pattern or not



Given two lists ![A](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e63249dbcb7bc1df2ae6aa725a10a1ad_l3.png) and
![B](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e87b11a274ac203c994e721bfef1cc87_l3.png), check if they
follow the same pattern or not.  
Condition for pattern matching:

  1. ![Ai](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-c41f9cd8e05cb3d413a00e62684c79ba_l3.png) > ![Aj](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-4554ae1cd24315ffa211943cbc2788f8_l3.png), then ![Bi](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f2c1b3217eecb0ad2fb8f924920c6595_l3.png) > ![Bj](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f2f4d16d611b6b0d49eafb9787c499ea_l3.png)
  2. ![Ai](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-c41f9cd8e05cb3d413a00e62684c79ba_l3.png) = ![Aj](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-4554ae1cd24315ffa211943cbc2788f8_l3.png), then ![Bi](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f2c1b3217eecb0ad2fb8f924920c6595_l3.png) = ![Bj](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f2f4d16d611b6b0d49eafb9787c499ea_l3.png)
  3. ![Ai](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-c41f9cd8e05cb3d413a00e62684c79ba_l3.png) < ![Aj](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-4554ae1cd24315ffa211943cbc2788f8_l3.png), then ![Bi](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f2c1b3217eecb0ad2fb8f924920c6595_l3.png) < ![Bj](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-f2f4d16d611b6b0d49eafb9787c499ea_l3.png),  
for all i, j.

 **Example:**

>  **Input:**  
>  2 17 100  
> 10 20 50
>
>  **Output:**  
>  YES
>
>  **Input:**  
>  5 7 10 33  
> 10 50 10 45
>
>  
>
>
>  
>
>
>  **Output:**  
>  NO

 **Approach:**  
To check if two lists follow the above pattern. Sort both lists and find the
index of previous list element in the sorted list. If indices match, then
pattern matched otherwise no pattern matched.

 **Code : Python program for checking the pattern.**

 __

 __  
 __

 __

 __  
 __  
 __

# python program for above approach

a = [5, 7, 10, 33]

b = [10, 50, 10, 45]

aa = a.copy()

bb = b.copy()

 

# sorting the list

aa.sort()

bb.sort()

 

for i in range(len(a)-1):

 

 # checking the index are same or not

 if aa[i] < aa[i + 1] and bb[i] < bb[i + 1]:

 if a.index(aa[i])== b.index(bb[i]) and a.index(aa[i +
1]) == b.index(bb[i + 1]):

 flag ="YES"

 else:

 flag ="NO"

 break

 

 elif aa[i] == aa[i + 1] and bb[i] == bb[i +
1]:

 if a.index(aa[i]) == b.index(bb[i]) and a.index(aa[i +
1]) == b.index(bb[i + 1]):

 flag = "YES"

 else:

 flag = "NO"

 break

 

 else:

 flag = "NO"

 break

 

print(flag)  
  
---  
  
 __

 __

 **Output :**

    
    
    NO
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

