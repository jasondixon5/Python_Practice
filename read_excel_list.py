#! /usr/bin/env python3
# read_excel_list.py - Take a vertical list of numbers in Excel and read them into a list

"""Arguments to pass when calling module (in addition to filename):
    - A filename, with extension
    - Name of the worksheet(tab) in the workbook that you want to use
    - Cell reference for where to start pulling in data (e.g., C3)
    - Number of rows of data to pull in (e.g., 10)
"""



import openpyxl
import os
from sys import argv

# Open workbook and save it in memory, verify working with right sheet
filename = argv[1]
# TODO - Build error checking - 'To start, enter a filename from the current directory (and don\'t forget the extension!):'
tabName = argv[2]
# TODO - Build error checking - 'Following are the tabs in this workbook. Enter the name of the tab that has the numbers you want to use without quotes {}:'.format(wb.get_sheet_names()))
startCellReference = argv[3]
lengthList = int(argv[4])

fullFilename = os.path.abspath(filename)
wb = openpyxl.load_workbook(fullFilename)
workingTab = wb.get_sheet_by_name(tabName)

startCell = workingTab[startCellReference]
startRowNumber = int('{}'.format(startCell.row))

# Get number version of column reference: Take cell reference provided, get letter for column, then get the ASCII number for the letter and subtract 64, so that "A" corresponds to "1".

# WARNING - Works for columns A - Z but not beginning with AA
startColumnLetter = '{}'.format(startCell.column)
startColumnNumber = ord(startColumnLetter) - 64
 
numbers = [workingTab.cell(row=row, column=startColumnNumber).value for row in range(startRowNumber, startRowNumber + lengthList)]

# TODO - Research how to break up lines in python

#print(numbers)
import stat_tools

print(stat_tools.standardDeviation(numbers))



# If the module is *imported*, __name__ is the name of the module
# If the module is *run on the commandline* __name__ is __main__
# So the following check says:
# "If this python file is being run from the command line, do..."

"""
print ("Name is: {}".format(__name__))
if __name__ == '__main__':
    print(standardDeviation([1, 4, 6]))
"""

# List scores that are outside of one st dev - find upper and lower limits, list scores that are higher than upper and lower than lower
"""
lowScoreLimit = averageScore - testStDev
highScoreLimit = averageScore + testStDev

withinRangeList = []
outsideRangeList = []
"""
"""
for score in scores:
    if score <= highScoreLimit:
        if score >= lowScoreLimit:
            withinRangeList.append(score)
""""""

for score in scores:
    if score > highScoreLimit or score < lowScoreLimit:
        outsideRangeList.append(score)
    else:
        withinRangeList.append(score)
    
#print("Scores within one standard deviation: {}".value(withinRangeList))
print("Mean is", averageScore)
print("Standard deviation is", round(testStDev,4))
print("Scores within one standard deviation: ", withinRangeList)
print("Scores outside one standard deviation: ", outsideRangeList)
print("Range of one standard deviation is between ", round(lowScoreLimit,2), "and ", round(highScoreLimit,2))

print(len(withinRangeList)/len(scores) * 100,"% of scores are within one standard deviation of the mean.")


"""
