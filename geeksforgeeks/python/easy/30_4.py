Naive Bayes Classifiers



This article discusses the theory behind the Naive Bayes classifiers and their
implementation.

Naive Bayes classifiers are a collection of classification algorithms based on
**Bayes’ Theorem**. It is not a single algorithm but a family of algorithms
where all of them share a common principle, i.e. every pair of features being
classified is independent of each other.

To start with, let us consider a dataset.

Consider a fictional dataset that describes the weather conditions for playing
a game of golf. Given the weather conditions, each tuple classifies the
conditions as fit(“Yes”) or unfit(“No”) for plaing golf.

Here is a tabular representation of our dataset.

  

  
| Outlook| Temperature| Humidity| Windy| Play Golf| 0| Rainy| Hot| High|
False| No| 1| Rainy| Hot| High| True| No| 2| Overcast| Hot| High| False| Yes|
3| Sunny| Mild| High| False| Yes| 4| Sunny| Cool| Normal| False| Yes| 5|
Sunny| Cool| Normal| True| No| 6| Overcast| Cool| Normal| True| Yes| 7| Rainy|
Mild| High| False| No| 8| Rainy| Cool| Normal| False| Yes| 9| Sunny| Mild|
Normal| False| Yes| 10| Rainy| Mild| Normal| True| Yes| 11| Overcast| Mild|
High| True| Yes| 12| Overcast| Hot| Normal| False| Yes| 13| Sunny| Mild| High|
True| No  
---|---|---|---|---|---  
  
The dataset is divided into two parts, namely, **feature matrix** and the
**response vector**.

  * Feature matrix contains all the vectors(rows) of dataset in which each vector consists of the value of **dependent features**. In above dataset, features are ‘Outlook’, ‘Temperature’, ‘Humidity’ and ‘Windy’.
  * Response vector contains the value of **class variable** (prediction or output) for each row of feature matrix. In above dataset, the class variable name is ‘Play golf’.

 **Assumption:**

The fundamental Naive Bayes assumption is that each feature makes an:

  * independent
  * equal

contribution to the outcome.

With relation to our dataset, this concept can be understood as:

  * We assume that no pair of features are dependent. For example, the temperature being ‘Hot’ has nothing to do with the humidity or the outlook being ‘Rainy’ has no effect on the winds. Hence, the features are assumed to be **independent**.
  * Secondly, each feature is given the same weight(or importance). For example, knowing only temperature and humidity alone can’t predict the outcome accuratey. None of the attributes is irrelevant and assumed to be contributing **equally** to the outcome.

 **Note:** The assumptions made by Naive Bayes are not generally correct in
real-world situations. In-fact, the independence assumption is never correct
but often works well in practice.

Now, before moving to the formula for Naive Bayes, it is important to know
about Bayes’ theorem.

 **Bayes’ Theorem**

  

  

Bayes’ Theorem finds the probability of an event occurring given the
probability of another event that has already occurred. Bayes’ theorem is
stated mathematically as the following equation:

![ P\(A|B\) = \\frac{P\(B|A\) P\(A\)}{P\(B\)}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7777aa719ea14857115695676adc0914_l3.png)

where A and B are events and P(B) ? 0.

  * Basically, we are trying to find probability of event A, given the event B is true. Event B is also termed as **evidence**.
  * P(A) is the **priori** of A (the prior probability, i.e. Probability of event before evidence is seen). The evidence is an attribute value of an unknown instance(here, it is event B).
  * P(A|B) is a posteriori probability of B, i.e. probability of event after evidence is seen.

Now, with regards to our dataset, we can apply Bayes’ theorem in following
way:

![ P\(y|X\) = \\frac{P\(X|y\) P\(y\)}{P\(X\)}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e85875a7ff9e9b557eab6281cc7ff078_l3.png)

where, y is class variable and X is a dependent feature vector (of size _n_ )
where:

![ X = \(x_1,x_2,x_3,.....,x_n\) ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-5385a4693c3fb17811cf36593978a601_l3.png)

Just to clear, an example of a feature vector and corresponding class variable
can be: (refer 1st row of dataset)

    
    
    X = (Rainy, Hot, High, False)
    y = No
    

