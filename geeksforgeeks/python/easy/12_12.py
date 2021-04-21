Chi-Square Test for Feature Selection – Mathematical Explanation



One of the primary tasks involved in any supervised Machine Learning venture
is to select the best features from the given dataset to obtain the best
results. One way to select these features is the Chi-Square Test.

Mathematically, a Chi-Square test is done on two distributions two determine
the level of similarity of their respective variances. In its **null
hypothesis** , it assumes that the given distributions are independent. This
test thus can be used to determine the best features for a given dataset by
determining the features on which the output class label is most dependent on.
For each feature in the dataset, the ![\\chi
^{2}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7ce7b41e2e981003b6d6104781a59553_l3.png) is calculated
and then ordered in descending order according to the ![\\chi
^{2}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7ce7b41e2e981003b6d6104781a59553_l3.png) value. The
higher the value of ![\\chi ^{2}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7ce7b41e2e981003b6d6104781a59553_l3.png), the more
dependent the output label is on the feature and higher the importance the
feature has on determining the output.

Let the feature in question have m attribute values and the output have k
class labels. Then the value of ![\\chi
^{2}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7ce7b41e2e981003b6d6104781a59553_l3.png) is given by the
following expression:-

![\\chi ^{2} = \\sum _{i=1}^{m} \\sum
_{j=1}^{k}\\frac{\(O_{ij}-E_{ij}\)^{2}}{E_{ij}}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-8a4f85ff0020722e6c1fb6c3617b63e5_l3.png)

where

![O_{ij}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e7d376bd0204c06d734c2fe0f2f8c045_l3.png) – Observed
frequency

  

  

![E_{ij}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-15dcecda7c27def106072379aa8e6620_l3.png) – Expected
frequency

For each feature, a contingency table is created with m rows and k columns.
Each cell (i,j) denotes the number of rows having attribute feature as i and
class label as k. Thus each cell in this table denotes the observed frequency.
To calculate the expected frequency for each cell, first the proportion of the
feature value in the total dataset is calculated and then it is multiplied by
the total number of the current class label.

 **Solved Example:**

Consider the following table:-

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190717115442/data5.png)

Here the output variable is the column named “PlayTennis” which determines
whether tennis was played on the given day given the weather conditions.

The contingency table for the feature “Outlook” is constructed as below:-

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190717120148/outlook.png)

  

  

Note that the expected value for each cell is given inside the parenthesis.

The expected value for the cell (Sunny,Yes) is calculated as
![\\frac{5}{14}\\times 9 = 3.21](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-588898b83e29ffd46ae040b9a760a436_l3.png) and similarly
for others.

The ![\\chi ^{2}_{outlook}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7bdd11c1fe5a63839bdaa090f4b05b16_l3.png) value is
calculated as below:-

![\\chi ^{2}_{outlook} =
\\frac{\(2-3.21\)^{2}}{3.21}+\\frac{\(3-1.79\)^{2}}{1.79}+\\frac{\(4-2.57\)^{2}}{2.57}+\\frac{\(0-1.43\)^{2}}{1.43}+\\frac{\(3-3.21\)^{2}}{3.21}+\\frac{\(2-1.79\)^{2}}{1.79}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-8884260d96dd93bc6baed6bcd046d4ed_l3.png)

![\\Rightarrow \\chi ^{2}_{outlook} = 3.129](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-aae8156cdb9a34612d53aa012618c061_l3.png)

The contingency table for the feature “Wind” is constructed as below:-

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190717120150/wind1.png)

The ![\\chi ^{2}_{wind}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-96fb077fa6dd4268cf8212b9fedadb73_l3.png) value is
calculated as below:-

![\\chi ^{2}_{wind} =
\\frac{\(3-3.86\)^{2}}{3.86}+\\frac{\(3-1.14\)^{2}}{1.14}+\\frac{\(6-5.14\)^{2}}{5.14}+\\frac{\(2-2.86\)^{2}}{2.86}](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-13b50d445d3d5742fa548d6eac20bf98_l3.png)

![\\Rightarrow \\chi ^{2}_{wind} = 3.629](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-751da11682791aee630552d1692f71d2_l3.png)

On comparing the two scores, we can conclude that the feature “Wind” is more
important to determine the output than the feature “Outlook”.

This article demonstrates how to do feature selection using Chi-Square Test.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

