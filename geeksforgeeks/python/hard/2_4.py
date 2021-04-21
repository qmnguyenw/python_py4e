Mathematical Approach to PCA



 **What is PCA?**

The main guiding principle for **Principal Component Analysis** is FEATURE
EXTRACTION i.e. “Features of a data set should be less as well as the
similarity between each other is very less.” In PCA, a new set of features are
extracted from the original features which are quite dissimilar in nature. So,
an **n-dimensional feature space** gets transformed into an **m-dimensional
feature space.** , where the dimensions are orthogonal to each other.

**Concept of Orthogonality :**

(In order to understand this topic, we have to go to the vector space concept
in linear algebra) **Vector Space** is a set of vectors. They can be
represented as a linear combination of the smaller set of vectors called
**BASIS VECTORS.** So any vector ‘v’ in a vector space can be represented as:

![v = \\sum_{i=1}^na_iu_i](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-a22f5e7faebea149b92f8a10f5a3ed3f_l3.png)

  

  

where _**a**_ represent ‘n’ scalars and u represents the basis vectors. Basis
vectors are orthogonal to each other. Orthogonality of vectors can be thought
of an extension of the vectors being perpendicular in a 2-D vector space **.**
So our feature vector (data-set) can be transformed into a set of principal
components (just like the basis vectors).

 **Objectives of PCA :**

  1.  **** The new features are distinct i.e. the covariance between the new features (in case of PCA, they are the principal components) is **0**.
  2. The principal components are generated in order of the variability in the data that it captures. Hence, the first principal component should capture the maximum variability, the second one should capture the next highest variability etc.
  3. The sum of the variance of the new features / the principal components should be equal to the sum of the variance of the original features.

 **Working of PCA :**

PCA works on a process called **Eigenvalue Decomposition** of a covariance
matrix of a data set. The steps are as follows:

  * First, calculate the covariance matrix of a data set.
  * Then, calculate the eigenvectors of the covariance matrix.
  * The eigenvector having the highest eigenvalue represents the direction in which there is the highest variance. So this will help in identifying the first principal component.
  * The eigenvector having the next highest eigenvalue represents the direction in which data has the highest remaining variance and also orthogonal to the first direction. So, this helps in identifying the second principal component.
  * Like this, **** identify the top ‘k’ eigenvectors having top ‘k’ eigenvalues to get the ‘k’ principal components.

 **Numerical for PCA :**

Consider the following dataset **x1**|  **2.5**|  **0.5**|  **2.2**|  **1.9**|
**3.1**|  **2.3**|  **2.0**|  **1.0**|  **1.5**|  **1.1**|  **x2**|  **2.4**|
**0.7**|  **2.9**|  **2.2**|  **3.0**|  **2.7**|  **1.6**|  **1.1**|  **1.6**|
**0.9**  
---|---|---|---|---|---|---|---|---|---|---  
  
####  **Step 1: Standardize the Dataset**

Mean for ![x_1   ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-b2f2e1e5ba4439f18eb9cb3a87a4f0cd_l3.png)= 1.81 =
![x_{1mean}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f35fba83156bbd4f5690a5bfc8ff4122_l3.png)

Mean for ![x_2   ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-633510ce1ad2f4bb6ede3379d4754614_l3.png)= 1.91 =
![x_{2mean}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-0f9387441d8ae8581e351332713dd684_l3.png)

  

  

We will change the dataset. ![x_{1new} = x_1 + x_{1mean}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d1fa7080d0a5766076c34768212aba2a_l3.png)| 0.69| -1.31|
0.39| 0.09| 1.29| 0.49| 0.19| -0.81| -0.31| -0.71| ![x_{2new} = x_2 +
x_{1mean}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7e3aec51c2e94c4079170d898449a7ba_l3.png)| 0.49| -1.21|
0.99| 0.29| 1.09| 0.79| -0.31| -0.81| -0.31| -1.01  
---|---|---|---|---|---|---|---|---|---|---  
  
