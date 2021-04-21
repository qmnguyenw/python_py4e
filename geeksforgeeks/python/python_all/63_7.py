Python – Find the maximum number of triangles with given points on three lines



Given three parallel straight lines _l1_ , _l2_ and _l3_ lying in the same
plane. Total numbers of _m_ , _n_ and _k_ points lie on the line _l1_ , _l2_ ,
_l3_ respectively. This article aims to find the maximum number of triangles
formed with vertices at these points.

 **Examples:**

>  **Input :** m = 14, n = 34, k = 114  
>  **Output :** 448708.0
>
>  **Input :** m = 95, n = 77, k = 94  
>  **Output :** 2755951.0

 **Approach-**

  

  

  1. Total number of triangle = ![\(m + n + k\)C3](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-a9d763107d03a689e495561a41e4a54f_l3.png)
  2. Number of triangle that is not valid traingle from l1 plane = ![mC3](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-73254ddd72330926fde1d744ef53456a_l3.png)
  3. Number of triangle that is not valid traingle from l2 plane = ![nC3](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-ee9a5745a136e4831b0446eb3924eb02_l3.png)
  4. Number of triangle that is not valid traingle from l3 plane = ![kC3](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-b02ab707199a965436e8e9b521367641_l3.png)
  5. so number of valid Triangle = ![\(m + n + k\)C3 - mC3 - nC3 - kC3](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-8d4dbc94a8ea3fc66e53e03595d15a2c_l3.png)

**Below is the Python code implementation of the approach.**

 __

 __  
 __

 __

 __  
 __  
 __

# Pyton code implementation

import math

def nooftriangle(m, n, k):

 

 # r1 = (m + n + k)C3

 r1 = math.factorial(m + n + k) / (

 math.factorial(3) * math.factorial(m + n + k - 3))

 # r2 = mC3

 r2 = math.factorial(m) / (math.factorial(3) *
math.factorial(m - 3))

 

 # r3 = nC3

 r3 = math.factorial(n) / (math.factorial(3) *
math.factorial(n - 3))

 

 #r4 = kC3

 r4 = math.factorial(k) / (math.factorial(3) *
math.factorial(k - 3))

 

 result = r1 - r2 - r3 - r4

 return(result) 

 

# Driver code

m = 17

n = 16

k = 11

print("Number of traingles : ", nooftriangle(m, n, k))

   
  
---  
  
__

__

**Output:**

    
    
    Number of traingles :  11839.0

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

