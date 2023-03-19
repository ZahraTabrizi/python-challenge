import os
import csv

#set path for file
budget_data_csv = os.path.join("Resources", "budget_data.csv")
file_path = os.path.join("Resources", "analysis.txt")

#Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0


#open the csv file
with open(budget_data_csv) as csvfile:  
    csvreader = csv.DictReader(csvfile)

    #Loop through to find total months
    for row in csvreader:

        #Count the total of months
        total_months += 1

        #Calculate the total revenue over the entire period
        total_revenue = total_revenue + int(row["Profit/Losses"])

        #Calculate the average change in revenue between months over the entire period
        revenue_change = float(row["Profit/Losses"])- previous_revenue
        previous_revenue = float(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row["Date"]]
       

        #The greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row['Date']
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)

with open(file_path, 'w') as txt_file:
     txt_file.write('Hello This is first line')

     #txt_file.write(total_revenue)
     #txt_file.write(total_months)
     #txt_file.write(revenue)
     #txt_file.write(previous_revenue)
     #txt_file.write(month_of_change)
     #txt_file.write(revenue_change)
     #txt_file.write(greatest_decrease)
     #txt_file.write(greatest_increase)
     #txt_file.write(revenue_change_list)
     #txt_file.write(revenue_average)