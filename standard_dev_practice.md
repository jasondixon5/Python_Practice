```
#! /usr/bin/env python3
# variance.py - module to calculate variance and standard deviation from Excel file

import openpyxl
import math

# Open workbook and save it in memory, verify working with right sheet

wb = openpyxl.load_workbook('/Users/jasondixon/Projects/Var-Stand Dev Practice.xlsx')

# Test scores are in column A, cells 4-13

scoresTab = wb.get_sheet_by_name('Test Scores')
scores = []

for row in range(4, 14):
    scores.append(scoresTab.cell(row=row, column=1).value)

#print(scores)

# TODO - Find mean of test scores (add and divide by n)
averageScore = sum(scores) / len(scores)

#print(averageScore)

# TODO - Find Variance - mean of squares of difference from mean
def vari(numberList):
    sumSquares = [(a - averageScore) ** 2 for a in numberList]
    return sum(sumSquares) / len(scores)
    
#print(vari(scores))
testScoresVariance = vari(scores)

# Find standard deviation - square root of variance
testStDev = math.sqrt(vari(scores))

#print(testStDev)

# List scores that are outside of one st dev - find upper and lower limits, list scores that are higher than upper and lower than lower

lowScoreLimit = averageScore - testStDev
highScoreLimit = averageScore + testStDev

withinRangeList = []
outsideRangeList = []
"""for score in scores:
    if score <= highScoreLimit:
        if score >= lowScoreLimit:
            withinRangeList.append(score)
"""
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

```
