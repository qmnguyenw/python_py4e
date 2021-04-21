NZEC error in Python



While coding in various competitive sites, many people must have have
encountered NZEC error. NZEC (non zero exit code) as the name suggests occurs
when your code is failed to return 0. When a code returns 0 it means it is
successfully executed otherwise it will return some other number depending on
the type of error.  
When the program ends and it is supposed to return “0” to indicate if finished
fine and not able to do so it cause NZEC. Of course there are more cases
associated with NZEC.

 **Why does NZEC occur?(one example)**

In python, generally multiple inputs are separated by commas and we read them
using input() or int(input()), but most of the online coding platforms while
testing gives input separated by space and in those cases int(input()) is not
able to read the input properly and shows error like NZEC.

 **How to resolve?**

For Example, Think of a simple program where you have to read 2 integer and
print them(in input file both integer are in same line). Suppose you have two
integers as shown below:  
23 45  
Instead of using :

  

  

    
    
    n = int(input())
    k = int(input())

Use:

    
    
    n, k = raw_input().split(" ")
    n = int(n)
    k = int(k)

to delimit input by white spaces.

 **Wrong code**

 __

 __  
 __

 __

 __  
 __  
 __

n= int(input())

k = int(input())

print n," ",k  
  
---  
  
 __

 __

 **Input:**  
2 3  
When you run the above code in IDE with above input you will get error:-

    
    
    Traceback (most recent call last):
      File "b712edd81d4a972de2a9189fac8a83ed.py", line 1, in 
        n = int(input())
      File "", line 1
        2 3
          ^
    SyntaxError: unexpected EOF while parsing
    

The above code will work fine when the input are in 2 two different lines. You
can test yourself. To overcome this problem you need to use split.

 **Correct code**

 __

 __  
 __

 __

 __  
 __  
 __

n, k= raw_input().split(" ")

n = int(n)

k = int(k)

print n," ",k  
  
---  
  
 __

 __

 **Input:**

    
    
    7 3

 **Output:**

    
    
    7   3
    

**Some prominent reasons for NZEC error**

  1. Infinite Recursion or if you have run out of stack memory.
  2. Input and output both are NOT exactly same as the test cases.
  3. As the online platforms, test your program using a computer code which matches your output with the specified outputs exactly.
  4. This type of error is also shown when your program is performing basic programming mistakes like dividing by 0.
  5. Check for the values of your variables, they can be vulnerable to integer flow.

There could be some other reasons also for occurrence NZEC error, i have
listed the frequent ones.

This article is contributed by **Aakash Tiwari**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![competitive-programming-img](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20200604102100/GFG-CP-Article-2.png)

My Personal Notes _arrow_drop_up_

Save

