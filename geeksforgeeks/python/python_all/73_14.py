Python | PRAW – Python Reddit API Wrapper



 **PRAW** (Python Reddit API Wrapper) is a Python module that provides a
simple access to Reddit’s API. PRAW is easy to use and follows all of Reddit’s
API rules.

The documentation regarding PRAW is located here.

 **Prerequisites** :

  * Basic Python Programming Skills
  * Basic Reddit Knowledge : Reddit is a network of communities based on people’s interests. Each of these communities is called a subreddit. Users can subscribe to multiple subreddits to post, comment and interact with them.
  * A Reddit Account

To install PRAW, we run the following pip script on the terminal / command
prompt.

    
    
    pip install praw

After installing PRAW, we need to import it:

  

  

 __

 __  
 __

 __

 __  
 __  
 __

import praw  
  
---  
  
 __

 __

After importing PRAW, we need to instantiate it. There are 2 types of PRAW
instances:

  *  **Read-only Instance:** With read-only instance we can only retrieve public information from Reddit. Information like top 10 posts from a certain subreddit. We can’t post material from this.
  *  **Authorized Instance:** With authorised instance we can do whatever a normal reddit account can do. Actions like comment, post, repost, upvote etc. can be performed.

 **Creating a read-only instance:**

 __

 __  
 __

 __

 __  
 __  
 __

reddit= praw.Reddit(client_id ='my client id',

 client_secret ='my client secret',

 user_agent ='my user agent')

 

# to verify whether the instance is read-only instance or not

print(reddit.read_only)  
  
---  
  
 __

 __

Output:

    
    
    True

 **Creating an authorized instance:**

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

 

# to verify whether the instance is authorised instance or not

print(reddit.read_only)  
  
---  
  
 __

 __

Output:

    
    
    False

To switch back to read-only mode:

 __

 __  
 __

 __

 __  
 __  
 __

reddit.read_only= True  
  
---  
  
 __

 __

Now let us see some of the operations we can acheive using PRAW:

  *  **Access a Subreddit:** In reddit there are multiple communities known as subreddits. We can obtain a subreddit instance using the method subreddit.

 __

 __  
 __

 __

 __  
 __  
 __

subreddit= reddit.subreddit('GRE')

 

# display the subreddit name

print(subreddit.display_name)

 

# display the subreddit title 

print(subreddit.title) 

 

# display the subreddit description 

print(subreddit.description)  
  
---  
  
 __

 __

Output :

    
        GRE
    GRE
    #/r/GRE  
    
    This subreddit is for discussion of the GRE (Graduate Record Examination). If you're studying for the GRE, or can help people who are studying for the GRE, you're in the right place!
    
      
    
    -----
    
    #Rules
    
    - You must read and follow the rules! 
    https://www.reddit.com/r/gre/about/rules
    
    -----

  *  **Access a Submission:** Within a subreddit there are multiple post submissions. We can iterate through the submissions in the submission instance. Reddit provides us multiple ways to sort submissions:
    * rising
    * new
    * hot
    * gilded
    * controversial
    * top

These methods will return a ListingGenerator, therefore we will need to
iterate through it.

 __

 __  
 __

 __

 __  
 __  
 __

# to find the top most submission in the subreddit "GRE"

subreddit = reddit.subreddit('GRE')

 

for submission in subreddit.top(limit = 1):

 # displays the submission title

 print(submission.title) 

 

 # displays the net upvotes of the submission

 print(submission.score) 

 

 # displays the submission's ID

 print(submission.id) 

 

 # displays the url of the submission

 print(submission.url)   
  
---  
  
__

__

Output:

    
        me irl
    483
    de58vq
    https://i.redd.it/0mqck4323yq31.png

  *  **Access a Redditor:** In Reddit, the user is called a Redditor. We can obtain the redditor instance using the method redditor. In the method we pass the username of the redditor.

 __

 __  
 __

 __

 __  
 __  
 __

# let the redditor be "AutoModerator"

redditor = reddit.redditor('AutoModerator')

 

# display AutoModerator's karma

print(redditor.link_karma)   
  
---  
  
__

__

Output:

    
        6554

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

