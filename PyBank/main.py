# Import the os module and module for reading .csv files
import os
import csv

#identify the .csv path
cwkdir = os.getcwd()
csvpath = os.path.join(cwkdir,'Resources','budget_data.csv')

#Define Variables
months = []
revenue = []
total_revenue = 0
monthly_revenue_change = []

 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    #Find totals for months and revenue
    for row in csvreader:
        months.append(row[0])
        total_months =(len(months))
        total_revenue = total_revenue + int(row[1])
        revenue.append(int(row[1]))
    
    #Find the monthly changes in revenue
    for i in range(len(revenue)-1):
        monthly_revenue_change.append(revenue[i+1]-revenue[i])

#Find the min and max of the monthly profit changes
max_increase_revenue = max(monthly_revenue_change)
max_decrease_revenue = min(monthly_revenue_change)

#Find the index of the max and min of revenue change to find the corresponding month where that revenue change occured
max_increase_month = monthly_revenue_change.index(max_increase_revenue)+1
max_decrease_month = monthly_revenue_change.index(max_decrease_revenue)+1
#assign the date values to the index
max_month = months[max_increase_month]
min_month = months[max_decrease_month]
    
#print the analysis to the terminal
print("Financial Analysis\n---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_revenue}")
print(f"Average Profit Change: ${round(sum(monthly_revenue_change)/len(monthly_revenue_change),2)}")
print(f"Greatest Increase in Profits: {max_month} (${max_increase_revenue})")
print(f"Greatest Decrease in Profits: {min_month} (${max_decrease_revenue})")
    
#Export the analysis as a text file
export_file = os.path.join( cwkdir, "analysis", "financial_analysis.txt")

with open(export_file, "w") as output:
    
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total months: {total_months}\n")
    output.write(f"Total: ${total_revenue}\n")
    output.write(f"Average Profit Change:  ${round(sum(monthly_revenue_change)/len(monthly_revenue_change),2)}\n")
    output.write(f"Greatest Increase in Profits: {max_month} (${max_increase_revenue})\n")
    output.write(f"Greatest Decrease in Profits: {min_month} (${max_decrease_revenue})\n")
  
        
    

   
