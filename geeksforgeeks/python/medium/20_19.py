Analyzing Mobile Data Speeds from TRAI with Pandas



Python is a great language for doing data analysis, primarily because of the
fantastic ecosystem of data-centric Python packages. **_Pandas_** is one of
those packages and makes importing and analyzing data much easier.

Let’s use a real dataset from TRAI to analyze mobile dataspeeds and try to see
the average speeds for a particular operator or state in that month. This will
also show how easily Pandas could be used on any real world data to derive
interesting results.

 **About Dataset –**  
Telecom Regulatory Authority of India (TRAI) releases a monthly dataset of the
internet speeds it measures through the MySpeed (TRAI) app. This includes
speed tests initiated by the user itself or periodic background tests done by
the app. We will try to analyze this dataset and see the average speeds for a
particular operator or state in that month.

 **Inspecting the raw structure of data:**

  * Go to TRAI MySpeed Portal and download the latest month’s csv file under the **Download** section. You can also download the csv file used in this article: sept18_publish.csv or sept18_publish_drive.csv

![](https://media.geeksforgeeks.org/wp-
content/uploads/trai_download_gfg-1.png)

  * Open this spreadsheet file.  
 **NOTE** : As the dataset is huge, the software may give you an warning that
all rows could not be loaded. This is fine. Also if you are using Microsoft
Excel, there might be a warning about opening of a SYLK file. This error could
be ignored as it is a common bug in Excel.  
Now, let’s take a look at the arrangement of the data-

  

  

![Column Names](https://media.geeksforgeeks.org/wp-
content/uploads/columns_gfg.png)

Column Names in the dataset

> 1st column is of the **Network Operator** – _JIO, Airtel_ etc.  
> 2nd column is of the **Network Technology** – _3G or 4G_.  
> 3rd column is the **Type of Test** initiated – _upload or download_.  
> 4th column is the **Speed Measured** in _Kilobytes per second._  
>  5th column is the **Signal Strength** during the measurement.  
> 6th column is the **Local Service Area(LSA)** , or the circle where the test
> was done – _Delhi, Orissa_ etc. We will refer to this as simply ‘states’.

 **NOTE:** The Signal Strength may have na (Not Available) values due to
some devices unable to capture signal. We will ignore using this parameter in
our calculations to make things simpler. However, it could be easily added as
a condition while filtering.

