# Bragi
A text parsing/highlighting tool - might be handy.  

Also, remember to test with:  
$ pytest -n 3 conftest.py test

## Introdution  
Overall, what I want is to be able to feed a spec guide to a pdf convertor, run it through
a tool, generate an html file filled with links, goodies, highlighting, backlinks, word cloud,
and possibly paragraph by paragraph sentiment analysis.  

## Steps  
1. prototype word cloud  
2. prototype acronym work  
3. prototype html generation (probably straight forward)  
4. look into local sentiment analysis  
5. look into highlighting  
6. auto linking/backlinks  

### prototype word cloud  
Word clouds are handy for giving the user a visual snapshot of what could be 
interesting.  The colours, sizes of the text and even the orientation can 
be quite lovely and help reinforce concepts.

### prototype acronym work  
Find ([A-Z]*) patterns and then try to map them back len(pattern) back with 
upper case characters.  For example: This is the Session Initiation Protocol
(SIP).  What it should map to:  

SIP - Session Initiation Protocol  

### prototype html generation  
Generate a text to html output - that should be straight-forward.  Perhaps
highlight identified ACRONYMS.

TITLE  
Paragraph body1  

Paragraph body2  

...

Closing  
