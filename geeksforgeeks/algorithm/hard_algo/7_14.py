Deriving the expression of Fibonacci Numbers in terms of golden ratio



 **Prerequisites:** Generating Functions, Fibonacci Numbers, Methods to find
Fibonacci numbers.

The method of using Generating Functions to solve the famous and useful
Fibonacci Numbers‘ recurrence has been discussed in this post.

The **Generating Function** is a powerful tool for solving a wide variety of
mathematical problems, including counting problems. It is a formal power
series. For example, in counting problems, we are often interested in finding
the number of objects of size ![n](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-ad7ed49d64e4f28446c48c53a0e2718a_l3.png). In
such a case, we define a power series, which, in simple terms is an infinite
term polynomial where the coefficient of the
![nth](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7cb2819d063bc4b29f52f7f5254bb8f6_l3.png) degree term is
the ![nth](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7cb2819d063bc4b29f52f7f5254bb8f6_l3.png) term of the
sequence. This helps us to find many interesting and important results. It
should be noted that in the use of generating functions, we generally use the
coefficients in the generating function power series, we rarely use the
variable in the series. In this post too, we shall do the same. The ordinary
generating function of some an is:

> ![\\mathcal{G}\(a_{n};x\) =
> \\sum_{n=0}^{\\infty}a_{n}x^n](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-26827ffc044b969e176a8143a027d909_l3.png)

Fibonacci Numbers are one of the fundamental sequences in mathematics, and
numerous ways have been discovered to find out the higher order terms of this
sequence. This post discusses one such method.

  

  

Let’s first define a generating function for the Fibonacci Numbers, and then
the function will be simplified to get a recurrence. Using this, expand the
simplification and break it into partial fractions, and then use two standard
power series, and later combine them both to arrive at surprising result for
the ![ith](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-410fff8080075c2144ee5d8f0e7d4833_l3.png) term of the
Fibonacci Series.

Let us define the generating function
![\\mathcal{F}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e8440b68fd1273c326f275a0370c3bc0_l3.png) as

> ![\\mathcal{F}\(z\) =
> \\sum_{i=0}^{\\infty}F_{i}z^i](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-7e21bd10d51153458b9786cba7fca0d6_l3.png)
>
> ![\\mathcal{F}\(z\) = 0 + z + z^2 + 2z^3 + 3z^4 + 5z^5 + 8z^6 + ...
> \\infty](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-927bafa168a3d84a39de445305fc61a5_l3.png),
>
> where ![F_{i}](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-c8b64f4aff9eac5909a001d6d5fa3cf9_l3.png) is the ith
> Fibonacci Number.

Since,

![\\mathcal{F}\(z\) = z + z^2 + 2z^3 + 3z^4 + 5z^5 + 8z^6 + ...
\\infty](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-15ea79c7dfe48e4c033da433c127a2e7_l3.png) .

![\\mathcal{F}\(z\) = z + \(1 + 0\)z^2 + \(1 + 1\)z^3 + \(2 + 1\)z^4 + \(3 +
2\)z^5 + \(5 + 3\)z^6 + ... \\infty](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-9d3a6d80e905c548b1850544f2f8ece4_l3.png) .

  

  

Rearranging them we get,

![\\mathcal{F}\(z\) = z + \[z^2 + z^3 + 2z^4 + 3z^5 + 5z^6 + ... \\infty\] +
\[0 + z^3 + z^4 + 2z^5 + 3z^6 + ...
\\infty\]](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-12fcad64c91296951a64ced9d8e8215c_l3.png).

Taking the common terms,

![\\mathcal{F}\(z\) = z + \(z\)\[z + z^2 + 2z^3 + 3z^4 + 5z^5 + ...
\\infty\]](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e2b83ae9f6ab3be2cff5d2e692dffdbf_l3.png)  
![+ \(z^2\)\[0 + z^1 + z^2 + z^3 + 3z^4 + ...
\\infty\]](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
ad6477d39311dddaa5b0ca9fd607f7c8_l3.png)

Simplifying it further, the below function is obtained.

