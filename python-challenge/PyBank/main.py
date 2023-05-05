# Importing the csv module for reading the csv file
import csv


# Read the "budget_data.csv" file using csv module and a context manager
with open("Resources/budget_data.csv", "r") as file:
    # Using csv reader to read the file object
    reader = csv.reader(file)

    # Reading the header (first line of the file)
    header = next(reader)

    # Initialize output variables
    num_months = 0
    net_profit = 0

    prev_profit = None
    total_changes = 0

    max_profit_increase = 0
    max_profit_decrease = 0

    max_profit_increase_date = ""
    max_profit_decrease_date = ""

    # Iterate through the file data one row at a time
    for row in reader:
        # reading date and profit values
        date, profit = row

        # converting the string profit value into an integer
        profit = int(profit)

        # Calculate the total number of months
        num_months = num_months + 1

        # Calculate the net profit
        net_profit = net_profit + profit

        # Calculate the changes in Profit/Losses
        if prev_profit is not None:
            # Calculating the difference between current and previous profit
            change = profit - prev_profit

            # Adding it to the total change across the entire data
            total_changes = total_changes + change

            # Calculate the greatest increase in profits if the change is greater than the max_profit_increase
            if change > max_profit_increase:
                max_profit_increase = change
                max_profit_increase_date = date

            # Calculate the greatest decrease in profits if the change is less than the max_profit_decrease
            elif change < max_profit_decrease:
                max_profit_decrease = change
                max_profit_decrease_date = date

        # Assigning the profit as a previous profit as we will go onto the next record
        prev_profit = profit

# Calculating the Average change
average_change = total_changes / (num_months - 1)

# Printing or displaying the output to the terminal screen
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {num_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_profit_increase_date} (${max_profit_increase})")
print(f"Greatest Decrease in Profits: {max_profit_decrease_date} (${max_profit_decrease})")


# Writing the output to the .txt file
# Using csv module writer to write the text (ouptut) to the .txt file
with open("financial_analysis_output.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n\n")
    file.write(f"Total Months: {num_months}\n")
    file.write(f"Total: ${net_profit}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {max_profit_increase_date} (${max_profit_increase})\n")
    file.write(f"Greatest Decrease in Profits: {max_profit_decrease_date} (${max_profit_decrease})\n")
