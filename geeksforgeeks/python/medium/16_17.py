Python | Fetch your gmail emails from a particular user



If you are ever curious to know how we can fetch Gmail e-mails using Python
then this article is for you.

As we know Python is a multi-utility language which can be used to do a wide
range of tasks. Fetching Gmail emails though is a tedious task but with
Python, many things can be done if you are well versed with its usage. Gmail
provides IMAP access to clients who want to access Gmail without manually
logging in the browser.

 **In setting page, enable this before running script.**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190524174934/gmail_python.png)  

 **Implementation:**  
The libraries used in this implementation includes **imaplib** , **email**.
You have to manually go and make IMAP access enabled by going into your Gmail
account settings. After this only you could access your Gmail account without
logging in browser.

  * Three functions are defined in the implementation which is used to get email body, search for emails from a particular user and get all emails under a label.
  * For showing results I have sent email to my id from my another Gmail account. Now I will be fetching emails from my Gmail account which is received from my another Gmail account.
  * The process begins from making Gmail connection with the help of _imaplib library_ and proving our Gmail login credentials to it.
  * After logging we are selecting emails under the label: Inbox which is a default labeled section for all users. However, you can create your own labels also.
  * Then we are calling get emails function and provide it the parameter from search function result i.e “from user”
  * In get emails function we are putting all emails in an array named “msgs”
  * Now print to see the msgs array
  * Now we can easily iterate over this array. We are iterating it in the order the emails arrived. Then we are searching for the index from where our content begins. This indexing part will be different for different emails/users and the user can manually change the indexes to print only that part which they require.
  * We have our results printed out.

Below is the Python implementation –

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Importing libraries

import imaplib, email

 

user = 'USER_EMAIL_ADDRESS'

password = 'USER_PASSWORD'

imap_url = 'imap.gmail.com'

 

# Function to get email content part i.e its body part

def get_body(msg):

 if msg.is_multipart():

 return get_body(msg.get_payload(0))

 else:

 return msg.get_payload(None, True)

 

# Function to search for a key value pair 

def search(key, value, con): 

 result, data = con.search(None, key,
'"{}"'.format(value))

 return data

 

# Function to get the list of emails under this label

def get_emails(result_bytes):

 msgs = [] # all the email data are pushed inside an array

 for num in result_bytes[0].split():

 typ, data = con.fetch(num, '(RFC822)')

 msgs.append(data)

 

 return msgs

 

# this is done to make SSL connnection with GMAIL

con = imaplib.IMAP4_SSL(imap_url) 

 

# logging the user in

con.login(user, password) 

 

# calling function to check for email under this label

con.select('Inbox') 

 

 # fetching emails from this user "tu**h*****1@gmail.com"

msgs = get_emails(search('FROM', 'MY_ANOTHER_GMAIL_ADDRESS',
con))

 

# Uncomment this to see what actually comes as data 

# print(msgs) 

 

 

# Finding the required content from our msgs

# User can make custom changes in this part to

# fetch the required content he / she needs

 

# printing them by the order they are displayed in your gmail 

for msg in msgs[::-1]: 

 for sent in msg:

 if type(sent) is tuple: 

 

 # encoding set as utf-8

 content = str(sent[1], 'utf-8') 

 data = str(content)

 

 # Handling errors related to unicodenecode

 try: 

 indexstart = data.find("ltr")

 data2 = data[indexstart + 5: len(data)]

 indexend = data2.find("</div>")

 

 # printtng the required content which we need

 # to extract from our email i.e our body

 print(data2[0: indexend])

 

 except UnicodeEncodeError as e:

 pass  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20190524175434/gmail_python_2.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

