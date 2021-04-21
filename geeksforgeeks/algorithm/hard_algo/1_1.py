Shor’s Factorization Algorithm



 ** _Shor’s Factorization Algorithm_ :**

  * Shor’s Factorization Algorithm is proposed by Peter Shor.
  * It suggests that quantum mechanics allows the factorization to be performed in polynomial time, rather than exponential time achieved after using classical algorithms.
  * This could have a drastic impact on the field of data security, a concept based on the prime factorization of large numbers.
  * Many polynomial-time algorithms for integer multiplication (e.g., Euclid’s Algorithm) do exist, but no polynomial-time algorithm for factorization exists.
  * So, Shor came up with an algorithm i.e. Shor’s Factorization Algorithm, an algorithm for factorizing non-prime integers **N** of **L** bits.
  *  **Quantum algorithms** are far much better than classical algorithms because they are based on Quantum Fourier Transform.
  * Run time on the classical computer is **O[exp (L 1/3(log L)2/3)]** but that on the quantum computer is **O(L 3)**.
  * So, Shor’s Algorithm in principle, shows that a quantum computer is capable of factoring very large numbers in polynomial time.

 ** _Shor’s Algorithm depends on_ :**

  * Modular Arithmetic
  * Quantum Parallelism
  * Quantum Fourier Transformation

 ** _The Algorithm stands as_ :**

Given an odd composite number **N** , find an integer **d** , strictly between
**1** and **N** , that divides **N**.

Shor’s Algorithm consists of the following two parts:

  

  

  * Conversion of the problem of factorizing to the problem of finding the period. This part can be implemented with classical means.
  * Finding the period or Quantum period finding using the **Quantum Fourier Transform** , and is responsible for quantum speedup, and utilizes quantum parallelism.

In Shor’s Algorithm, the **Input** is Non-prime number **N** and the
**Output** is Non-trivial factor of **N**

>  _INPUT (N)_ —> _**SHOR’S ALGORITHM**_ —> _OUTPUT (Non-trivial factor of N)_

 **Algorithm:** It contains a few steps, at only step 2 the use of quantum
computers is required.

  1. Choose any random number let say **r** , such that **r < N** so that they are co-primes of each other.
  2. A quantum computer is used to determine the unknown period **p** of the function **f r, N (x) = rx ****mod** **N**.
  3. If **p** is an odd integer, then go back to **Step 1**. Else move to the next step.
  4. Since **p** is an even integer so, **(r p/2 – 1)(rp/2 \+ 1) = rp – 1 = 0 mod N**.
  5. Now, if the value of **r p/2 \+ 1 = 0 mod N**, go back to **Step 1**.
  6. If the value of **r p/2 \+ 1 != 0 mod N**, Else move to the next step.
  7. Compute **d = gcd(r p/2-1, N)**.
  8. The answer required is ‘ **d** ’.

 ** _Classical part (_ The order finding problem):**  
This is the classical part of order finding problem. Given that **x** and
**N** , such that **x <N** and **gcd(x, N) = 1**. The order of **x** is the
least positive integer, y such that **x y = 1(mod N)**.

  1. A random number **n** is picked, such that **n < N**. Compute **gcd(n, N)**.
  2. This can be done using the Euclid Algorithm.
  3. If **gcd(n, N) != 1** , then there is a non-trivial factor of N.If **(x+p) = n x + p mod N = nxmod N = f(x)**.
  4. If r is odd, then go back to **Step 1**.
  5. If **n p/2 = -1(mod N)**, then go back to **Step 1**.
  6. The **gcd(n p/2 +/- 1, N)** is a non-trivial factor of **N**.

 ** _Quantum part:_**

> This is the quantum order finding part. Choose a power of 2, then  
>  **Q = 2L such that N 2 <= Q <= 2N2**

And consider f = {0, 1, 2, …, Q-1}

Where, **f(y)=1/(Q) 1/2 ∑x=0Q-1I f(x) I wxy** and **w = exp(2π i/Q)** , i.e.
Qth root of unity.

  * Let’s perform **Shor’s Algorithm** using an example: To factor an odd integer N (let N = 17).
  * Choose an integer Q such that **N 2 <= Q ≤ 2 N2** ( lets Q = 324).
  * Then, randomly choose any integer n such that gcd(n, N)=1, (let us choose the integer be n=7).
  * Then create two quantum registers (these registers should be entangled so that the collapse of the input registered corresponds to the collapse of the output register)
    *  **Input Register:** must be containing enough qubits to represent numbers as large as Q-1.(i.e., up to 323, so we need 9 qubits).
    *  **Output Register:** must be containing enough qubits to represent numbers as large as **(N – 1)**. (i.e., up to 16, so we require 4 qubits).

 **Code :**

## Python

 __

 __  
 __

 __

 __  
 __  
 __

from qiskit import IBMQ

from qiskit.aqua import QuantumInstance

from qiskit.aqua.algorithms import Shor

# Enter your API token here

IBMQ.enable_account('ENTER API TOKEN HERE') 

provider = IBMQ.get_provider(hub='ibm-q')

# Specifies the quantum device

backend = provider.get_backend('ibmq_qasm_simulator')

print('\n Shors Algorithm')

print('--------------------')

print('\nExecuting...\n')

# Function to run Shor's algorithm

# where 21 is the integer to be factored

factors = Shor(35)

result_dict = factors.run(QuantumInstance(

 backend, shots=1, skip_qobj_validation=False))

 # Get factors from results

result = result_dict['factors']

print(result)

print('\nPress any key to close')

input()  
  
---  
  
 __

 __

 **Output :**

    
    
    Shors Algorithm
    - - - - - - - - - - - - -
    Executing...
    [[5,7]]
    Press any key to close

Output for the code above showing the factors 5 and 7 for N=35.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

