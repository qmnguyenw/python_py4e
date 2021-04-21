How to Sort by Column in a file using Python?



For sorting files particularly CSV or tab or space separated files, We use
Pandas and sort the data. Because Pandas provide multiple functions to achieve
the same. But one thing we have to realize here is Pandas are built for bigger
data sets and not for smaller files. For small files, we can even use the
built-in functions provided by python, and no need to install additional
libraries like Pandas to get the required.

The main reason for writing this article is to show how we can use built-in
functions like the sort to order smaller files which are of <10K lines in the
required manner and still get what we want. In this article, we will
understand how to use the sort function to customize the sorting according to
our requirement rather than relying on the default element wise sorting
provided by the function.

Sort is a built-in list function in python that can sort any given object in
place such as integers, float, string in ascending or descending order.
Besides that, it provides a special attribute called “key” using which we can
customize the sorting. To the “key” attribute we can either pass a one-liner
function like Lambda or a user-defined function.

**Syntax:**

    
    
    sort(self, /, *, key=None, reverse=False)

Let us understand how to use the sort function of list data type by applying
two common types of data we see in general i.e. numerical and categorical
data.

  

  

**Method 1#:** How to Sort Numerical data using sort function?

Download the MallSalesData.csv file from the github link into your current
directory and save it as MallSalesData.csv. then the sample file
MallSalesData.csv downloaded has information about sales data in Mart store
containing fields such as product code, production description, and price of
the product. In the below code we will use the sort function to sort the CSV
file downloaded by price in ascending order.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def my_sort(line):

 line_fields = line.strip().split(',')

 amount = float(line_fields[2])

 return amount

 

 

# opening file MallSalesData.csv

# and getting contents into a list

fp = open('MallSalesData.csv')

contents = fp.readlines()

 

# sorting using our custom logic

contents.sort(key=my_sort)

 

# printing the sorting contents to stdout

for line in contents:

 print(line)

 

fp.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    22633,HAND WARMER UNION JACK,11.1
    
    22632,HAND WARMER RED POLKA DOT,11.1
    
    85123A,WHITE HANGING HEART T-LIGHT HOLDER,15.3
    
    22752,SET 7 BABUSHKA NESTING BOXES,15.3
    
    71053,WHITE METAL LANTERN,20.34
    
    84029G,KNITTED UNION FLAG HOT WATER BOTTLE,20.34
    
    84029E,RED WOOLLY HOTTIE WHITE HEART,20.34
    
    84406B,CREAM CUPID HEARTS COAT HANGER,22
    
    21730,GLASS STAR FROSTED T-LIGHT HOLDER,25.5
    
    84879,ASSORTED COLOUR BIRD ORNAMENT,54.08
    

In the above, you can see we are defining our own custom logic i.e. my_sort
function which guides the sort function to sort on a particular field such as
price to sort the records. You can see in the above output the entire file is
sorted based on the price field.

### **How does this work?**

  * When we use the key attribute in the sort() function each time an element of the list which is a customer purchase record in this case is passed to our function my_sort().
  * my_sort function will split the record by comma, fetch the price, and store in amount variable.
  * The amount variable is further returned as the return value of my_sort() function which is used by sort() to sort the records.
  * This means each time sort() function see the amount() value in numbers to sort the records.

 **Method 2#:** How to Sort Categorical data using sort function?

1\. Download the Flights.txt file from the github link into your current
directory and save the filename as Flights.txt. The sample file Flights.txt
downloaded has information about flight passengers such as their ticket
number, passenger name, ticket code, and cabin class they are traveling. In
the below code we will use the sort function to sort the text file downloaded
based on their cabin class. That is ECONOMY followed by PREMIUM ECONOMY
followed by BUSINESS followed by FIRST CLASS.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def my_sort(line):

 flight_class = {'ECONOMY': 1,

 'PREMIUMECONOMY': 2,

 'BUSINESS': 3,

 'FIRSTCLASS': 4}

 line_fields = line.strip().split()

 cabin_class = line_fields[-1]

 return flight_class[cabin_class]

 

 

# reading flights.csv and storing in list

# variable contents

fp = open('Flights.txt')

contents = fp.readlines()

 

# sorting based on categorical variable cabin class

contents.sort(key=my_sort)

 

# displaying contents on stdout after sorting

for line in contents:

 print(line)

 

fp.close()  
  
---  
  
 __

 __

 **Output:**

    
    
    001 AALAM SAMIMI/MOJGAN MRS 5SZKUU ECONOMY
    
    007 AFSHAR GHAHREMANKHANI/ARA ZYA4NT ECONOMY
    
    010 AHMADI SOBHANI/JALEH MS 2ASCHO ECONOMY
    002 ABDOLI/AHMAD DR MR 5AMBNC PREMIUMECONOMY
    
    008 AFSHARGHAHREMANKHANI/ALI 8CP4YE PREMIUMECONOMY
    
    003 ABDOLLAHIMOTLAGHSOMEHSA/M 6VXREM BUSINESS
    
    009 AFSHARGHAHREMANKHANI/ARIA 8CQFCB BUSINESS
    
    004 AFRASIABI/HASSAN MR 2Y24ER FIRSTCLASS
    
    005 AFSHAR BAKESHLOO/LIDA MRS 8CQFCB FIRSTCLASS
    
    006 AFSHAR GHAHREMANKHANI/ALI 25KO4X FIRSTCLASS
    

In the above, you can see we have defined our custom logic i.e. my_sort
function which guides the sort function to sort on a categorical variable
called cabin class. You can see in the above output the entire file is sorted
on the last field i.e. cabin class where you can observe that the records are
ordered with ECONOMY followed by PREMIUM ECONOMY followed by BUSINESS followed
by FIRST CLASS.

### **How does this work?**

  * When we use the key attribute in sort() function each time an element of the list which is passenger traveling in-flight information is passed to our function my_sort().
  * my_sort function will split the record by space and fetch the last field which is cabin class into variable cabin_class.
  * We also have defined a dictionary flight_class where we defined the cabin class order according to our requirement i.e. ECONOMY to 1, PREMIUM ECONOMY to 2, and so on. This will help us to send the order we want to sort these categorical values.
  * Once we get cabin_class from each record we will check in dictionary flight_class what is the order priority mentioned and pass that value as return value to sort() function.
  * This means each time sort() function will see the order priority defined for flight cabin class and sort the records accordingly.

This way we can customize any type of sorting functionality by just using the
basic functions provided by python. Similarly, we can customize max, min, and
other built-in functions of python to perform the operations according to our
requirements.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

