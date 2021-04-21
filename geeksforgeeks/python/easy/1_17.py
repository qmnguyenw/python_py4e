Extract feed details from RSS in Python



In the article, we will be seeing how to extract feed and post details using
RSS feed for a Hashnode blog. Although we are going to use it for blogs on
Hashnode it can be used for other feeds as well.

RSS means Rich Site Summary and uses standard web formats to publish
information that changes frequently like blog posts, news, audio, video, etc.
RSS documents often know as feed which consists of text, and metadata, like
time and author’s name.

 **Installing feed parser:**

We will be using the Feedparser python library for parsing the RSS feed of the
blog. It is quite a popular library for parsing blog feeds.

    
    
    pip install feedparser

 **Let’s understand this stepwise:**

  

  

 **Step 1:** Getting RSS feed

Use the feedparser.parse() function for creating a feed object which contains
parsed blog. It takes the URL of the blog feed.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# url of blog feed

feed_url = "https://vaibhavkumar.hashnode.dev/rss.xml"

 

blog_feed = feedparser.parse(feed_url)  
  
---  
  
 __

 __

 **Step 2:** Getting details from the blog.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# returns title of the blog site

blog_feed.feed.title 

 

# returns the link of the blog

# and number of entries(blogs) in the site.

blog_feed.feed.link

len(blog_feed.entries)

 

# Details of individual blog can

# be accessed by using attribute name

print(blog_feed.entries[0].title)

print(blog_feed.entries[0].link)

print(blog_feed.entries[0].author)

print(blog_feed.entries[0].published)

 

# Getting lists of tags and authors.

tags = [tag.term for tag in blog_feed.entries[0].tags]

authors= [author.name for author in
blog_feed.entries[0].authors]  
  
---  
  
 __

 __

 **Below is the full implementation:** Now use the above code to write a
function that takes the link of RSS feed and returns the details.

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

def get_posts_details(rss=None):

 

 """

 Take link of rss feed as argument

 """

 if rss is not None:

 

 # import the library only when url for feed is passed

 import feedparser

 

 # parsing blog feed

 blog_feed = blog_feed = feedparser.parse(rss)

 

 # getting lists of blog entries via .entries

 posts = blog_feed.entries

 

 # dictionary for holding posts details

 posts_details = {"Blog title" : blog_feed.feed.title,

 "Blog link" : blog_feed.feed.link}

 

 post_list = []

 

 # iterating over individual posts

 for post in posts:

 temp = dict()

 

 # if any post doesn't have information then throw error.

 try:

 temp["title"] = post.title

 temp["link"] = post.link

 temp["author"] = post.author

 temp["time_published"] = post.published

 temp["tags"] = [tag.term for tag in post.tags]

 temp["authors"] = [author.name for author in
post.authors]

 temp["summary"] = post.summary

 except:

 pass

 

 post_list.append(temp)

 

 # storing lists of posts in the dictionary

 posts_details["posts"] = post_list 

 

 return posts_details # returning the details which is dictionary

 else:

 return None

 

if __name__ == "__main__":

 import json

 

 feed_url = "https://vaibhavkumar.hashnode.dev/rss.xml"

 

 data = get_posts_details(rss = feed_url) # return blogs data as
a dictionary

 

 if data:

 # printing as a json string with indentation level = 2

 print(json.dumps(data, indent=2)) 

 else:

 print("None")  
  
---  
  
 __

 __

 **Output:**

![](https://media.geeksforgeeks.org/wp-
content/uploads/20210120222207/Capture-660x280.JPG)  

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

