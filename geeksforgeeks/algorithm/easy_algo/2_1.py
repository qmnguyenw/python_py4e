Print all possible combinations of the string by replacing ‘$’ with any other
digit from the string



Given a number as a string where some of the digits are replaced by a **‘$’**
, the task is to generate all possible number by replacing the **‘$’** with
any of the digits from the given string.

 **Examples:**

>  **Input:** str = “23$$”  
>  **Output:**  
>  2322  
> 2323  
> 2332  
> 2333
>
>  **Input:** str = “$45”  
>  **Output:**  
>  445  
> 545

## Recommended: Please try your approach on **__{IDE}__** first, before moving
on to the solution.

 **Approach:**

  

  

  * Find all the combinations of the string by replacing the character **$** with any of the digits of the string, for this check if the current character is a digit if yes then store this character into an array **pre[]** then recursively find all of its combinations else if current character is a **‘$’** then replace it with the digits stored in the array and recursively find all the combinations.
  * To find the all possible numbers initialize array **set[]** that stores all the possible numbers, to generate numbers take two nested loop outer loop is for input string and inner loop is for array **set[]** that stores all the possible combinations of the numbers. Initialize the boolean flag to check if character of the input string is already present in **set[]** or not if character of the input string is already present in **set[]** then set **flag = false** else if flag is true then move the current character of the input string to **set[]** and recursively find all the combinations of the input string and store it in the array set[]. Finally print each number from the array **set[]**

Below is the implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

// C++ implementation of the approach

#include <stdbool.h>

#include <stdio.h>

#include <string.h>

#define MAX 20

#define DIGITS 10

 

// Array to store all the

// possible numbers

char set[DIGITS];

 

// Index to set[] element

int end;

 

// Function to find all the combinations

// of the string by replacing '$' with

// the other digits of the string

void combinations(char* num, char* pre, int curr, int lvl)

{

 

 // Check if current length is less than

 // the length of the input string

 if (curr < strlen(num)) {

 

 // If current charecter is a digit

 // then store digit into pre[] and

 // recursively find all the combinations

 if (num[curr] >= '0' && num[curr] <= '9') {

 pre[lvl] = num[curr];

 combinations(num, pre, curr + 1, lvl + 1);

 }

 

 // If current charecter is a '$' then replace

 // it with the other digits of the string and

 // recursively find all the combinations

 // Else go to the next charecter and

 // recursively find all the combinations

 else if (num[curr] == '$')

 for (int i = 0; i < end; i++) {

 pre[lvl] = set[i];

 combinations(num, pre, curr + 1, lvl + 1);

 }

 else

 combinations(num, pre, curr + 1, lvl);

 }

 

 // Print the array pre[]

 else {

 pre[lvl] = '\0';

 printf("%s\n", pre);

 }

}

 

// Function to find all the numbers formed

// from the input string by replacing '$' with

// all the digits of the input string

int findNumUtil(char num[])

{

 // Array that stores the digits before

 // the charecter $ in the input string

 char pre[MAX];

 

 end = 0;

 

 // Traverse the input string and check if

 // the current charecter is a digit

 // if it is then set flag to true

 for (int i = 0; i < strlen(num); i++)

 if (num[i] >= '0' && num[i] <= '9') {

 bool flag = true;

 

 // Check if current character of the input

 // string is already present in the array set[]

 // then set flag to false

 for (int j = 0; j < end; j++)

 if (set[j] == num[i])

 flag = false;

 

 // Flag is true then store the charecter

 // into set[] and recursively find all

 // the combinations of numbers and store

 // it in the set[] array

 

 if (flag == true)

 set[end++] = num[i];

 }

 

 combinations(num, pre, 0, 0);

 

 return 0;

}

 

// Function to print all the combinations

// of the numbers by replacing '$' with

// the other digits of the input string

int findNum(char* num, int* result_count)

{

 int i;

 if (num[i]) {

 result_count[i] = findNumUtil(num);

 return (result_count[i]);

 }

 return 0;

}

 

// Driver code

int main()

{

 char num[MAX] = "23$$";

 int result_count[MAX];

 

 findNum(num, result_count);

 

 return 0;

}  
  
---  
  
 __

 __

 **Output:**

    
    
    2322
    2323
    2332
    2333
    

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

