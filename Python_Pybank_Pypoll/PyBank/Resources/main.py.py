# Modules - Start by importing relevant modules
import os
import csv

# Create lists to hold data
month_count = 0
prev_revenue = 0
monthly_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

# Set the path for file, it has been manually placed in the same folder, so both csv file and python VSC file in same folder
csvpath = os.path.join("budget_data.csv")
output_pathout = os.path.join("..", "Resources", "Budget Analysis")
print(csvpath) 

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

# To open the loop with a 'for' statement, to iterate for each row in the list
    for row in csvreader:

        # Tracking total - will require to collect number of months & revenue
        month_count = month_count + 1
        total_revenue = total_revenue + int(row[1])

        # Revenue 
        revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        monthly_change = monthly_change + [row[0]] 

        # Greatest increase
        if (revenue_change) > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change

        # Greatest decrease
        if (revenue_change) < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change

# Average revenue change
revenue_average = sum(revenue_change_list) / len(revenue_change_list)

# Generate output financial summary analysis
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_average}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print output
print(output)
# Export results to text file
with open(output_pathout, 'w') as txt_file:
    txt_file.write(output)



