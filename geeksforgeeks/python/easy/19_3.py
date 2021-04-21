Is sizeof for a struct equal to the sum of sizeof of each member?



 **Prerequisite :** sizeof operator in C  
The sizeof for a struct is not always equal to the sum of sizeof of each
individual member. This is because of the padding added by the compiler to
avoid alignment issues. Padding is only added when a structure member is
followed by a member with a larger size or at the end of the structure.

Different compilers might have different alignment constraints as C standards
state that alignment of structure totally depends on the implementation.

Let’s take a look at the following examples for better understanding:

  *  **Case 1:**

 __

 __  
 __

 __

 __  
 __  
 __

// C program to illustrate

// size of struct

#include <stdio.h>

 

int main()

{

 

 struct A {

 

 // sizeof(int) = 4

 int x;

 // Padding of 4 bytes

 

 // sizeof(double) = 8

 double z;

 

 // sizeof(short int) = 2

 short int y;

 // Padding of 6 bytes

 };

 

 printf("Size of struct: %ld", sizeof(struct A));

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    Size of struct: 24
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/struct_sizeof_ex1-300x154.png)  
The red portion represents the padding added for data alignment and the green
portion represents the struct members. In this case, **x** (int) is followed
by **z** (double), which is larger in size as compared to **x**. Hence padding
is added after **x**. Also, padding is needed at the end for data alignment.

  *  **Case 2:**

 __

 __  
 __

 __

 __  
 __  
 __

// C program to illustrate

// size of struct

#include <stdio.h>

 

int main()

{

 

 struct B {

 // sizeof(double) = 8

 double z;

 

 // sizeof(int) = 4

 int x;

 

 // sizeof(short int) = 2

 short int y;

 // Padding of 2 bytes

 };

 

 printf("Size of struct: %ld", sizeof(struct B));

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Size of struct: 16
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/struct_sizeof_ex2-300x124.png)

In this case, the members of the structure are sorted in decreasing order of
their sizes. Hence padding is required only at the end.

  *  **Case 3:**

 __

 __  
 __

 __

 __  
 __  
 __

// C program to illustrate

// size of struct

#include <stdio.h>

 

int main()

{

 

 struct C {

 // sizeof(double) = 8

 double z;

 

 // sizeof(short int) = 2

 short int y;

 // Padding of 2 bytes

 

 // sizeof(int) = 4

 int x;

 };

 

 printf("Size of struct: %ld", sizeof(struct C));

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    Size of struct: 16
    

![](https://media.geeksforgeeks.org/wp-
content/uploads/struct_sizeof_ex3-300x128.png)  
In this case, **y** (short int) is followed by **x** (int) and hence padding
is required after **y**. No padding is needed at the end in this case for data
alignment.

C language doesn’t allow the compilers to reorder the struct members to reduce
the amount of padding. In order to minimize the amount of padding, the struct
members must be sorted in a descending order (similar to the case 2).

Want to learn from the best curated videos and practice problems, check out
the **C Foundation Course **for Basic to Advanced C.

My Personal Notes _arrow_drop_up_

Save

