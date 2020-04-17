#Dependencies
import csv
import os

#Creating the path where the data file is located, the financial data is called: budget_data.csv
csvpath = os.path.join("Resources/budget_data.csv")

#The dataset is composed of two columns: Date and Profit/Losses.
#Setup for reading the csv file and start a list of cell values.

with open(csvpath) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',') #creating the csv_reader, spliting the data using commas
    
    header = next(csv_reader) #Skiping the first column of header

    month = []
    revenue = [] 
    revenue_change = []
    monthly_change = []
                 
#Using "for loop" to go down along the rows 

#for - determining the months     
    for row in csv_reader:
        month.append(row[0])
        revenue.append(row[1])

 #for- determining the total revenue 
    revenue_int = map(int,revenue) #The map() function executes a specified function for each item in a iterable.
    total_revenue = (sum(revenue_int))


 #for - determining the average change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        revenue_change.append(profit_loss)
    
    Total = sum(revenue_change)
    monthly_change = Total / len(revenue_change)
    
#Greatest Increase
    profit_increase = max(revenue_change)
    gI = revenue_change.index(profit_increase)
    month_increase = month[gI+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
    gD = revenue_change.index(profit_decrease)
    month_decrease = month[gD+1]


#Printing the statements


print(f'--------------------------------------------------------'+'\n')
print(f'Financial Analysis'+'\n')
print(f'---------------------------------------------------------'+'\n')


print("Total number of months: " + str(len(month)))

print("Total Revenue in period: $ " + str(total_revenue))
      
print("Average monthly change in Revenue : $" + str(monthly_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase}) ")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

print(f'---------------------------------------------------------'+'\n')


#Export a text file with the results

results = open("Results_pyBank.txt", "w")

results.write("Financial Analysis\n")

results.write("------------------------\n")

results.write("Total months: " + str(len(month)) + "\n")

results.write("Total: $" + str(total_revenue) + "\n")

results.write("Average change: $" + str(monthly_change) + "\n")

results.write(f"Greatest increase in Profits: {month_increase} (${profit_increase}) \n")

results.write(f"Greatest decrease in Profits: {month_decrease} (${profit_decrease}) \n")


results.write("------------------------\n")
results.close()


#the end