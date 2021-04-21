Code Golfing in Python



 **Code Golf** in Python refers to attempting to solve a problem using the
least amount of characters possible. Like in Golf, the low score wins, the
fewest amount of characters “wins”.

Python is a fantastic language for code golfing due to backward compatibility,
quirks, it being a high-level language, and all the coercion. So, here we will
look at some Code golfing techniques in Python language.

## Using loops

 **Collapse two numerical loops:** Suppose you are iterating over a matrix of
**m rows** and **n columns** . Instead of two nested for loops, one for the
row and one of the columns, it’s usually shorter to use a single loop to
iterate over the m*n matrix.

 **Original Code :**

    
    
    m = n = 3
    for i in range(m):
        for j in range(n):
            print(i, j)
    

**Golfed Code :**

  

  

    
    
    m = n = 3
    for i in range(m*n):
        print(i//n, i%n)
    

This technique is not limited to only two nested loops, we can even write the
same loop for **3 or more nested loops**

    
    
    m, n, o = 2, 3, 4
    for k in range(m*n*o):
        print(k//n//o, k%(n*o), k%o)
    

## Using operators

 ****

* Addition or Subtraction by 1:

