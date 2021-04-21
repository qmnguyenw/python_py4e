Python – Data visualization using covid19 India API



 **API (Application Programming Interface)** is a computing interface that
interacts between multiple software.

**JSON (JavaScript Object Notation)** is a lightweight format for storing and
transporting data. It is used to send data from server to web.

 **Required modules:**

  * matplotlib
  * requests
  * pandas
  * json

 **Commands to install modules:**

    
    
    pip install matplotlib
    pip install requests
    pip install pandas

 **Steps:**

  

  

  1. Importing all required modules.
  2. Calling API and getting JSON data.
  3. Getting the State Wise District Data.
  4. Visualization of data.

The below URL redirects you to API
https://api.covid19india.org/state_district_wise.json

 **Importing all required modules**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#importing modules

import json

import requests

import pandas as pd

import matplotlib.pyplot as plt  
  
---  
  
 __

 __

 **Function for getting JSON data from API and Visualization of Data**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

#storing the url in the form of string

url="https://api.covid19india.org/state_district_wise.json"

 

#function to get data from api

def casesData():

 #getting the json data by calling api

 data = ((requests.get(url)).json())

 states = []  
  
---  
  
 __

 __

 **Getting State Names available in JSON Data**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# getting statewise data

for state in states:

 f = (data[state]['districtData'])

# states data available in JSON Data

'''

0 State Unassigned

1 Andaman and Nicobar Islands

2 Andhra Pradesh

3 Arunachal Pradesh

4 Assam

5 Bihar

6 Chandigarh

7 Chhattisgarh

8 Delhi

9 Dadra and Nagar Haveli and Daman and Diu

10 Goa

11 Gujarat

12 Himachal Pradesh

13 Haryana

14 Jharkhand

15 Jammu and Kashmir

16 Karnataka

17 Kerala

18 Ladakh

19 Lakshadweep

20 Maharashtra

21 Meghalaya

22 Manipur

23 Madhya Pradesh

24 Mizoram

25 Nagaland

26 Odisha

27 Punjab

28 Puducherry

29 Rajasthan

30 Sikkim

31 Telangana

32 Tamil Nadu

33 Tripura

34 Uttar Pradesh

35 Uttarakhand

36 West Bengal

'''  
  
---  
  
 __

 __

 **Getting the state-wise Data**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# getting statewise data

for state in states:

 f = (data[state]['districtData'])

 tc = []

 dis = []

 act, con, dea, rec = 0, 0, 0, 0

 

 # getting districtwise data

 for key in (data[state]['districtData']).items():

 district = key[0]

 dis.append(district)

 active = data[state]['districtData'][district]['active']

 confirmed =
data[state]['districtData'][district]['confirmed']

 deaths = data[state]['districtData'][district]['deceased']

 recovered =
data[state]['districtData'][district]['recovered']

 if district == 'Unknown':

 active, confirmed, deaths, recovered = 0, 0, 0, 0

 tc.append([active, confirmed, deaths, recovered])

 act = act + active

 con = con + confirmed

 dea = dea + deaths

 rec = rec + recovered

 tc.append([act, con, dea, rec])

 dis.append('Total')

 parameters = ['Active', 'Confirmed', 'Deaths',
'Recovered']  
  
---  
  
 __

 __

 **Creating DataFrame Using pandas**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# creating a dataframe

df = pd.DataFrame(tc, dis, parameters)

print('COVID - 19', state, 'District Wise Data')

print(df)  
  
---  
  
 __

 __

 **Data Visualization Using Matplotlib**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# plotting of data

plt.bar(dis, df['Active'], width=0.5, align='center')

fig = plt.gcf()

fig.set_size_inches(18.5, 10.5)

plt.xticks(rotation=75)

plt.show()

print('*'*100)  
  
---  
  
 __

 __

 **Final casesData() function code**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# function to get data from api

