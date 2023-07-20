#import csv
import os
import csv


#import cvs file part 2
csvpath = os.path.join ("election_data.csv")

#read csv___________
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next (csvreader)
print (f"CSV Header: {csvheader}")