Python | Program to implement simple FLAMES game



Python is a multipurpose language and one can do literally anything with it.
Python can also be used for game development. Let’s create a simple FLAMES
game without using any external game libraries like PyGame.

 **FLAMES** is a popular game named after the acronym: Friends, Lovers,
Affectionate, Marriage, Enemies, Sibling. This game does not accurately
predict whether or not an individual is right for you, but it can be fun to
play this with your friends.

There are two steps in this game:

 **Get the count :**

    * Take the two names.
    * Remove the common characters with their respective common occurrences.
    * Get the count of the characters that are left .

 **Get the result :**

  

  

    * Take FLAMES letters as [“F”, “L”, “A”, “M”, “E”, “S”]
    * Start removing letter using the count we got.
    * The letter which last the process is the result.

 **Example :**

    
    
    Input :   player1 name : AJAY
              player 2 name : PRIYA
    
    Output : Relationship status : Friends

 **Explanation:** In above given two names A and Y are common letters which
are occurring one time(common count) in both names so we are removing these
letters from both names. Now count the total letters that are left here it is
5. Now start removing letters one by one from FLAMES using the count we got
and the letter which lasts the process is the result.

Counting is done in anti-clockwise circular fashion.

> FLAMES  
> counting is start from F, E is at 5th count so we remove E and start
> counting again but a this time start from S.  
> FLAMS  
> M is at 5th count so we remove M and counting start from S.  
> FLAS  
> S is at 5th count so we remove S and counting start from F.  
> FLA  
> L is at 5th count so we remove L and counting start from A.  
> FA  
> A is at 5th count so we remove A. now we have only one letter is remaining
> so this is the final answer.  
> F  
> So, the relationship is F i.e. Friends .

 **Approach:** Take two names as input then remove the common characters with
their respective common occurrences. For removing purpose we create user-
defined remove_match_char function with two arguments as list1 and list2
which stores list of characters of two players name respectively and return
list of concatenated list(list1 + “*” flagst2) and flag value which we store
in ret_list variable.After removing all the common characters, count the total
no. of remaining characters then create a result list with FLAMES acronym i.e
[“Friends”, “Love”, “Affection”, “Marriage”, “Enemy”, “Siblings”]. Now start
removing word one by one untill list not contains only one word, using the
total count which we got. the word which remains in the last, is the result.

Below is the implementation :

 __

 __  
 __

 __

 __  
 __  
 __

# function for removing common characters

# with their respective occurrences

def remove_match_char(list1, list2):

 

 for i in range(len(list1)) :

 for j in range(len(list2)) :

 

 # if common character is found

 # then remove that character

 # and return list of concatenated

 # list with Ture Flag

 if list1[i] == list2[j] :

 c = list1[i]

 

 # remove character from the list

 list1.remove(c)

 list2.remove(c)

 

 # concatenation of two list elements with *

 # * is act as border mark here

 list3 = list1 + ["*"] + list2

 

 # return the concatenated list with True flag

 return [list3, True]

 

 # no common characters is found

 # return the concatenated list with False flag

 list3 = list1 + ["*"] + list2

 return [list3, False]

 

# Driver code

if __name__ == "__main__" :

 

 # take first name 

 p1 = input("Player 1 name : ")

 

 # converted all letters into lower case

 p1 = p1.lower()

 

 # replace any space with empty string

 p1.replace(" ", "")

 

 # make a list of letters or characters

 p1_list = list(p1)

 

 # take 2nd name

 p2 = input("Player 2 name : ")

 p2 = p2.lower()

 p2.replace(" ", "")

 p2_list = list(p2)

 

 # taking a flag as True initially

 proceed = True

 

 # keep calling remove_match_char function

 # untill common characters is found or

 # keep looping untill proceed flag is True

 while proceed :

 

 # function calling and store return value 

 ret_list = remove_match_char(p1_list, p2_list)

 

 # take out concatenated list from return list

 con_list = ret_list[0]

 

 # take out flag value from return list

 proceed = ret_list[1]

 

 # find the index of "*" / border mark

 star_index = con_list.index("*")

 

 # list slicing perform

 

 # all characters before * store in p1_list

 p1_list = con_list[ : star_index]

 

 # all characters after * store in p2_list

 p2_list = con_list[star_index + 1 : ]

 

 

 # count total remaining characters

 count = len(p1_list) + len(p2_list)

 

 # list of FLAMES acronym

 result = ["Friends", "Love", "Affection", "Marriage",
"Enemy", "Siblings"]

 

 # keep looping untill only one item

 # is not remaining in the result list

 while len(result) > 1 :

 

 # store that index value from

 # where we have to perform slicing.

 split_index = (count % len(result) - 1)

 

 # this steps is done for performing

 # anticlock-wise circular fashion counting.

 if split_index >= 0 :

 

 # list slicing

 right = result[split_index + 1 : ]

 left = result[ : split_index]

 

 # list concatenation

 result = right + left

 

 else :

 result = result[ : len(result) - 1]

 

 # print final result

 print("Relationship status :", result[0])  
  
---  
  
 __

 __

 **Output:**

    
    
    Player 1 name : ANKIT
    Player 2 name : DEEPIKA
    Relationship status : Marriage
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

