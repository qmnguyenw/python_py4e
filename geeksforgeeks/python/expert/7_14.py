Python | Single Point Crossover in Genetic Algorithm



 **Single Point Crossover** in Genetic Algorithm is a form of crossover in
which two-parent chromosome are selected and a random/given point is selected
and the genes/data are interchanged between them after the given/selected
point for example

 **Examples:**

    
    
    **P1:** 000011110011 
    **P2:** 101010101010
    
    **Point: 4**
    **After Crossover:**
    **C1:** 000010101010
    **C2:** 101011110011
    

The problem is to select a random point for the crossover of two given parents
and generate at least five generations of children from the given pair of a
chromosome.

 **Code : Python program for single-point crossover in Genetic Algorithm**

 __

 __  
 __

 __

 __  
 __  
 __

# library to generate a random number

import random

 

# function for implementing the single-point crossover

def crossover(l, q):

 

# converting the string to list for performing the crossover

 l = list(l)

 q = list(q)

 

# generating the random number to perform crossover

 k = random.randint(0, 15)

 print("Crossover point :", k)

 

# interchanging the genes

 for i in range(k, len(s)):

 l[i], q[i] = q[i], l[i]

 l = ''.join(l)

 q = ''.join(q)

 print(l)

 print(q, "\n\n")

 return l, q

 

 

# patent chromosomes:

 

s = '1100110110110011'

p = '1000110011011111'

print("Parents")

print("P1 :", s)

print("P2 :", p, "\n")

 

# function calling and storing the off springs for 

# next generation crossover

for i in range(5):

 print("Generation ", i+1, "Childrens :")

 s, p = crossover(s, p)  
  
---  
  
 __

 __

 **Output:**

    
    
    Parents
    P1 : 1100110110110011
    P2 : 1000110011011111 
    
    Generation  1 Childrens :
    Crossover point : 2
    1100110011011111
    1000110110110011 
    
    
    Generation  2 Childrens :
    Crossover point : 7
    1100110110110011
    1000110011011111 
    
    
    Generation  3 Childrens :
    Crossover point : 0
    1000110011011111
    1100110110110011 
    
    
    Generation  4 Childrens :
    Crossover point : 7
    1000110110110011
    1100110011011111 
    
    
    Generation  5 Childrens :
    Crossover point : 2
    1000110011011111
    1100110110110011
    

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

  
  

  

My Personal Notes _arrow_drop_up_

Save

