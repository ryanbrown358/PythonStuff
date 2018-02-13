"""
Importing keyword and sys,

The keyword module contains a list of all python reserved keywords.  The sus module allows you to explore many 
features including the interactive mode help system. 

"""

import sys
import keyword
print("Python version: ", sys.version)

print("Interpreter Location:", sys.executable)

print("Keywords: ")
for word in keyword.kwlist:
    print(word)

#you can use the iskeyword to check to see if the word you are going to use is a reserved keyword or not
print(keyword.iskeyword('def'))
