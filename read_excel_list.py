#! /usr/bin/env python3
# read_excel_list.py - Take a vertical list of numbers in Excel and read them into a list
# Also tests importing functions from another module (for statistics) and returning a result

import openpyxl
import os

# Open workbook and save it in memory, verify working with right sheet
filename = input('To start, enter a filename from the current directory (and don\'t forget the extension!): ')
fullFilename = os.path.abspath(filename)
wb = openpyxl.load_workbook(fullFilename)


# Pass filename, tab name, and range for list of numbers
tabName = input('Following are the tabs in this workbook. Enter the name of the tab that has the numbers you want to use without quotes {}:'.format(wb.get_sheet_names()))
numbersTab = wb.get_sheet_by_name(tabName)

numbers = []

startCell = numbersTab[input('Enter cell address (e.g., B2) where list of numbers starts: ')]
lengthList = int(input('Enter how many numbers to include in calculations: '))
startRowNumber = int('{}'.format(startCell.row))

# Get number version of column reference: Take cell reference provided, get letter for column, then get the ASCII number for the letter and subtract 64, so that "A" corresponds to "1".

# WARNING - Works for columns A - Z but not beginning with AA
startColumnLetter = '{}'.format(startCell.column)
startColumnNumber = ord(startColumnLetter) - 64
 
for row in range(startRowNumber, startRowNumber + lengthList):
    numbers.append(numbersTab.cell(row=row, column=startColumnNumber).value)

#print(numbers)
import stat_tools

print(stat_tools.standardDeviation(numbers))
