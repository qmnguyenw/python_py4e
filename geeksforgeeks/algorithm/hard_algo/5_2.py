How is the time complexity of Sieve of Eratosthenes is n*log(log(n))?



 **Pre-requisite:** Sieve of Eratosthenes

 **What isSieve of Eratosthenes algorithm?**  
In order to analyze it, let’s take a number **n** and the task is to print the
prime numbers less than n. Therefore, by definition of Sieve of Eratosthenes,
for every prime number, it has to check the multiples of the prime and mark it
as composite. This process continues until a value **p** which is the highest
prime number less than **n**.

 **Understanding the n*log(log n) time complexity ofSieve of Eratosthenes**

  1. If it is assumed that the time taken to mark a number as composite is constant, then the number of times the loop runs is equal to:

![](https://latex.codecogs.com/gif.latex?\\frac{n}{2}&space;+&space;\\frac{n}{3}&space;+&space;\\frac{n}{5}&space;+&space;\\frac{n}{7}&space;+&space;......&space;p)

  2. On taking n common from the above equation, the above equation can be rewritten as:  
![](https://latex.codecogs.com/gif.latex?n*\(\\frac{1}{2}&space;+&space;\\frac{1}{3}&space;+&space;\\frac{1}{5}&space;+&space;\\frac{1}{7}&space;+&space;......&space;p\))

  

  

  3. It can be proved as below with the help of **Harmonic Progression of the sum of primes** :  
![](https://latex.codecogs.com/gif.latex?\\frac{1}{2}&space;+&space;\\frac{1}{3}&space;+&space;\\frac{1}{5}&space;+&space;\\frac{1}{7}&space;+&space;.....&space;=&space;log\(log\(n\)\))

 **Proof of Harmonic Progression of the sum of primes:**  
In order to understand the proof, the prerequisite is the Harmonic series and
**Taylor series expansion**.

    * Lets take an the equation:  
![](https://latex.codecogs.com/gif.latex?log\(\\frac{1}{1-x}\))

    * The taylor series expansion of the above equation is given by:  
![](https://latex.codecogs.com/gif.latex?x&space;+&space;\\frac{x^{2}}{2}&space;+&space;\\frac{x^{3}}{3}&space;+&space;...)

    * Putting **x = 1** in the above equation, we get the relation:

![](https://latex.codecogs.com/gif.latex?\\sum_{1}^{n}&space;\\frac{1}{r}&space;=&space;log\(n&space;\))

Let’s mark the above equation as **1**.

    * From Euler’s product formula,

![](https://latex.codecogs.com/gif.latex?\\sum_{1}^\\infty&space;{\\frac{1}{r^{s}}}&space;=&space;\\prod&space;\\frac{1}{1&space;-&space;p^{-s}})

    * On substituting **s = 1** in the above equation, we get

![](https://latex.codecogs.com/gif.latex?\\sum_{1}^\\infty&space;{\\frac{1}{r^{1}}}&space;=&space;\\prod&space;\\frac{1}{1&space;-&space;p^{-1}})

  

  

    * On applying **log** to both the sides:  
ul  
![](https://latex.codecogs.com/gif.latex?log\(\\sum_{1}^\\infty&space;{\\frac{1}{r^{1}}}\)&space;=&space;log\(\\prod&space;\\frac{1}{1&space;-&space;p^{-1}}\))

    * On **simplifying** the above equation, it becomes:

![](https://latex.codecogs.com/gif.latex?log\(\\sum_{1}^\\infty&space;{\\frac{1}{r^{1}}}\)&space;=&space;\\sum&space;log\(&space;\\frac{1}{1&space;-&space;p^{-1}}\))

    * In the above equation, **1 > p-1 > -1**
    * Thus, we can use taylor series expansion for the right hand side of the above equation.  
![](https://latex.codecogs.com/gif.latex?log\(\\frac{1}{1-x}\)&space;=&space;\\sum_{1}^{\\infty}&space;\\frac{1}{n*p^{n}})

    * On substituting this in the above equation, we get:

![](https://latex.codecogs.com/gif.latex?log\(\\sum_{1}^{n}\\frac{1}{r}\)&space;=&space;\\sum&space;\\sum_{1}^{n}&space;\\frac{1}{n*p^{n}})

where p is a prime number.

    * On expanding the inner summation;

![](https://latex.codecogs.com/gif.latex?\\sum_{1}^{n}&space;\\frac{1}{n*p^{n}}&space;=&space;\\frac{1}{p}&space;+&space;\\frac{1}{2p^{2}}&space;+&space;\\frac{1}{3p^{3}}&space;+&space;....)

    * The above series is convergent. So, the above series can be approximated to:  
![](https://latex.codecogs.com/gif.latex?\\frac{1}{p})

    * Therefore, on substituting and rewriting the equation; we get

![](https://latex.codecogs.com/gif.latex?log\(\\sum_{1}^{\\infty&space;}\\frac{1}{n}\)&space;=&space;\\sum&space;\\frac{1}{p})

where p is the prime number.

    *  **From the initial equation **1** , we can finally conclude that:  
![](https://latex.codecogs.com/gif.latex?\\sum&space;\\frac{1}{p}&space;=&space;log\(log\(n\)\))  
where p is the sum of prime numbers.**

  4. On substituting this in the equation, we get the time complexity as:  
![](https://latex.codecogs.com/gif.latex?O\(n*\(log\(log\(n\)\)\)\))

 **Hence the time complexity of Sieve of Eratosthenes is n*log(log(n))**

 **Reference:** Divergence of the sum of the reciprocals of the primes

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

