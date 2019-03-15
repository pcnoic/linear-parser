##########stoicParser######################
#@author: Christos Alexiou: da18032        #
#@package-name: stoicParser                #
#@desc: parser for general linear problem  #
#@version: 1.0.0                           #
############################################

import re


#read file functions

def problemType(f):
    file = open(f, "r")
    #return 1 if it's maximization or -1 for minification
    if file.read(3) == "max":
        return 1
    else:
        return -1

def readLine(f,n):
    file = open(f, "r")
    #function used inline so return what's needed
    return file.readline(n) 


#properly formatting the file
def correctSpaces(string):
    #let's do some counting with regex
    tokens = re.findall('\s+', s)

    for i in range(0, len(tokens)):
        return len(tokens[i]) 





    
