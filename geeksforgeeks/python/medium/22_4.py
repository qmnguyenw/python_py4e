Python | Working with date and time using Pandas



While working with data, encountering time series data is very usual. Pandas
is a very useful tool while working with time series data.

Pandas provide a different set of tools using which we can perform all the
necessary tasks on date-time data. Let’s try to understand with the examples
discussed below.

 **Code #1:** Create a dates dataframe

 __

 __  
 __

 __

 __  
 __  
 __

import pandas as pd

 

# Create dates dataframe with frequency 

data = pd.date_range('1/1/2011', periods = 10, freq
='H')

 

data  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/data_dataframe1.jpg)  

**Code #2:** Create range of dates and show basic features

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Create date and time with dataframe

data = pd.date_range('1/1/2011', periods = 10, freq
='H')

 

x = datetime.now()

x.month, x.year  
  
---  
  
 __

 __

 **Output:**

    
    
    (9, 2018)

  
**Datetime** features can be divided into two categories.The first one time
moments in a period and second the time passed since a particular period.
These features can be very useful to understand the patterns in the data.

 **Divide a given date into features –**

 **pandas.Series.dt.year** returns the year of the date time.  
 **pandas.Series.dt.month** returns the month of the date time.  
 **pandas.Series.dt.day** returns the day of the date time.  
 **pandas.Series.dt.hour** returns the hour of the date time.  
 **pandas.Series.dt.minute** returns the minute of the date time.

Refer all **datatime** properties from here.

 **Code #3:** Break data and time into separate features

 __

 __  
 __

 __

 __  
 __  
 __

# Create date and time with dataframe

rng = pd.DataFrame()

rng['date'] = pd.date_range('1/1/2011', periods = 72, freq
='H')

 

# Print the dates in dd-mm-yy format

rng[:5]

 

# Create features for year, month, day, hour, and minute

rng['year'] = rng['date'].dt.year

rng['month'] = rng['date'].dt.month

rng['day'] = rng['date'].dt.day

rng['hour'] = rng['date'].dt.hour

rng['minute'] = rng['date'].dt.minute

 

# Print the dates divided into features

rng.head(3)  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/Untitled-125.png)  
  
**Code #4:** To get the present time, use Timestamp.now() and then convert
timestamp to datetime and directly access year, month or day.

