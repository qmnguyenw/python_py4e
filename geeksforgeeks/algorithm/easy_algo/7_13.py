Difference between Algorithm, Pseudocode and Program



In this post, we will discuss the most common misconception that an algorithm
and a pseudocode is one of the same things. **No** , they are not!  
Let us take a look at definitions first,  
 **Algorithm :** **Systematic logical approach** which is a well-defined,
step-by-step procedure that allows a computer to solve a problem.  
 **Pseudocode :** It is a **simpler version of a programming code** in plain
English which uses short phrases to write code for a program before it is
implemented in a specific programming language.  
 **Program :** It is exact code written for problem **following all the rules
of the programming language.**

 **Algorithm**

An algorithm is used to provide a solution to a particular problem in form of
well-defined steps. Whenever you use a computer to solve a particular problem,
the steps which lead to the solution should be properly communicated to the
computer. While executing an algorithm on a computer, several operations such
as additions and subtractions are combined to perform more complex
mathematical operations. Algorithms can be expressed using **natural
language,flowcharts**, etc.  
Let’s take a look at an example for a better understanding. As a programmer,
we are all aware of the Linear Search program. (Linear Search)

 **Algorithm of linear search :**

    
    
    1. Start from the leftmost element of arr[] and 
    one by one compare x with each element of arr[]. 
    2. If x matches with an element, return the index. 
    3. If x doesn’t match with any of elements, return -1. 
    

Here, we can see how the steps of a linear search program are explained in a
simple, English language.

  

  

 **Pseudocode**

It is one of the methods which can be **used to represent an algorithm for a
program**. It **does not have a specific syntax** like any of the programming
languages and thus cannot be executed on a computer. There are several formats
which are used to write pseudo-codes and most of them take down the structures
from languages such as **C, Lisp, FORTRAN, etc.**

Many time algorithms are presented using pseudocode since they can be read and
understood by programmers who are familiar with different programming
languages. Pseudocode allows you to include several control structures such as
**While, If-then-else, Repeat-until, for and case** , which is present in many
high-level languages.  
 **Note:** Pseudocode is **not** an actual programming language.  
 **Peudocode for Linear Search :**

    
    
    FUNCTION linearSearch(list, searchTerm):
         FOR index FROM 0 -> length(list):
           IF list[index] == searchTerm THEN
               RETURN index
           ENDIF
           ENDLOOP
               RETURN -1
    END FUNCTION 
    

In here, we haven’t used any specific programming language but wrote the steps
of a linear search in a simpler form which can be further modified into a
proper program.

 **Program**

A program is a set of instructions for the computer to follow. The machine
can’t read a program directly, because it only understands machine code. But
you can write stuff in a computer language, and then a compiler or interpreter
can make it understandable to the computer.

 **Program for Linear Search :**

 __

 __  
 __

 __

 __  
 __  
 __

// C++ code for linearly search x in arr[]. If x

// is present then return its location, otherwise

// return -1

int search(int arr[], int n, int x)

{

 int i;

 for (i = 0; i < n; i++)

 if (arr[i] == x)

 return i;

 return -1;

}  
  
---  
  
 __

 __

 **Algorithm vs Psuedocode vs Program**

  1. An algorithm is defined as a well-defined sequence of steps that provides a solution for a given problem, whereas a pseudocode is one of the methods that can be used to represent an algorithm.
  2. While algorithms are generally written in a natural language or plain English language, pseudocode is written in a format that is similar to the structure of a high-level programming language. Program on the other hand allows us to write a code in a particular programming language.

So, as depicted above you can clearly see how the algorithm is used to
generate the pseudocode which is further expanded by following a particular
syntax of a programming language to create the code of the program.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

