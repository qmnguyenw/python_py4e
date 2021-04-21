Method of guessing and confirming



The basic idea behind this method is to **guess the answer** , and then
**prove it correct by induction.** This method can be used to solve any
recurrence. If a solution is guessed and then try to verify our guess
inductively, usually either the proof will succeed (in that case we are done),
or the proof will fail (in that case the failure will help us refine our
guess).

For example, consider the recurrence: ![T\(N\) = √N*T\(√N\) +
N](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
ecf1d07653242233bfd502e8836e0706_l3.png). This doesn’t fit into the form
required by the Master Theorems. Carefully observing the recurrence gives us
the impression that it is similar to the divide and conquer method (diving the
problem into _√N_ subproblems each with size _√N_ ). As it can be seen that,
the size of the subproblems at the first level of recursion is _N_. So, let us
guess that ![T\(N\) = O\(N*log N\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-ec0932edd9f608a4ee8f60a2e3d863f1_l3.png), and
then try to prove that the guess is correct.

Let’s start by trying to prove an upper bound:

> ![T\(N\) \\le cN*logN:](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-79a9b47da2a6285904dc3963692d88a3_l3.png)
>
> ![T\(N\) = √N*T\(√N\) + N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-ecf1d07653242233bfd502e8836e0706_l3.png)
>
>  
>
>
>  
>
>
> ![T\(N\) \\le √N* c√N*log√N + N](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-979cdb00e321b70b209409ff13432809_l3.png)
>
> ![T\(N\) = N* clog√N + N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-5037d59d359cd14a000985f91362fbaf_l3.png)
>
> ![T\(N\) = N*1/2*c*log N + N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-77d51c98abff4e880bdece091ae7a50e_l3.png)
>
> ![T\(N\) \\le cN*log N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-bf4e9647c5c192817bb976f0fc79e5e3_l3.png)

The last inequality assumes only that ![1 \\le 1/2*clog
N](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8cc98cb5d188b99c130c9597b10da024_l3.png). This is correct
if _N_ is sufficiently large and for any constant c, no matter how small.

From the above proof, we can see that our guess is correct for the upper
bound. Now, let us prove the lower bound for this recurrence:

> ![T\(N\) = √N*T\(√N\) + N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-ecf1d07653242233bfd502e8836e0706_l3.png)
>
> ![T\(N\) \\ge  √N* k√N*log√N + N](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-d0dd96ea1924a20facf101b158ec07e2_l3.png)
>
>  
>
>
>  
>
>
> ![T\(N\) = N* klog√N + N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-80633b63effe2a770e91c16e8ba39355_l3.png)
>
> ![T\(N\) = N*1/2*k*log N + N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-a99fc73cc067dc273e4e637e80481d7f_l3.png)
>
> ![T\(N\) \\ge  N*k*log N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-0e035b929bef09ea391e6eb48ad83b6e_l3.png)

The last inequality assumes only that ![1 \\ge  1/2*k*log
N](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
ae69e71d4ef0acae575c3d1d3816af19_l3.png). This is incorrect if _N_ is
sufficiently large and for any constant k.

From the above proof, we can see that our guess is incorrect for the lower
bound.

From the above discussion, it can be understood that ![Θ\(N*log
N\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8308733f046e15c59ba90b3512ed7644_l3.png) is too big. But
how about ![Θ\(N\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a7b3aa830b4c1acf8fe6e5b5763db784_l3.png)? The lower bound
is easy to prove directly:

> ![T\(N\) = √N*T\(√N\) + N \\ge  N](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-162733b5c8d1544f925db0bb026471cd_l3.png)

Now, let us prove the upper bound for this Θ(N):  
![T\(N\) = √N*T\(√N\) + N\\\\ \\le √N*c√N + N\\\\ = N c+ N\\\\ = N \(c +
1\)\\\\ \\nleq cN](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-fe0631c06e1b92d3841b74cb17a4ba64_l3.png)

From the above induction, it can be understood that
![Θ\(N\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a7b3aa830b4c1acf8fe6e5b5763db784_l3.png) is too small and
![Θ\(N*log N\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8308733f046e15c59ba90b3512ed7644_l3.png) is too big. So,
we need something bigger than N and smaller than ![N*log
N](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
fd19eb200e5241125993165bf628433b_l3.png)? How about ![N*√log
N](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a2210d394b2e52eabbd1e150b1cb9ae6_l3.png)?

Proving upper bound for ![N*√log N](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-a2210d394b2e52eabbd1e150b1cb9ae6_l3.png):

> ![T\(N\) = √N*T\(√N\) + N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-ecf1d07653242233bfd502e8836e0706_l3.png)
>
> ![T\(N\) \\le √n*c√N*√\(log √N\) + N](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-d2679258633d54c771a616499204866e_l3.png)
>
> ![T\(N\) = N* 1/√2 *c*log √N + N](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-da21f10f6fc6ab729a84ff063d63851b_l3.png)
>
> ![T\(N\) \\le N*c*log √N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-09b321a1249c7614b1905389fd2c6a9b_l3.png)

Proving lower bound for ![N*√log N](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-a2210d394b2e52eabbd1e150b1cb9ae6_l3.png):

> ![T\(N\) = √N*T\(√N\) + N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-ecf1d07653242233bfd502e8836e0706_l3.png)
>
> ![T\(N\) \\ge  √N*k√N*√\(log√N\) + N](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-d86776026c32d38acd6ceaa5a9cbf011_l3.png)
>
> ![T\(N\) = N*1/√2*k*log √N + N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-5badf2aa86e9b87a36dbb01c02905ca0_l3.png)
>
> ![T\(N\) \\ngeq N*k*log √N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-4bc4e88bd9b4fefac77b79ccb9fbb6c3_l3.png)

The last step doesn’t work. So, ![Θ\(N*√log
N\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8b28c10fd2dbe2f3db30beebfff2c55d_l3.png) doesn’t work.
What else is between N and ![N*log N](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-fd19eb200e5241125993165bf628433b_l3.png)? How
about ![N*log\(log N\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-0ea3b88cc65385be0bfdb6fa69e63b09_l3.png)?

Proving upper bound for ![N*log\(log N\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-0ea3b88cc65385be0bfdb6fa69e63b09_l3.png):

> ![T\(N\) = √N*T\(√N\) + N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-ecf1d07653242233bfd502e8836e0706_l3.png)  
> ![T\(N\) \\le √N*c√N*log\(log √N\) + N](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-5fcb4073749f2bdbf851b8b2ee3bde25_l3.png)  
> ![T\(N\) = N*clog\(log N\) - cN + N](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-fc13825e1723111063e68b111ff26cbd_l3.png)  
> ![T\(N\) \\le N*clog\(log N\), if \\ c\\ge
> 1](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-38e7c407084c50b23aafd362ac7852a2_l3.png)

Proving lower bound for ![N*log\(log N\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-0ea3b88cc65385be0bfdb6fa69e63b09_l3.png):

> ![T\(N\) = √N*T\(√N\) + N](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-ecf1d07653242233bfd502e8836e0706_l3.png)
>
> ![T\(N\) \\ge  √N*k√N*log\(log √N\) + N](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-923de01c5ed18c4f3bfd15f7605738d8_l3.png)
>
> ![T\(N\) = N*k*log\(log N\) - kN + N](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-155b7c8217e7bf1d71a597de06eff64b_l3.png)
>
> ![T\(N\) \\ge  N*klog\(log N\), if \\ k \\le
> 1](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-b523f100910452ac922e4ba0e8d3b910_l3.png)

From the above proofs, it can see that ![T\(N\) \\le N*clog\(log N\), if \\ c
\\ge  1](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c7787dc0806a01205a4b39d3a9add224_l3.png) and ![T\(N\)
\\ge  N*klog\(log N\), if \\ k \\le 1](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-b523f100910452ac922e4ba0e8d3b910_l3.png).  
Technically, we’re still missing the base cases in both proofs, but we can be
fairly confident at this point that ![T\(N\) = Θ\(N*log\(log
N\)\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-193dac625bf4a604c0cec9763c03b6b1_l3.png).

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

