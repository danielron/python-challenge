import csv
import os

# This is the PyBank option final

def budget(inputfile, outputfile):
    if not os.path.exists(inputfile):
        print("File not found")
        return

    # Load the file and initialize variables
    with open(inputfile, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        firstrow = next(csvreader, None)
        revenue_list = []
        revenue_list_negative = []
        num_months = 0
        total = 0
        months = []
        mydict = {}
        prev_rev = None
        rev_change_sum = 0

        # Process rows
        for row in csvreader:
            month = str(row[0])
            revenue = int(row[1])
            months.append(month)
            mydict[month] = revenue
            total = total + revenue
            num_months = num_months + 1

            # Within each row except the first, compute the change in revenue from previous
            if prev_rev is not None:
                rev_change = revenue - prev_rev
                revenue_list.append(rev_change)
                rev_change_sum = rev_change + rev_change_sum

            prev_rev = revenue

        avg_rev_change = rev_change_sum / (num_months-1)
        greatestincrease = max(revenue_list)
        gi_index = revenue_list.index(max(revenue_list))
        inc_mon = months[gi_index + 1]
        greatestdecrease = min(revenue_list)
        gd_index = revenue_list.index(min(revenue_list))
        dec_mon = months[gd_index + 1]

    print("Financial Analysis")
    print("-------------------")
    print("Total months:", num_months)
    print("Total revenue:", total)
    print("Average revenue change:", avg_rev_change)
    print("Greatest increase in revenue:", greatestincrease, "and month is " +
inc_mon)
    print("Greatest decrease in revenue:", greatestdecrease, "and month is " +
dec_mon)
    print("-------------------")

# Specify the file to write to
    output_path = os.path.join(outputfile)

# print (output_path)
# Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(["Financial Analysis"])
        csvwriter.writerow(["-------------------"])
        csvwriter.writerow(["Total months:" + str(num_months)])
        csvwriter.writerow(["Total revenue:" + str(total)])
        csvwriter.writerow(["Average revenue change:" + str(avg_rev_change)])
        csvwriter.writerow(["Greatest Increase:" + str(greatestincrease) + " and month is " + inc_mon])
        csvwriter.writerow(["Greatest Decrease:" + str(greatestdecrease) + " and month is " + dec_mon])
        csvwriter.writerow(["-------------------"])

# Calling budget function with data files as inputs
budget("budget_data_1.csv", "financial_summary1.txt")
budget("budget_data_2.csv", "financial_summary2.txt")