So basically, P(y|X) here means, the probability of “Not playing golf” given
that the weather conditions are “Rainy outlook”, “Temperature is hot”, “high
humidity” and “no wind”.

 **Naive assumption**

Now, its time to put a naive assumption to the Bayes’ theorem, which is,
**independence** among the features. So now, we split **evidence** into the
independent parts.

Now, if any two events A and B are independent, then,

    
    
    P(A,B) = P(A)P(B)
    

Hence, we reach to the result:

![ P\(y|x_1,...,x_n\) = \\frac{
P\(x_1|y\)P\(x_2|y\)...P\(x_n|y\)P\(y\)}{P\(x_1\)P\(x_2\)...P\(x_n\)}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-1c3f5ab570cf0ab3f43d5c18c645b67a_l3.png)

which can be expressed as:

![ P\(y|x_1,...,x_n\) =
\\frac{P\(y\)\\prod_{i=1}^{n}P\(x_i|y\)}{P\(x_1\)P\(x_2\)...P\(x_n\)}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-8171c1fe2cbd3ed62bc3f40d682c0512_l3.png)

Now, as the denominator remains constant for a given input, we can remove that
term:

![ P\(y|x_1,...,x_n\)\\propto P\(y\)\\prod_{i=1}^{n}P\(x_i|y\)
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c778553cb5a67518205ac6ea18502398_l3.png)

Now, we need to create a classifier model. For this, we find the probability
of given set of inputs for all possible values of the class variable _y_ and
pick up the output with maximum probability. This can be expressed
mathematically as:

![y = argmax_{y} P\(y\)\\prod_{i=1}^{n}P\(x_i|y\)
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-f3637f468262bfbb4accb97da8110028_l3.png)

So, finally, we are left with the task of calculating P(y) and P(xi | y).

Please note that P(y) is also called **class probability** and P(xi | y) is
called **conditional probability**.

The different naive Bayes classifiers differ mainly by the assumptions they
make regarding the distribution of P(xi | y).

Let us try to apply the above formula manually on our weather dataset. For
this, we need to do some precomputations on our dataset.

We need to find P(xi | yj) for each xi in X and yj in y. All these
calculations have been demonstrated in the tables below:

![table23](https://media.geeksforgeeks.org/wp-content/uploads/naive-bayes-
classification.png)

So, in the figure above, we have calculated P(xi | yj) for each xi in X and yj
in y manually in the tables 1-4. For example, probability of playing golf
given that the temperature is cool, i.e P(temp. = cool | play golf = Yes) =
3/9.

Also, we need to find class probabilities (P(y)) which has been calculated in
the table 5. For example, P(play golf = Yes) = 9/14.

So now, we are done with our pre-computations and the classifier is ready!

Let us test it on a new set of features (let us call it today):

    
    
    today = (Sunny, Hot, Normal, False)
    

So, probability of playing golf is given by:

![ P\(Yes | today\) = \\frac{P\(Sunny Outlook|Yes\)P\(Hot
Temperature|Yes\)P\(Normal Humidity|Yes\)P\(No Wind|Yes\)P\(Yes\)}{P\(today\)}
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-c6067bf0bf53532b6701c72215bc0758_l3.png)

and probability to not play golf is given by:

![ P\(No | today\) = \\frac{P\(Sunny Outlook|No\)P\(Hot
Temperature|No\)P\(Normal Humidity|No\)P\(No Wind|No\)P\(No\)}{P\(today\)}
](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-
ed23967bcb3871bd6919752aa396a167_l3.png)

Since, P(today) is common in both probabilities, we can ignore P(today) and
find proportional probabilities as:

![ P\(Yes | today\) \\propto
\\frac{2}{9}.\\frac{2}{9}.\\frac{6}{9}.\\frac{6}{9}.\\frac{9}{14} \\approx
0.0141 ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-e061a86d4158d65787e64c4cdfd15f17_l3.png)

and

![ P\(No | today\) \\propto
\\frac{3}{5}.\\frac{2}{5}.\\frac{1}{5}.\\frac{2}{5}.\\frac{5}{14} \\approx
0.0068 ](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-176cc113842cb9f7bf3e645e10381bec_l3.png)

Now, since

![ P\(Yes | today\) + P\(No | today\) = 1 ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-c11dfe6cbfca4b42282dff3c7689a4ae_l3.png)