![\\mathcal{F}\(z\) = z + z\\mathcal{F}\(z\) +
z^2\\mathcal{F}\(z\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8609c204adfaac60004754b5aec687f1_l3.png) .

Solving for ![\\mathcal{F}\(z\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-b0de1b43eb6ce9670133934c0f56d522_l3.png), we get:

![\\mathcal{F}\(z\) = \\frac{z}{1-z-z^2}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-3bd7a1760b8bf2046d81f2ed2e12eb87_l3.png) .

We get the below formula by above operations:

> ![1-z-z^2 = -\(z + \\phi\)\(z +
> \\widehat{\\phi}\)](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-c7f60cbdf21570104b19f14fb84899f8_l3.png),
>
> where, ![\\phi = \\frac{1+\\sqrt{5}}{2}](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-29d368c706a5efe6133a6454855a140e_l3.png) and
> ![\\widehat{\\phi} =
> \\frac{1-\\sqrt{5}}{2}](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-07aafdee445fdcdc4ee55ece75f35e1d_l3.png) .

Thus,

![\\mathcal{F}\(z\) = \\frac{-z}{\(z + \\phi\)\(z +
\\widehat{\\phi}\)}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-ac5b9c0a24ee05c9116478508688133e_l3.png)  
Also note that,

![\\phi\\widehat{\\phi} = -1](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c0b88710b0af86f7b249a5d251a25693_l3.png).

Thus, keeping this relation in above expression, we get,

![\\mathcal{F}\(z\) = \\frac{z}{\(1-z\\phi\)\(1 -
z\\widehat{\\phi}\)}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-1043dbecafcfe070d034bfb88bf48562_l3.png) .

Now the right hand side of the above expression can be separated into partial
fractions,

![\\mathcal{F}\(z\) = \\frac{1}{\\sqrt{5}}\\left \[ \\frac{1}{\(1-\\phi z\)} -
\\frac{1}{\(1-\\widehat{\\phi} z\)}\\right
\]](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-399ddde8c421a3f0766584f1a31b9c05_l3.png) .

Using Expansion on the two fractions,

![\\frac{1}{\(1-\\phi z\)} = 1 + \\phi z + \\phi ^2 z^2 + \\phi ^3 z^3 + ...
\\infty = \\sum_{i=0}^{\\infty}\\phi ^iz^i](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-682dc1e1a4df8fad4d7a6dfa6efa1f64_l3.png) .

Similarly,

![\\frac{1}{\(1-\\widehat{\\phi} z\)} = 1 + \\widehat{\\phi} z +
\\widehat{\\phi} ^2 z^2 + \\widehat{\\phi} ^3 z^3 + ... \\infty =
\\sum_{i=0}^{\\infty}\\widehat{\\phi} ^iz^i](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-cb383e55bade91ca2ffaa23fce1e114a_l3.png) .

Thus,

![\\mathcal{F}\(z\) = \\sum_{i=0}^{\\infty}\\frac{1}{\\sqrt{5}}\(\\phi ^iz^i -
\\widehat{\\phi} ^iz^i\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e086b23e93a8f9810eb76eb3f202b679_l3.png) .

Thus,

![F_{i} = \\frac{1}{\\sqrt{5}}\(\\phi ^i - \\widehat{\\phi}
^i\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d87cafc22717fac185d52ac5b44889b3_l3.png) .

Now,

![\\left | \\phi \\right |  < 1](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-111db432b77df49a1f3c5c37e4ab7389_l3.png),

and,

![\\left | \\frac{\\widehat{\\phi} ^i}{\\sqrt{5}} \\right | < \\left |
\\frac{\\phi ^i}{\\sqrt{5}} \\right | <
\\frac{1}{2}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-bb651eb14d3bc9b32dc40d545525f4f4_l3.png)

Using the above two facts, it can be safely concluded that the value of

> ![F_{i} = \\frac{\\phi ^i}{\\sqrt{5}}](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-0932210ba1cd46f38814e7649135050f_l3.png),
> rounded to the nearest integer.

Finding n-th Fibonacci number using Golden ratio is one of the applications of
this formula.

Attention reader! Don’t stop learning now. Get hold of all the important DSA
concepts with the **DSA Self Paced Course** at a student-friendly price and
become industry ready. To complete your preparation from learning a language
to DS Algo and many more, please refer **Complete Interview Preparation
Course** **.**

My Personal Notes _arrow_drop_up_

Save