####  **Step 2: Find the Eigenvalues and eigenvectors**

 **Correlation Matrix c =**![C = \\left\(\\frac{X \\cdot
X^T}{N-1}\\right\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-873cee2a84a8f1c6f74324cac243f0bc_l3.png)

 **where, X is the Dataset Matrix** (In this numerical, it is a 10 X 2 matrix)

![X^T   ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-380950e1a9e2f11c611376bbc0c522ce_l3.png)**** is the
transpose of the X (In this numerical, it is a 2 X 10 matrix) and N is the
number of elements = 10

So, ![C = \\left\(\\frac{X \\cdot X^T}{10 - 1}\\right\)= \\left\(\\frac{X
\\cdot X^T}{9}\\right\)](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7cdd2117e95bb3853d4a4edca207ce25_l3.png)

{So in order to calculate the Correlation Matrix, we have to do the
multiplication of the Dataset Matrix with its transpose}

![C = \\begin{bmatrix} 0.616556 & 0.615444\\\\ 0.615444 & 0.716556
\\end{bmatrix}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-6a38ba90e9d97f104f70efc39ae00bfe_l3.png)

Using the equation, **| C –**![\\lambda
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-59fae9c37b5d312d3baaf0e4c81ca0e6_l3.png) **I | = 0** –
**equation (i)** where { \lambda is the eigenvalue and I is the Identity
Matrix }

So solving equation (i)

![\\begin{bmatrix} 0.616556 & 0.615444 \\\\ 0.615444 & 0.716556 \\end{bmatrix}
- \\lambda \\begin{bmatrix} 1 & 0 \\\\ 0 & 1
\\end{bmatrix}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-1ede3c9df3863a12781e502a31010625_l3.png)

![\\begin{vmatrix} 0.616556-\\lambda & 0.615444 \\\\ 0.615444 &
0.716556-\\lambda \\end{vmatrix} =  0](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-c274bdf232aa36cbffc8e35b67e6be52_l3.png)

Taking the determinant of the left side, we get

![0.44180 - 0.616556\\lambda - 0.716556\\lambda + \\lambda^2 - 0.37877 =
0](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-4d2e41c9067afa4237a53977047865b4_l3.png)

![\\lambda^2 - 1.33311\\lambda + 0.06303 = 0
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-5e9f85d6f2bc8235a452453bac0eca96_l3.png)

We get two values for ![\\lambda   ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-c5a9c5f1ae4cdba8529e25da216483c4_l3.png), that
are **(**![\\lambda_1   ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-28316e2dd30f5533791aa36983c2e4f4_l3.png) **) = 1.28403
and (**![\\lambda_2   ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-df3791b283f9a20522de1e7684be5e91_l3.png) **) =
0.0490834**. Now we have to find the eigenvectors for the eigenvalues
![\\lambda_1   ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-28316e2dd30f5533791aa36983c2e4f4_l3.png)**and**![\\lambda_2](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-ca23d4644827d930543e08665e508753_l3.png)

 **To find the eigenvectors from the eigenvalues, we will use the following
approach:**

First, we will find the eigenvectors for the eigenvalue 1.28403 by using the
equation **** ![C \\cdot X = \\lambda \\cdot
X](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
ae55ecc9f93b4bb07132f019aab2640d_l3.png)

![\\begin{bmatrix} 0.616556 & 0.615444 \\\\ 0.615444 & 0.716556 \\end{bmatrix}
\\cdot \\begin{bmatrix} x \\\\ y \\end{bmatrix} = 1.28403 \\cdot
\\begin{bmatrix} x \\\\ y \\end{bmatrix}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-fd0733dd0e900b0b987a2d9775a67f0f_l3.png)

![\\begin{bmatrix} 0.616556x + 0.615444y \\\\ 0.615444x + 0.716556y
\\end{bmatrix} = \\begin{bmatrix} 1.28403x \\\\ 1.28403y
\\end{bmatrix}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d2e1afa5e121c04f08e30f0eebf537d1_l3.png)

Solving the matrices, we get

0.616556x + 0.615444y = 1.28403x ; **x = 0.922049 y**

(x and y belongs to the matrix X) so if we put y = 1, x comes out to be
0.922049. So now the updated X matrix will look like:

![X = \\begin{bmatrix} 0.922049 \\\\ 1
\\end{bmatrix}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e654c073911bcaffe7066f9c3da84b03_l3.png)

> **IMP: Till now we haven’t reached to the eigenvectors, we have to a bit of
> modifications in the X matrix. They are as follows:**
>
> A. Find the square root of the sum of the squares of the element in X matrix
> i.e.
>
>
> ![\\sqrt{0.922049^2+1^2}=\\sqrt{0.850174+1}=\\sqrt{1.850174}=1.3602](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-a4fb71213257e41f1606dad504ec90ad_l3.png)
>
> B. Now divide the elements of the X matrix by the number 1.3602 (just found
> that)
>
> ![\\begin{bmatrix} \\frac{0.922049}{1.3602} \\\\ \\\\ \\frac{1}{1.3602}
> \\end{bmatrix} = \\begin{bmatrix} 0.67787\\\\ 0.73518 \\end{bmatrix}
> ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-c9d05f7228a563bdac2ccfdfd824d3a5_l3.png)
>
> **So now we found the eigenvectors for the eigenvector**![\\lambda_1
> ](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-a0ae56f2ef50377b5a93324ba90512da_l3.png) **, they are
> 0.67787 and 0.73518**

 **Secondly, we will find the eigenvectors for the eigenvalue 0.0490834 by
using the equation {Same approach as of previous step)**

![\\begin{bmatrix} 0.616556 & 0.615444 \\\\ 0.615444 & 0.716556 \\end{bmatrix}
\\cdot \\begin{bmatrix} x \\\\ y \\end{bmatrix} = 0.0490834 \\cdot
\\begin{bmatrix} x \\\\ y \\end{bmatrix}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-02f24d28041e7b96d86c41519355209e_l3.png)

![\\begin{bmatrix} 0.616556x + 0.615444y \\\\ 0.615444x + 0.716556y
\\end{bmatrix} = \\begin{bmatrix} 0.0490834x \\\\ 0.0490834y
\\end{bmatrix}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-21eda558c35bced5aa4560b1dc8a807d_l3.png)

Solving the natrices, we get

0.616556x + 0.615444y = 0.0490834x; **y = -0.922053**

(x and y belongs to the matrix X) so if we put x = 1, y comnes out to be
-0.922053 So now the updated X matrix will look like:

![X = \\begin{bmatrix} 1 \\\\ -0.922053
\\end{bmatrix}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-62f8097c21b2dba1bc99a70cf36d5e24_l3.png)

> IMP: Till now we haven’t reached to the eigenvectors, we have to a bit of
> modifications in the X matrix. They are as follows:
>
> A. Find the square root of the sum of the squares of the elemnts in X matrix
> i.e.
>
>
> ![\\sqrt{1^2+\(-0.922053\)^2}=\\sqrt{1+0.85018}=\\sqrt{1.85018}=1.3602](https://www.geeksforgeeks.org/wp-
> content/ql-cache/quicklatex.com-5948d70b11aeb8bfac16df41cbb520be_l3.png)
>
> B. Now divide the elements of the X matrix by the number 1.3602 (just found
> that)
>
> ![\\begin{bmatrix} \\frac{1}{1.3602} \\\\ \\\\ \\frac{-0.922053}{1.3602}
> \\end{bmatrix} = \\begin{bmatrix} 0.735179 \\\\ 0.677873
> \\end{bmatrix}](https://www.geeksforgeeks.org/wp-content/ql-
> cache/quicklatex.com-374fa298c50267eca14d83f39d7024a2_l3.png)
>
>  **So now we found the eigenvectors for the eigenvector \lambda_2, they are
> 0.735176 and 0.677873**

Sum of eigenvalues (![\\lambda_1   ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-28316e2dd30f5533791aa36983c2e4f4_l3.png)) and
(![\\lambda_2   ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-df3791b283f9a20522de1e7684be5e91_l3.png)) = 1.28403 +
0.0490834 = 1.33 = Total Variance {Majority of variance comes from
![\\lambda_1   ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-28316e2dd30f5533791aa36983c2e4f4_l3.png)}

####  **Step 3: Arrange Eigenvalues**

The eigenvetor with the highest eigenvalue is the Principal Component **** of
the dataset. So in this case, eigenvectors of lambda1 are the principal
components.

{Basically in order to complete the numerical we have to only solve till this
step, but if we have to prove why we have chosen that particular eigenvector
we have to follow the steps from 4 to 6 **}**

####  **Step 4: Form Feature Vector**

![\\begin{bmatrix} 0.677873 & 0.735179 \\\\ 0.735179 & -0.677879
\\end{bmatrix}      ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-98bcdf76fa87d3f077bbf96d3ae22303_l3.png) **** This is the
FEATURE VECTOR for Numerical

Where first column are the eigenvectors of ![\\lambda_1
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-28316e2dd30f5533791aa36983c2e4f4_l3.png) & second column
are the eigenvectors of ![\\lambda_2](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-ca23d4644827d930543e08665e508753_l3.png)

#### **Step 5: Transform Original Dataset**

Use the equation Z = X V

![\\begin{bmatrix} 0.69 & 0.49 \\\\ -1.31 & -1.21 \\\\ 0.39 & 0.99 \\\\ 0.09 &
0.29 \\\\ 1.29 & 1.09 \\\\ 0.49 & 0.79 \\\\ 0.19 & -0.31 \\\\ -0.81 & -0.81
\\\\ -0.31 & -0.31 \\\\ -0.71 & -1.01 \\end{bmatrix} \\cdot \\begin{bmatrix}
0.677873 & 0.735179 \\\\ 0.735179 & -0.677879 \\end{bmatrix} =
\\begin{bmatrix} 0.8297008 & 0.17511574 \\\\ -1.77758022 & -0.14285816 \\\\
0.99219768 & -0.38437446 \\\\ 0.27421048 & -0.13041706 \\\\ 1.67580128 &
0.20949934 \\\\ 0.91294918 & -0.17528196 \\\\ -1.14457212 & -0.04641786 \\\\
-0.43804612 & -0.01776486 \\\\ -1.22382.62 & 0.16267464 \\end{bmatrix} =
Z](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-89ab42274353da25ce0eb5278e46a56c_l3.png)

####  **Step 6: Reconstructing Data**

Use the equation X = ![Z*V^T          ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-4572775ac337ebea074cbb3a60b4a8d9_l3.png)
(![V^T    ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-3ba17c6bf204012e5eb3a812aa50939c_l3.png)is Transpose of
V), X = Row Zero Mean Data

![\\begin{bmatrix} 0.8297008 & 0.17511574 \\\\ -1.77758022 & -0.14285816 \\\\
0.99219768 & -0.38437446 \\\\ 0.27421048 & -0.13041706 \\\\ 1.67580128 &
0.20949934 \\\\ 0.91294918 & -0.17528196 \\\\ -1.14457212 & -0.04641786 \\\\
-0.43804612 & -0.01776486 \\\\ -1.22382.62 & 0.16267464 \\end{bmatrix} \\cdot
\\begin{bmatrix} 0.677873 & 0.735179 \\\\ 0.735176 & -0.677879 \\end{bmatrix}
= \\begin{bmatrix} 0.6899999766573 & 0.4899999834233 \\\\ -1.3099999556827 &
-1.2099999590657 \\\\ 0.389999968063 & 0.9899999665083 \\\\ 0.0899999969553 &
0.2899999901893 \\\\ 0.61212695653593 & 0.35482096313253 \\\\ 0.4899999834233
& 0.7899999732743 \\\\ 0.189999935723 & -0.309999995127 \\\\ -0.8099999725977
& -0.8099999725977 \\\\ -0.3099999895127 & -0.3099999895127\\\\
-0.7099999759807 & -1.0099999658317
\\end{bmatrix}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d00cc81492ac1b388e80d13358095e1a_l3.png)

So in order to reconstruct the original data, we follow:

 **Row Original DataSet = Row Zero Mean Data + Original Mean**

![\\begin{bmatrix} 0.6899999766573 & 0.4899999834233 \\\\ -1.3099999556827 &
-1.2099999590657 \\\\ 0.389999968063 & 0.9899999665083 \\\\ 0.0899999969553 &
0.2899999901893 \\\\ 0.61212695653593 & 0.35482096313253 \\\\ 0.4899999834233
& 0.7899999732743 \\\\ 0.189999935723 & -0.309999995127 \\\\ -0.8099999725977
& -0.8099999725977 \\\\ -0.3099999895127 & -0.3099999895127\\\\
-0.7099999759807 & -1.0099999658317 \\end{bmatrix} + \\begin{bmatrix} 1.81 &
1.91 \\end{bmatrix} = \\begin{bmatrix} 2.49 & 2.39 \\\\ 0.5 & 0.7 \\\\ 2.19 &
2.89 \\\\ 1.89 & 2.19 \\\\ 3.08 & 2.99 \\\\ 2.30 & 2.7 \\\\ 2.01 & 1.59 \\\\
1.01 & 1.11 \\\\ 1.5 & 1.6 \\\\ 1.1 & 0.9
\\end{bmatrix}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-fd22f811b5c8d4d78ad8325901627e66_l3.png)

So for the eigenvectors of first eigenvalue, data can be reconstructed similar
to the original dataset. Thus we can say that the Principal Compoent of the
dataset is ****![\\lambda_1       ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-c00c0b7ad2dbb906971acf3fda9ee001_l3.png) is
1.28403 followed by ****![\\lambda_2   ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-df3791b283f9a20522de1e7684be5e91_l3.png)**that
is 0.0490834**

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

