import csv
import os
import datetime
import usstateabre

# This is the PyBoss option
def employees (inputfile, outputfile):


    if not os.path.exists(inputfile):
        print("File not found.")
        return

    with open(inputfile, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        firstrow = next(csvreader, None)


        with open(outputfile, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow(['Emp ID', 'First', 'Last', 'DOB', 'SSN', 'State'])

            for row in csvreader:
                empid = str(row[0])
                name = str(row[1])
                DOB = str(row[2])
                SSN = str(row[3])
                state = str(row[4])
                stateabbreviation = usstateabre.us_state_abbrev[state]

                fl = name.split()
                f = fl[0]
                l = fl[1]
     #           DOB = datetime.datetime.strptime(row[2], "%m/%d/%Y").strftime("%d/%m/%Y")
                finalssn = "*" * (len(SSN) - 6) + SSN[-4:]

                csvwriter.writerow([empid, str(f), str(l),DOB, str(finalssn), str(stateabbreviation)])

#calling function with data as inputs
employees("employee_data1.csv", "employee_data1out.csv")
employees("employee_data2.csv", "employee_data2out.csv")