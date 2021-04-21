ML | Extra Tree Classifier for Feature Selection



 **Prerequisites:** Decision Tree Classifier

 **Extremely Randomized Trees Classifier(Extra Trees Classifier)** is a type
of ensemble learning technique which aggregates the results of multiple de-
correlated decision trees collected in a “forest” to output it’s
classification result. In concept, it is very similar to a Random Forest
Classifier and only differs from it in the manner of construction of the
decision trees in the forest.

Each Decision Tree in the Extra Trees Forest is constructed from the original
training sample. Then, at each test node, Each tree is provided with a random
sample of k features from the feature-set from which each decision tree must
select the best feature to split the data based on some mathematical criteria
(typically the Gini Index). This random sample of features leads to the
creation of multiple de-correlated decision trees.

To perform feature selection using the above forest structure, during the
construction of the forest, for each feature, the normalized total reduction
in the mathematical criteria used in the decision of feature of split (Gini
Index if the Gini Index is used in the construction of the forest) is
computed. This value is called the Gini Importance of the feature. To perform
feature selection, each feature is ordered in descending order according to
the Gini Importance of each feature and the user selects the top k features
according to his/her choice.

Consider the following data:-

  

  

![](https://media.geeksforgeeks.org/wp-
content/uploads/20190719133406/data8.png)

Let us build a hypothetical Extra Trees Forest for the above data with **five
decision trees** and the value of k which decides the number of features in a
random sample of features be **two**. Here the decision criteria used will be
Information Gain. First, we calculate the entropy of the data. Note the
formula for calculating the entropy is:-

![ Entropy\(S\) = \\sum _{i=1}^{c} -p_{i}log_{2}\(p_{i}\)
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-240575f035311c93ea460127c283dcf4_l3.png)

where c is the number of unique class labels and
![p_{i}](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d9fdb3a89f4dd9c043c9847440b7d75b_l3.png) is the
proportion of rows with output label is i.

Therefore for the given data, the **entropy** is:-

![Entropy\(S\) =
-\\frac{9}{14}log\(\\frac{9}{14}\)-\\frac{5}{14}log\(\\frac{5}{14}\)](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-a38ff6d55917477bd431cb59fd61a8a3_l3.png)

![\\Rightarrow Entropy\(S\) = 0.940](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-6d338ecea02506250bb9a9c6ab30b164_l3.png)

Let the decision trees be constructed such that:-

  

  

