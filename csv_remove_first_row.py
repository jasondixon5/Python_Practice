#! /usr/bin/env python3
#csv_remove_first_row.py - takes a csv file, removes first row, writes rest into new file

import csv

sourceFile = open('example.csv')
sourceValues = csv.reader(sourceFile)
outputFile = open('new_example.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)

for row in sourceValues:
    if sourceValues.line_num == 1:
        continue
    else:
        outputWriter.writerow(row)
    

outputFile.close()