Newspaper: Article scraping & curation (Python)



Newspaper is a Python module used for extracting and parsing newspaper
articles. Newspaper use advance algorithms with web scrapping to extract all
the useful text from a website. It works amazingly well on online newspapers
websites. Since it use web scrapping too many request to a newspaper website
may lead to blocking, so use it accordingly.

Installation:

    
    
    pip install newspaper3k

Newspaper supports following languages:

    
    
      **input code**         **full name**
      ar               Arabic
      da               Danish
      de               German
      el               Greek
      en               English
      it               Italian
      zh               Chinese
    ......... and many more
    

Some Useful functions

To create an instance of article

  

  

    
    
    article_name = Article(url, language="language code according to newspaper")
    

To download an article

    
    
    article_name.download()
    

To parse an article

    
    
    article_name.parse()
    

To apply nlp(natural language procesing) on article

    
    
    article_name.nlp()
    

To extract article’s text

    
    
    article_name.text
    

To extract article’s title

    
    
    article_name.title
    

To extract article’s summary

    
    
    article_name.summary
    

To extract article’s keywords

    
    
    article_name.keywords
    

__

__  
__

__

__  
__  
__

from newspaper import Article

 

#A new article from TOI

url = "http:// timesofindia.indiatimes.com/world/china/chinese-expert-
warns-of-troops-entering-kashmir/articleshow/59516912.cms"

 

#For different language newspaper refer above table

toi_article = Article(url, language="en") # en for English

 

#To download the article

toi_article.download()

 

#To parse the article

toi_article.parse()

 

#To perform natural language processing ie..nlp

toi_article.nlp()

 

#To extract title

print("Article's Title:")

print(toi_article.title)

print("n")

 

#To extract text

print("Article's Text:")

print(toi_article.text)

print("n")

 

#To extract summary

print("Article's Summary:")

print(toi_article.summary)

print("n")

 

#To extract keywords

print("Article's Keywords:")

print(toi_article.keywords)  
  
---  
  
 __

 __

Output:

    
    
    Article's Title:
    India China News: Chinese expert warns of troops entering Kashmir
    
    
    Article's Text:
    BEIJING: A Chinese expert has argued that his country's troops would be entitled to enter the Indian side of Kashmir by extending the logic that has permitted Indian troops to enter an area which is disputed by China and Bhutan This is one of the several arguments made by the scholar in an attempt to blame India for. India has responded to efforts by China to build a road in the Doklam area, which falls next to the trijunction connecting Sikkim with Tibet and Bhutan and"Even if India were requested to defend Bhutan's territory, this could only be limited to its established territory, not the disputed area, " Long Xingchun, director of the Center for Indian Studies at China West Normal University said in an article. "Otherwise, under India's logic, if the Pakistani government requests, a third country's army can enter the area disputed by India and Pakistan, including India-controlled Kashmir".China is not just interfering, it is building roads and other infrastructure projects right inside Pakistan-Occupied Kashmir (PoK), which is claimed by both India and Pakistan. This is one of the facts that the article did not mention.The scholar, through his article in the Beijing-based Global Times, suggested that Beijing can internationalize the Doklam controversy without worrying about western countries supporting India because the West has a lot of business to do with China."China can show the region and the international community or even the UN Security Council its evidence to illustrate China's position, " Long said. At the same time, he complained that "Western governments and media kept silent, ignoring India's hegemony over the small countries of South Asia" when India imposed a blockade on the flow of goods to Nepal in 2015.Recent actions by US president Donald Trump, which include selling arms to Taiwan and pressuring China on the North Korean issue, shows that the West is not necessarily cowered down by China's business capabilities.He reiterated the government's stated line that Doklam belongs to China, and that Indian troops had entered the area under the guise of helping Bhutan protect its territory."For a long time, India has been talking about international equality and non-interference in the internal affairs of others, but it has pursued hegemonic diplomacy in South Asia, seriously violating the UN Charter and undermining the basic norms of international relations, " he said.Interestingly, Chinese scholars are worrying about India interfering in Bhutan's "sovereignty and national interests" even though it is Chinese troops who have entered the Doklam area claimed by it."Indians have migrated in large numbers to Nepal and Bhutan, interfering with Nepal's internal affairs. The first challenge for Nepal and Bhutan is to avoid becoming a state of India, like Sikkim, " he said.
    
    
    Article's Summary:
    sending its troops to the disputed Doklam area +puts Indian territory at risk +BEIJING: A Chinese expert has argued that his country's troops would be entitled to enter the Indian side of Kashmir by extending the logic that has permitted Indian troops to enter an area which is disputed by China and Bhutan This is one of the several arguments made by the scholar in an attempt to blame India for.
    "Otherwise, under India's logic, if the Pakistani government requests, a third country's army can enter the area disputed by India and Pakistan, including India-controlled Kashmir".China is not just interfering, it is building roads and other infrastructure projects right inside Pakistan-Occupied Kashmir (PoK), which is claimed by both India and Pakistan.
    "China can show the region and the international community or even the UN Security Council its evidence to illustrate China's position, " Long said.
    "Indians have migrated in large numbers to Nepal and Bhutan, interfering with Nepal's internal affairs.
    The first challenge for Nepal and Bhutan is to avoid becoming a state of India, like Sikkim, " he said.
    
    
    Article's Keywords:
    ['troops', 'india', 'china', 'territory', 'west', 'disputed', 'expert', 'indian', 'bhutan', 'kashmir', 'chinese', 'entering', 'doklam', 'area', 'warns']
    
    

Reference : Newspaper python package on github

This article is contributed by **Pratik Chhajer**. If you like GeeksforGeeks
and would like to contribute, you can also write an article using
contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