def casesData():

 # getting the json data by calling api

 data = ((requests.get(url)).json())

 states = []

 

 # getting states

 for key in data.items():

 states.append(key[0])

 

 # getting statewise data

 for state in states:

 f = (data[state]['districtData'])

 tc = []

 dis = []

 act, con, dea, rec = 0, 0, 0, 0

 

 # getting districtwise data

 for key in (data[state]['districtData']).items():

 district = key[0]

 dis.append(district)

 active = data[state]['districtData'][district]['active']

 confirmed =
data[state]['districtData'][district]['confirmed']

 deaths = data[state]['districtData'][district]['deceased']

 recovered =
data[state]['districtData'][district]['recovered']

 if district == 'Unknown':

 active, confirmed, deaths, recovered = 0, 0, 0, 0

 tc.append([active, confirmed, deaths, recovered])

 act = act + active

 con = con + confirmed

 dea = dea + deaths

 rec = rec + recovered

 tc.append([act, con, dea, rec])

 dis.append('Total')

 parameters = ['Active', 'Confirmed', 'Deaths',
'Recovered']

 

 # creating a dataframe

 df = pd.DataFrame(tc, dis, parameters)

 print('COVID - 19', state, 'District Wise Data')

 print(df)

 

 # plotting of data

 plt.bar(dis, df['Active'], width=0.5, align='center')

 fig = plt.gcf()

 fig.set_size_inches(18.5, 10.5)

 plt.xticks(rotation = 75)

 plt.show()

 print('*' * 100)  
  
---  
  
 __

 __

###  **Final Implementation:**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# importing modules

import json

import requests

import pandas as pd

import matplotlib.pyplot as plt

 

# storing the url in the form of string

url = "https://api.covid19india.org/state_district_wise.json"

 

# function to get data from api

 

 

def casesData():

 # getting the json data by calling api

 data = ((requests.get(url)).json())

 states = []

 

 # getting states

 for key in data.items():

 states.append(key[0])

 

 # getting statewise data

 for state in states:

 f = (data[state]['districtData'])

 tc = []

 dis = []

 act, con, dea, rec = 0, 0, 0, 0

 

 # getting districtwise data

 for key in (data[state]['districtData']).items():

 district = key[0]

 dis.append(district)

 active = data[state]['districtData'][district]['active']

 confirmed =
data[state]['districtData'][district]['confirmed']

 deaths = data[state]['districtData'][district]['deceased']

 recovered =
data[state]['districtData'][district]['recovered']

 if district == 'Unknown':

 active, confirmed, deaths, recovered = 0, 0, 0, 0

 tc.append([active, confirmed, deaths, recovered])

 act = act + active

 con = con + confirmed

 dea = dea + deaths

 rec = rec + recovered

 tc.append([act, con, dea, rec])

 dis.append('Total')

 parameters = ['Active', 'Confirmed', 'Deaths',
'Recovered']

 

 # creating a dataframe

 df = pd.DataFrame(tc, dis, parameters)

 print('COVID - 19', state, 'District Wise Data')

 print(df)

 

 # plotting of data

 plt.bar(dis, df['Active'], width = 0.5, align = 'center')

 fig = plt.gcf()

 fig.set_size_inches(18.5, 10.5)

 plt.xticks(rotation = 75)

 plt.show()

 print('*' * 100)

 

 

# states data available throug API

'''

0 State Unassigned

1 Andaman and Nicobar Islands

2 Andhra Pradesh

3 Arunachal Pradesh

4 Assam

5 Bihar

6 Chandigarh

7 Chhattisgarh

8 Delhi

9 Dadra and Nagar Haveli and Daman and Diu

10 Goa

11 Gujarat

12 Himachal Pradesh

13 Haryana

14 Jharkhand

15 Jammu and Kashmir

16 Karnataka

17 Kerala

18 Ladakh

19 Lakshadweep

20 Maharashtra

21 Meghalaya

22 Manipur

23 Madhya Pradesh

24 Mizoram

25 Nagaland

26 Odisha

27 Punjab

28 Puducherry

29 Rajasthan

30 Sikkim

31 Telangana

32 Tamil Nadu

33 Tripura

34 Uttar Pradesh

35 Uttarakhand

36 West Bengal

'''

 

#Driver Code

casesData()  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210101203458/Image72.png)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

