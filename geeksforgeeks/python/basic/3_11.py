Case-insensitive string comparison in Python



We generally use Python lists to store items. An online shopping application
may contain a list of items in it so that the user can search the item from
the list of items. For example, Our shopping application has a list of laptops
it sells. List contains many brands and one of them is ‘Lenovo’. If we want to
buy a laptop of Lenovo brand we go to the search bar of shopping app and
search for ‘Lenovo’. Then it displays all the models of Lenovo laptops. But
sometimes the user may type ‘lenovo’ in lowercase or ‘LENOVO’ in upper case.
Even then it should display all the models of Lenovo laptops. That means we
should perform a case-insensitive check.

Case-insensitive means the string which you are comparing should exactly be
the same as a string which is to be compared but both strings can be either in
upper case or lower case. (ie., different cases)

 **Example 1: Conversion to lower case for comparison**

In this example, the user string and each list item are converted into
lowercase and then the comparison is made.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# conversion to lowercase for search

 

#function to search item

def check_Laptops():

 

 laptops = ['Msi', 'Lenovo', 'Hp', 'Dell']

 

 your_laptop = 'lenovo'

 

 # 'lenovo' is in lower case but it is present in the list of laptops.

 

 for lapy in laptops:

 

 #convert to lowercase and compare

 if your_laptop.lower() == lapy.lower():

 

 return True

 

 else:

 

 return False

 

# If the function returns true 

if check_Laptops():

 

 print('Laptop is present')

 

 

# If function returns false

else:

 

 print('Laptop is not present')  
  
---  
  
 __

 __

 **Output**

  

  

    
    
    Laptop is present
    
    

