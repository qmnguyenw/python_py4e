Create Find and Replace features in Tkinter Text Widget



 **Prerequisistes:** Python GUI – tkinter

Firstly we need to find all the words or letters that we want to replace in
our below text for that we will use the find function in which we will
determine all the starting and the ending indexes from the editor of the same
word after that we will apply the replace functionality in which we will
delete that part of the text and after that, we will apply insert function to
add the text at that exact positions.

 **Important inbuilt functions used**  

  *  **Tk()** it creates a base window/tkinter base widget
  *  **Frame()** it creates a a separate Frame at a particular position on the Tk() instance
  *  **Label()** it adds the statement or the name or labeling of anything
  *  **Entry()** it adds the dialog box to enter the text
  *  **‘EntryInstance’ .pack()** it packs the entry box at the specified position
  *  **Button()** it places a button at the specifed position with the command and the label
  *  **Text()** it places a text Box to write ans add content
  *  **‘TextInstance’ .insert()** it adds text at the specified index(over here index is of string type)
  *  **‘TextInstance’ .tag_add()** Tags are used to refer to all the contents at the same time, for eg if a paragraph contains text “this” five times and in order to make a change to them at all at same time we use tags. tag_Add adds all those text under a particular tag where name is provided by us
  *  **‘TextInstance’ .tag_config()** they are used to configure them that is highlight, font, background color, foreground color
  *  **‘TextInstance’ .tag_remove()** used to remove all the text used from starting index to ending index
  *  **‘EntryInstance’ .get()** used to have access to the text entered inside the dialog box of Entry
  *  **‘TextInstance’ .search()** used to search a particular text in the whole editor from starting index till end with an argument of ‘nocase’ which if set 1 implies no case sensitivity will be considered in search
  *  **‘ButtonInstance’ .config()** used to confiure the button that is we can separately add the command or the changes in the button that will take place when it will be pressed
  *  **‘TkInstance’ .mainloop()** used to make sure that the text widget remain open

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

from tkinter import *

 

 

# to create a window 

root = Tk() 

 

# root window is the parent window 

fram = Frame(root) 

 

# Creating Label, Entry Box, Button 

# and packing them adding label to

# search box 

Label(fram, text ='Find').pack(side = LEFT)

 

# adding of single line text box 

edit = Entry(fram) 

 

# positioning of text box 

edit.pack(side = LEFT, fill = BOTH, expand = 1) 

 

# setting focus 

edit.focus_set() 

 

# adding of search button 

Find = Button(fram, text ='Find')

Find.pack(side = LEFT)

 

 

Label(fram, text = "Replace With ").pack(side = LEFT)

 

edit2 = Entry(fram)

edit2.pack(side = LEFT, fill = BOTH, expand = 1)

edit2.focus_set()

 

replace = Button(fram, text = 'FindNReplace')

replace.pack(side = LEFT)

 

fram.pack(side = TOP) 

 

# text box in root window 

text = Text(root) 

 

# text input area at index 1 in text window 

text.insert('1.0', '''Type your text here''') 

text.pack(side = BOTTOM) 

 

# function to search string in text 

def find(): 

 

 # remove tag 'found' from index 1 to END 

 text.tag_remove('found', '1.0', END) 

 

 # returns to widget currently in focus 

 s = edit.get()

 

 if (s): 

 idx = '1.0'

 while 1: 

 # searches for desried string from index 1 

 idx = text.search(s, idx, nocase = 1, 

 stopindex = END)

 

 if not idx: break

 

 # last index sum of current index and 

 # length of text 

 lastidx = '% s+% dc' % (idx, len(s))

 

 

 # overwrite 'Found' at idx 

 text.tag_add('found', idx, lastidx) 

 idx = lastidx 

 

 # mark located string as red

 

 text.tag_config('found', foreground ='red')

 edit.focus_set()

 

def findNreplace(): 

 

 # remove tag 'found' from index 1 to END 

 text.tag_remove('found', '1.0', END) 

 

 # returns to widget currently in focus 

 s = edit.get()

 r = edit2.get()

 

 if (s and r): 

 idx = '1.0'

 while 1: 

 # searches for desried string from index 1 

 idx = text.search(s, idx, nocase = 1, 

 stopindex = END)

 print(idx)

 if not idx: break

 

 # last index sum of current index and 

 # length of text 

 lastidx = '% s+% dc' % (idx, len(s))

 

 text.delete(idx, lastidx)

 text.insert(idx, r)

 

 lastidx = '% s+% dc' % (idx, len(r))

 

 # overwrite 'Found' at idx 

 text.tag_add('found', idx, lastidx) 

 idx = lastidx 

 

 # mark located string as red

 text.tag_config('found', foreground ='green', background =
'yellow')

 edit.focus_set()

 

 

Find.config(command = find)

replace.config(command = findNreplace)

 

# mainloop function calls the endless 

# loop of the window, so the window will

# wait for any user interaction till we

# close it 

root.mainloop()  
  
---  
  
 __

 __

 **Output:**

https://media.geeksforgeeks.org/wp-content/uploads/20200527182326/tkinter-
find-and-replace.webm

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

  
  

  

My Personal Notes _arrow_drop_up_

Save

