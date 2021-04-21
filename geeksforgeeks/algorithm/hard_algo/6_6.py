Algorithms Sample Questions | Set 3 | Time Order Analysis



  
 **Question 1:** What is the asymptotic boundary of T(n)?

> ![ T\(n\) =  \\sum_{i=2}^{n} log_{i}n = log_{2}n + log_{3}n + \\ldots +
> log_{n}n  ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-a30f3b87a626c29368104ab737aa79d7_l3.png)

  1. θ( n*log(n) )
  2. θ( n2 )
  3. θ( n )
  4. θ( n*log2(n) )
  5. θ( n2*log2(n) )

 **Answer: 3**  
 **Explanation:** To find appropriate upper and lower boundaries, an approach
which first comes to mind is to expand the sigma notation to single terms
among which some patterns can be detected. This way it helps to define some
acceptable upper and lower boundaries and their combination might lead to a
possible solution.

Regarding specifying these boundaries, there are some hints as following:

  * This is obvious that for any k greater than &Sqrt; n, each logkn should be less than log&Sqrt;nn = 2, while more than lognn = 1. In mathematic language:

  

  

  1. A hint on UPPER boundary, for k > &Sqrt; n:

![ \\forall k \\geq \\sqrt{n},  log_{k}n \\leq log_{\\sqrt{n}}n = 2
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-773bdefd5f141db64c934cdf162cbb4c_l3.png)

![ \\Rightarrow \\sum_{i=\[\\sqrt{n}\]}^{ n } log_{i}n \\leq
\\sum_{i=\[\\sqrt{n}\]}^{ n } 2 ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-db9f1a658d930759424b4e0329e14891_l3.png)

  2. A hint on LOWER boundary, for k > &Sqrt; n:

![ \\forall k \\geq \\sqrt{n},  log_{k}n \\geq log_{n}n = 1
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-0f3d2ac72191bae9dfb0b21cc86382bd_l3.png)

![ \\Rightarrow \\sum_{i=\[\\sqrt{n}\] + 1}^{ n } log_{i}n \\geq
\\sum_{i=\[\\sqrt{n}\] + 1}^{ n } 1 ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-bda39c60c18aab07aa6739252aa2198a_l3.png)

* Besides that, as the base of a logarithm increases, its value decreases; so none of the terms resulted from expansion of the first sigma can be more than the first ter, log2n, nor can be less than the last one, which is log&Sqrt;nn; in other sentences,

  1. Another hint on UPPER boundary, but this time for k < &Sqrt; n:

![ \\forall k \\leq \\sqrt{n},  log_{k}n \\leq log_{2}n
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e52df941febb9e8d5de48af0517fae5e_l3.png)

![ \\Rightarrow  \\sum_{i=2}^{  \[\\sqrt{n}\] } log_{i}n \\leq  \\sum_{i=2}^{
\[\\sqrt{n}\] } log_{2}n](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-ccf61475ec5ce05ff753fc1a4f5b8993_l3.png)

  2. Another hint on LOWER boundary, but this time for k < &Sqrt; n:

![ \\forall k \\leq \\sqrt{n},  log_{k}n \\geq log_{\\sqrt{n}}n = 2
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-406c337af2912bc5e37c1f020f8b877b_l3.png)

  

  

![ \\Rightarrow \\sum_{i=2}^{  \[\\sqrt{n}\] } log_{i}n \\geq  \\sum_{i=2}^{
\[\\sqrt{n}\] } 2](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-cc28fd0fe008667f793f768624f3e76c_l3.png)

