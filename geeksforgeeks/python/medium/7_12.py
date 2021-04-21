How to Create a Programming Language using Python?



In this article, we are going to learn how to create your own programming
language using SLY(Sly Lex Yacc) and Python. Before we dig deeper into this
topic, it is to be noted that this is not a beginner’s tutorial and you need
to have some knowledge of the prerequisites given below.

#### Prerequisites

  * Rough knowledge about compiler design.
  * Basic understanding of lexical analysis, parsing and other compiler design aspects.
  * Understanding of regular expressions.
  * Familiarity with Python programming language.

## Getting Started

Install SLY for Python. SLY is a lexing and parsing tool which makes our
process much easier.

    
    
    pip install sly
    

## Building a Lexer

The first phase of a compiler is to convert all the character streams(the high
level program that is written) to token streams. This is done by a process
called lexical analysis. However, this process is simplified by using SLY

First let’s import all the necessary modules.

## Python3

  

  

 __

 __  
 __

 __

 __  
 __  
 __

from sly import Lexer  
  
---  
  
 __

 __

