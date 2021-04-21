How to get client_id and client_secret for Python Reddit API registration ?



Reddit is a network of communities based on people’s interests. Each of these
communities is called a subreddit. Users can subscribe to multiple subreddits
to post, comment and interact with them.  
A Reddit bot is something that automatically responds to a user’s post or
automatically posts things at certain intervals. This could depend on what
content the users post. It can be triggered by certain key phrases and also
depends on various subreddits regarding their content.  
In order to implement a Reddit bot, we will use the Python Reddit API Wrapper
(PRAW). It allows us to login to the Reddit API to directly interact with the
backend of the website. More information about this library can be found here
– PRAW – Python Reddit API Wrapper  
.

To create an instance of PRAW we need to run the following code:

 __

 __  
 __

 __

 __  
 __  
 __

reddit= praw.Reddit(client_id ='my client id', 

 client_secret ='my client secret', 

 user_agent ='my user agent', 

 username ='my username', 

 password ='my password')   
  
---  
  
__

__

In order to get the information for these fields:

  * Create a Reddit account.
  * The username of the reddit account will go to the username field.
  * The password of the reddit account will go to the password field.
  * user_agent is a unique identifier that helps Reddit determine the source of network requests.
  * client_id and client_secret are needed to access Reddit’s API as a script application. We can find them by:
    1. Login to your Reddit account.
    2. Open the link: https://www.reddit.com/prefs/apps
    3. The following will open up:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200511191452/Screenshot-2242.png)

    4. Click on “create an app…”. The following fields will be requested:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200511191754/Screenshot-2253.png)

    5. Give an appropriate name to the application and fill rest of the fields:  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200511191936/Screenshot-2262.png)

    6. Click on “create app”.
    7. The text in the green box is the client_id.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200511193013/Screenshot-2383.png)

    8. Click on “edit”. The text in the green box is the client_secret.  
![](https://media.geeksforgeeks.org/wp-
content/uploads/20200511193209/Screenshot-2394.png)

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

