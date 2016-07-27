#! /usr/bin/env python3
#regSearch.py - Opens all .txt files in a folder
# and uses reg exps to search searches for any line that matches input
# Prints lines with searched phrase to screen.

import os
import re

#Requires user to input text
#Takes text, compiles a regular expression for anything, stores search results in variable
searchFor = input("Enter what you would like to search for: ")
searchRegex = re.compile(r'.*')
mo = searchRegex.search(searchFor)
foundResults = mo.group()

#Get a list of strings of all filenames in the current directory
allFiles = os.listdir(os.getcwd()) #tested and works
fileRegex = re.compile(r'.*\.txt$') #tested and works
textFiles = [] #list container to hold files found via search
foundLines = [] #list container to hold lines found via search

#? Needed? mo = searchRegex.search(******PUT STRING OF CONTENTS OF FILE HERE)

# ? needed? print(mo.group())

#search for .txt files from the list of filesnames in current dir found
#appends to list of textfiles
for file in allFiles:
    if file.endswith('.txt'):
        textFiles.append(file)

#open each file and search it line by line for user input
#if input found add it to list of found results and then display that list
for file in textFiles:
    currentFile = open(file, 'r')
    for line in currentFile.readlines():
        if foundResults in line: 
            foundLines.append(line+" in "+file)

print(foundLines) 

    #open() function - pass string path indicating file want to open
    #returns a file object
    #.read() method of file object - read contents of file as str value 
    