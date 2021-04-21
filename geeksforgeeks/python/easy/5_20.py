Interquartile Range to Detect Outliers in Data



An observation which differs from an overall pattern on a sample dataset is
called an outlier.

 **Outliers:**  
The outliers may suggest experimental errors, variability in a measurement, or
an anomaly. The age of a person may wrongly be recorded as 200 rather than 20
Years. Such an outlier should definitely be discarded from the dataset.  
However, not all outliers are bad. Some outliers signify that data is
significantly different from others. For example, it may indicate an anomaly
like bank fraud or a rare disease.

 **Significance of outliers:**

  * Outliers badly affect mean and standard deviation of the dataset. These may statistically give erroneous results.
  * Most machine learning algorithms do not work well in the presence of outlier. So it is desirable to detect and remove outliers.
  * Outliers are highly useful in anomaly detection like fraud detection where the fraud transactions are very different from normal transactions.

 **What is Interquartile Range IQR?**

IQR is used to **measure variability** by dividing a data set into quartiles.
The data is sorted in ascending order and split into 4 equal parts. Q1, Q2, Q3
called first, second and third quartiles are the values which separate the 4
equal parts.

  

  

  * Q1 represents the 25th percentile of the data.
  * Q2 represents the 50th percentile of the data.
  * Q3 represents the 75th percentile of the data.

If a dataset has _2n / 2n+1_ data points, then  
Q1 = median of the dataset.  
Q2 = median of n smallest data points.  
Q3 = median of n highest data points.

IQR is the range between the first and the third quartiles namely Q1 and Q3:
_IQR = Q3 – Q1_. The data points which fall below _Q1 – 1.5 IQR_ or above _Q3
+ 1.5 IQR_ are outliers.