These numbers can be converted into a probability by making the sum equal to 1
(normalization):

![ P\(Yes | today\) = \\frac{0.0141}{0.0141 + 0.0068} = 0.67
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-d743d4c0f318303820d38a8b533d07d8_l3.png)

and

![ P\(No | today\) = \\frac{0.0068}{0.0141 + 0.0068} = 0.33
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-1c3af0ce1707cd819282d764d8b71f63_l3.png)

Since

![ P\(Yes | today\) > P\(No | today\) ](https://www.geeksforgeeks.org/wp-
content/ql-cache/quicklatex.com-0214e299f25961601b470dab459842c0_l3.png)

So, prediction that golf would be played is ‘Yes’.

The method that we discussed above is applicable for discrete data. In case of
continuous data, we need to make some assumptions regarding the distribution
of values of each feature. The different naive Bayes classifiers differ mainly
by the assumptions they make regarding the distribution of P(xi | y).

Now, we discuss one of such classifiers here.

 **Gaussian Naive Bayes classifier**

In Gaussian Naive Bayes, continuous values associated with each feature are
assumed to be distributed according to a **Gaussian distribution**. A Gaussian
distribution is also called Normal distribution. When plotted, it gives a bell
shaped curve which is symmetric about the mean of the feature values as shown
below:

![normal](https://media.geeksforgeeks.org/wp-content/uploads/naive-bayes-
classification-1.png)

The likelihood of the features is assumed to be Gaussian, hence, conditional
probability is given by:

![ P\(x_i | y\) = \\frac{1}{\\sqrt{2\\pi\\sigma _{y}^{2} }} exp \\left
\(-\\frac{\(x_i-\\mu _{y}\)^2}{2\\sigma _{y}^{2}}  \\right \)
](https://www.geeksforgeeks.org/wp-content/ql-
cache/quicklatex.com-7fb78d7323fcbade0cb664161a8e84c4_l3.png)

Now, we look at an implementation of Gaussian Naive Bayes classifier using
scikit-learn.

 __

 __  
 __

 __

 __  
 __  
 __

# load the iris dataset

from sklearn.datasets import load_iris

iris = load_iris()

 

# store the feature matrix (X) and response vector (y)

X = iris.data

y = iris.target

 

# splitting X and y into training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,
test_size=0.4, random_state=1)

 

# training the model on training set

from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()

gnb.fit(X_train, y_train)

 

# making predictions on the testing set

y_pred = gnb.predict(X_test)

 

# comparing actual response values (y_test) with predicted response values
(y_pred)

from sklearn import metrics

print("Gaussian Naive Bayes model accuracy(in %):",
metrics.accuracy_score(y_test, y_pred)*100)  
  
---  
  
 __

 __

Output:

    
    
    Gaussian Naive Bayes model accuracy(in %): 95.0

Other popular Naive Bayes classifiers are:

  *  **Multinomial Naive Bayes** : Feature vectors represent the frequencies with which certain events have been generated by a **multinomial distribution**. This is the event model typically used for document classification.
  *  **Bernoulli Naive Bayes** : In the multivariate Bernoulli event model, features are independent booleans (binary variables) describing inputs. Like the multinomial model, this model is popular for document classification tasks, where binary term occurrence(i.e. a word occurs in a document or not) features are used rather than term frequencies(i.e. frequency of a word in the document).

As we reach to the end of this article, here are some important points to
ponder upon:

  * In spite of their apparently over-simplified assumptions, naive Bayes classifiers have worked quite well in many real-world situations, famously document classification and spam filtering. They require a small amount of training data to estimate the necessary parameters.
  * Naive Bayes learners and classifiers can be extremely fast compared to more sophisticated methods. The decoupling of the class conditional feature distributions means that each distribution can be independently estimated as a one dimensional distribution. This in turn helps to alleviate problems stemming from the curse of dimensionality.

References:

  * https://en.wikipedia.org/wiki/Naive_Bayes_classifier
  * http://gerardnico.com/wiki/data_mining/naive_bayes
  * http://scikit-learn.org/stable/modules/naive_bayes.html

This blog is contributed by Nikhil Kumar. If you like GeeksforGeeks and would
like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

