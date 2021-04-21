Python | Get the real time currency exchange rate



Python is a very versatile programming language. Python is being used in
almost each mainstream technology and one can develop literally any
application with it.

Let’s see a Python program to the real-time currency exchange rate. To use
this service, one must need the API key, which can be get form here. One can
get the list of currency codes from here.

We will be using **CURRENCY_EXCHANGE_RATE API** ,which can return the
realtime exchange rate for any pair of digital currency (e.g., Bitcoin) or
physical currency (e.g., USD).

 **Modules Needed :**

    
    
    requests
    json
    

Below is the implementation :

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python program to get the real-time

# currency exchange rate

 

# Function to get real time currency exchange 

def RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key) :

 

 # importing required libraries

 import requests, json

 

 # base_url variable store base url 

 base_url = r"https://www.alphavantage.co/query?function =
CURRENCY_EXCHANGE_RATE"

 

 # main_url variable store complete url

 main_url = base_url + "&from;_currency =" + from_currency +

 "&to;_currency =" + to_currency + "&apikey; =" + api_key

 

 # get method of requests module 

 # return response object 

 req_ob = requests.get(main_url)

 

 # json method return json format

 # data into python dictionary data type.

 

 # result contains list of nested dictionaries

 result = req_ob.json()

 

 print(" Result before parsing the json data :\n", result)

 

 

 print("\n After parsing : \n Realtime Currency Exchange Rate for",

 result["Realtime Currency Exchange Rate"]

 ["2. From_Currency Name"], "TO",

 result["Realtime Currency Exchange Rate"]

 ["4. To_Currency Name"], "is",

 result["Realtime Currency Exchange Rate"]

 ['5. Exchange Rate'], to_currency)

 

 

 

# Driver code

if __name__ == "__main__" :

 

 # currency code

 from_currency = "USD"

 to_currency = "INR"

 

 # enter your api key here 

 api_key = "Your_Api_Key"

 

 # function calling

 RealTimeCurrencyExchangeRate(from_currency, to_currency, api_key)  
  
---  
  
 __

 __

 **Output :**

> Result before parsing the json data :  
> {‘Realtime Currency Exchange Rate’: {‘1. From_Currency Code’: ‘USD’, ‘2.
> From_Currency Name’: ‘United States Dollar’, ‘3. To_Currency Code’: ‘INR’,
> ‘4. To_Currency Name’: ‘Indian Rupee’, ‘5. Exchange Rate’: ‘71.51500000’,
> ‘6. Last Refreshed’: ‘2018-12-13 17:40:36’, ‘7. Time Zone’: ‘UTC’}}
>
> After parsing :  
> Realtime Currency Exchange Rate for United States Dollar TO Indian Rupee is
> 71.51500000 INR

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

