Python – Golomb Encoding for b=2n and b!=2n



The Golomb coding is a form of parameterized coding in which integers to be
coded are stored as values relative to a constant b

 **Coding:-**  
A positive number x is spoken to in two sections:

  * The initial segment is an unary portrayal of q+1, where q is the remainder floor((x/b)), and
  * The subsequent part is an extraordinary double portrayal of the leftover portion **r = x-qb**. Note that there are b potential leftovers.

For instance, if b = 3, the potential remnants will be 0, 1 and 2. To spare
space, compose the initial couple of remnants utilizing floor(log(b, 2)) bits
and the rest utilizing ceil(log(b, 2)) bits. We should do so with the end goal
that the decoder knows at the point when floor(log(b, 2)) bits are utilized
and when ceil(log(b, 2)) bits are utilized

 **Examples:**

    
    
    **Input  :** N = 37, M = 11 
    **Output :** 0001100

