NLP | Chunking Rules



Below are the steps involed for Chunking –

  * Conversion of sentence to a flat tree.  
![](https://media.geeksforgeeks.org/wp-content/uploads/chunk-rule-1.jpg)

  * Creation of Chunk string using this tree.
  * Creation of RegexpChunkParser by parsing the grammer using RegexpParser.
  * Appying the created chunk rule to the ChunkString that matches the sentence into a chunk.  
![](https://media.geeksforgeeks.org/wp-content/uploads/chunk-rule-2.jpg)

  * Splitting the bigger chunk to a smaller chunk using the defined chunk rules.  
![](https://media.geeksforgeeks.org/wp-content/uploads/chunk-rule-3.jpg)

  * ChunkString is then converted back to tree, with two chunk subtrees.  
![](https://media.geeksforgeeks.org/wp-content/uploads/chunk-rule-4.jpg)

 **Code #1 : ChunkString getting modified by applying each rule.**

 __

 __  
 __

 __

 __  
 __  
 __

# Loading Libraries

from nltk.chunk.regexp import ChunkString, ChunkRule, ChinkRule

from nltk.tree import Tree

 

# ChunkString() starts with the flat tree

tree = Tree('S', [('the', 'DT'), ('book', 'NN'),

 ('has', 'VBZ'), ('many', 'JJ'), ('chapters',
'NNS')])

 

# Initializing ChunkString()

chunk_string = ChunkString(tree)

print ("Chunk String : ", chunk_string)

 

# Initializing ChunkRule

chunk_rule = ChunkRule('<DT><NN.*><.*>*<NN.*>', 'chunk determiners
and nouns')

chunk_rule.apply(chunk_string)

print ("\nApplied ChunkRule : ", chunk_string)

 

# Another ChinkRule

ir = ChinkRule('<VB.*>', 'chink verbs')

ir.apply(chunk_string)

print ("\nApplied ChinkRule : ", chunk_string, "\n")

 

# Back to chunk sub-tree

chunk_string.to_chunkstruct()  
  
---  
  
 __

 __

 **Output:**

    
    
    Chunk String :   <<DT>  <NN>  <VBZ>  <JJ>  <NNS> 
    
    Applied ChunkRule :  {<DT>  <NN>  <VBZ>  <JJ>  <NNS>}
    
    Applied ChinkRule :  {<DT>  <NN>} <VBZ> {<JJ>  <NNS>} 
    
    Tree('S', [Tree('CHUNK', [('the', 'DT'), ('book', 'NN')]), 
        ('has', 'VBZ'), Tree('CHUNK', [('many', 'JJ'), ('chapters', 'NNS')])])
    

**Note :** This code works exactly in the same manner as explained in the
ChunkRule steps above.  
  
**Code #2 : How to this task directly with RegexpChunkParser.**

 __

 __  
 __

 __

 __  
 __  
 __

# Loading Libraries

from nltk.chunk.regexp import ChunkString, ChunkRule, ChinkRule

from nltk.tree import Tree

from nltk.chunk import RegexpChunkParser

 

# ChunkString() starts with the flat tree

tree = Tree('S', [('the', 'DT'), ('book', 'NN'),

 ('has', 'VBZ'), ('many', 'JJ'), ('chapters',
'NNS')])

 

# Initializing ChunkRule

chunk_rule = ChunkRule('<DT><NN.*><.*>*<NN.*>', 'chunk determiners
and nouns')

 

 

# Another ChinkRule

chink_rule = ChinkRule('<VB.*>', 'chink verbs')

 

# Applying RegexpChunkParser

chunker = RegexpChunkParser([chunk_rule, chink_rule])

chunker.parse(tree)  
  
---  
  
 __

 __

 **Output:**

  

  

    
    
    Tree('S', [Tree('CHUNK', [('the', 'DT'), ('book', 'NN')]), 
        ('has', 'VBZ'), Tree('CHUNK', [('many', 'JJ'), ('chapters', 'NNS')])])
    

  
**Code #3 : Parsing with different ChunkType.**

 __

 __  
 __

 __

 __  
 __  
 __

# Loading Libraries

from nltk.chunk.regexp import ChunkString, ChunkRule, ChinkRule

from nltk.tree import Tree

from nltk.chunk import RegexpChunkParser

 

# ChunkString() starts with the flat tree

tree = Tree('S', [('the', 'DT'), ('book', 'NN'),

 ('has', 'VBZ'), ('many', 'JJ'), ('chapters',
'NNS')])

 

# Initializing ChunkRule

chunk_rule = ChunkRule('<DT><NN.*><.*>*<NN.*>', 'chunk determiners
and nouns')

 

 

# Another ChinkRule

chink_rule = ChinkRule('<VB.*>', 'chink verbs')

 

# Applying RegexpChunkParser

chunker = RegexpChunkParser([chunk_rule, chink_rule], chunk_label
='CP')

chunker.parse(tree)  
  
---  
  
 __

 __

 **Output:**

    
    
    Tree('S', [Tree('CP', [('the', 'DT'), ('book', 'NN')]), ('has', 'VBZ'), 
              Tree('CP', [('many', 'JJ'), ('chapters', 'NNS')])])
    

![machine-learning](https://media.geeksforgeeks.org/wp-content/cdn-
uploads/20210107141454/ML-Live-Article-Bottom-min.png)

My Personal Notes _arrow_drop_up_

Save

