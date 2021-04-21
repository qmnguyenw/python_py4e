twitter-text-python (ttp) module – Python



 **twitter-text-python** is a Tweet parser and formatter for Python. Amongst
many things, the tasks that can be performed by this module are :

  *  **reply :** The username of the handle to which the tweet is bieng replied to.
  *  **users :** All the usernames mentioned in the tweet.
  *  **tags :** All the hashtags mentioned in the tweet.
  *  **urls :** All the URLs mentioned in the tweet.
  *  **html :** Adds hyperlinks to the fields mentioned above.

 **Example 1 :**

 __

 __  
 __

 __

 __  
 __  
 __

# import the twitter-text-python module

from ttp import ttp

 

# the text to be parsed

tweet_text = ("@twitter Sample tweet containing different components."
+

 "# gfg # tweeple Visit : https://twitter.com @TwitterIndia")

 

# instantiating the Parser

p = ttp.Parser()

 

# parsing the text

result = p.parse(tweet_text)

 

# printing the username of the

# account being replied to

print("The username being replied to is : " + result.reply)

 

# printing all the usernames

# mentioned in the tweet

print("\nAll the usernames mentioned are : " + str(result.users))

 

# printing all the hashtags

# mentioned in the tweet

print("\nAll the hashtags mentioned are : " + str(result.tags))

 

# printing all the URLs

# mentioned in the tweet

print("\nAll the URLs mentioned are : " + str(result.urls))

 

# adding hyperlinks to usernames,

# hashtags and URLs

print(result.html)  
  
---  
  
 __

 __

 **Output :**

> The username being replied to is : twitter
>
> All the usernames mentioned are : [‘twitter’, ‘TwitterIndia’]
>
>  
>
>
>  
>
>
> All the hashtags mentioned are : [‘gfg’, ‘tweeple’]
>
> All the URLs mentioned are : [‘https://twitter.com’]
>
> @twitter Sample tweet containing different components.#gfg #tweeple Visit :
> https://twitter.com @TwitterIndia

 **Example 2 :** We can also find the position of string (POS) by doing
include_spans = True.

 __

 __  
 __

 __

 __  
 __  
 __

# import the twitter-text-python module

from ttp import ttp

 

# the text to be parsed

tweet_text = ("@twitter Sample tweet containing different components."
+

 "# gfg # tweeple Visit : https://twitter.com @TwitterIndia")

 

# instantiating the Parser

# with spans

p = ttp.Parser(include_spans = True)

 

# parsing the text

result = p.parse(tweet_text)

 

# printing all the usernames

# mentioned in the tweet with POS

print("All the usernames mentioned are : " + str(result.users))

 

# printing all the hashtags

# mentioned in the tweet with POS

print("\nAll the hashtags mentioned are : " + str(result.tags))

 

# printing all the URLs

# mentioned in the tweet with POS

print("\nAll the URLs mentioned are : " + str(result.urls))  
  
---  
  
 __

 __

 **Output :**

> All the usernames mentioned are : [(‘twitter’, (0, 8)), (‘TwitterIndia’,
> (130, 143))]
>
> All the hashtags mentioned are : [(‘gfg’, (96, 100)), (‘tweeple’, (101,
> 109))]
>
> All the URLs mentioned are : [(‘https://twitter.com’, (76, 95))]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

