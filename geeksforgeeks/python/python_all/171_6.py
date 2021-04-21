Python program to print Emojis



There are multiple ways we can print the Emojis in Python. Let’s see how to
print Emojis with Uniocdes, CLDR names and emoji module.

 **Using Unicodes:**  
Every emoji has a Unicode associated with it. Emojis also have a CLDR short
name, which can also be used.

From the list of unicodes, replace “+” with “000”. For example – “U+1F600”
will become “U0001F600” and prefix the unicode with “\” and print it.

 __

 __  
 __

 __

 __  
 __  
 __

# grinning face

print("\U0001f600")

 

# grinning squinting face

print("\U0001F606")

 

# rolling on the floor laughing

print("\U0001F923")  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/emoji.png)  
  
**Using CLDR short name:**

 __

 __  
 __

 __

 __  
 __  
 __

# grinning face

print("\N{grinning face}")

 

# slightly smiling face

print("\N{slightly smiling face}")

 

# winking face

print("\N{winking face}")  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/emoji2.png)

  

  

  
**Using emoji module:**

Emojis can also be implemented by using the emoji module provided in Python.
To install it run the following in the terminal.

    
    
    pip install emoji

emojize() function requires the CLDR short name to be passed in it as the
parameter. It then returns the corresponding emoji. Replace the spaces with
underscore in the CLDR short name.

 __

 __  
 __

 __

 __  
 __  
 __

# import emoji module

import emoji

 

 

print(emoji.emojize(":grinning_face_with_big_eyes:"))

print(emoji.emojize(":winking_face_with_tongue:"))

print(emoji.emojize(":zipper-mouth_face:"))  
  
---  
  
 __

 __

 **Output:**  
![](https://media.geeksforgeeks.org/wp-content/uploads/emoji3.png)  
  
demojize() function converts the emoji passed into its corresponding CLDR
short name.  
![](https://media.geeksforgeeks.org/wp-content/uploads/emoji4.png)

  
Below is a list of some common emoji Unicodes with their CLDR short names:CLDR
Short Name| Unicode| grinning face| U+1F600| grinning face with big eyes|
U+1F603| grinning face with smiling eyes| U+1F604| beaming face with smiling
eyes| U+1F601| grinning squinting face| U+1F606| grinning face with sweat|
U+1F605| rolling on the floor laughing| U+1F923| face with tears of joy|
U+1F602| slightly smiling face| U+1F642| upside-down face| U+1F643| winking
face| U+1F609| smiling face with smiling eyes| U+1F60A| smiling face with
halo| U+1F607| smiling face with 3 hearts| U+1F970| smiling face with heart-
eyes| U+1F60D| star-struck| U+1F929| face blowing a kiss| U+1F618| kissing
face| U+1F617| smiling face| U+263A| kissing face with closed eyes| U+1F61A|
kissing face with smiling eyes| U+1F619| face savoring food| U+1F60B| face
with tongue| U+1F61B| winking face with tongue| U+1F61C| zany face| U+1F92A|
squinting face with tongue| U+1F61D| money-mouth face| U+1F911| hugging face|
U+1F917| face with hand over mouth| U+1F92D| shushing face| U+1F92B| thinking
face| U+1F914| zipper-mouth face| U+1F910| face with raised eyebrow| U+1F928|
neutral face| U+1F610| expressionless face| U+1F611| face without mouth|
U+1F636| smirking face| U+1F60F| unamused face| U+1F612| face with rolling
eyes| U+1F644| grimacing face| U+1F62C| lying face| U+1F925| relieved face|
U+1F60C| pensive face| U+1F614| sleepy face| U+1F62A| drooling face| U+1F924|
sleeping face| U+1F634| face with medical mask| U+1F637| face with
thermometer| U+1F912| face with head-bandage| U+1F915| nauseated face| U+1F922  
---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

