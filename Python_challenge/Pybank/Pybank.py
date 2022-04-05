# # # create a Python script that analyzes the records to calculate each of the following:

# # * The total number of months included in the dataset

# # * The net total amount of "Profit/Losses" over the entire period

# # * The changes in "Profit/Losses" over the entire period, and then the average of those changes

# # * The greatest increase in profits (date and amount) over the entire period

# # * The greatest decrease in profits (date and amount) over the entire period
# Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $22564198
#   Average Change: $-8311.11
#   Greatest Increase in Profits: Aug-16 ($1862002)
#   Greatest Decrease in Profits: Feb-14 ($-1825558)



#import the modules
import csv
import os

#setting the path for csv file:

PyBankcsv =os.path.join("Resources","budget_data.csv")

#creating the list for storing datas
profit =[]
monthly_changes =[]
date=[]

#initalize the variable
count =0
total_profit = 0
total_change_profits = 0
initial_profit = 0

#now open the csv using the path pyBankcsv
with open(PyBankcsv,newline="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    csvheader= next(csvreader)
    for row in csvreader:
        count =count+1
        #this will be required whlie collecting the greatest increase and decrease in profit
        date.append(row[0])

        #append the profit info and calculate the total profit
        profit.append(row[1])
        total_profit = total_profit+ int(row[1])
        #calculate the average change in profits from month to month. Then calulate the average change in profits
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit
        #storing the monthly changes in list
        monthly_changes.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit
        #Calculate the average change in profits
        average_change_profits = (total_change_profits/count)
        #Find the max and min change in profits and the corresponding dates these changes were obeserved
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_increase_profits)]
        decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
    print("----------------------------------------------------------")

with open("finacial_analysis.txt", "w") as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")




