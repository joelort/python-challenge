#for pybank
#import csv
import os
import csv

#import csv file.
csvpath = os.path.join("resources","budget_data.csv")
#outpath = os.paht.join("analysis_budget.txt")
#with open(output_path, 'w', encoding='utf-8', newline='') as csvfile:

#________________________________________________

# Reading CSV module
with open (csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    #print (csvreader)
    
    
#Read the header row firsy (for headers)
    csvheader = next(csvreader)
    #print (f"CSV Header: {csvheader}")
    #print (row)     
    
    lines = 0
    for row in csvreader:
        lines += 1 
    
  #____________________________________ _______________ 
with open (csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)
    column_sum = 0
    for row in csvreader:
        column_value = float(row[1])
        column_sum += column_value
        average = column_sum/lines
        
    #__________ print outcomes__________
#print ("Total months:", lines)    
#print ("this is the sum: ", "$",(column_sum))
#print ("The average: ", "$" ,(average))

    #__________________max value___________________
with open (csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)

    # from here the max
    max_value = float ("-inf")

    for row in csvreader:
        value = float(row[1])  
        if value > max_value:
            max_value = value
            max_row = row
            
#print("Greatest Increase in Profits: ", (max_row))
 
#__________________min value___________________    
with open (csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)
    
    
    # from here the min
    min_value = float ("inf")
    for row in csvreader:
        value = float(row[1])  
        if value < min_value:
            min_value = value
            min_row = row

#print("Greatest Decrease in Profits: ", min_row)
   
#__________________________output file___________
output_file = os.path.join("Pybank","analysis", "analysis.txt")
with open(output_file, "w",) as datafile:
    datafile.write ("Financial Analysis"+"\n"+ "_________________________"+ "\n")
    datafile.write ("Total of months: " + str(lines)+"\n")
    datafile.write ("Total: " + "$" + str (column_sum) + "\n")
    datafile.write ("Average change: (this is not right): " +"$" + str (average)+ "\n")
    datafile.write ("Greatest increase in profits: " + str(max_row)+"\n")
    datafile.write ("Greatest decrease in profits: " +str (min_row)) 
    
    

