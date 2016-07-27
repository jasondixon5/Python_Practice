#! /usr/bin/env python3
# bulletPointAdder.py - Adds bullet points to start of each line of text on the clipboard starting with the 3rd line (skips first two).

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)-2):    #loop through all indexes in the "lines" list
    lines[i + 2] = '* ' + lines[i + 2] #add star to ech string in "lines" list
text = '\n'.join(lines)

pyperclip.copy(text)
