import csv
import os
import usstateabre

# This is pyboss final
def employees (inputfile, outputfile):


    with open(inputfile, newline="", encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        firstrow = next(csvreader, None)

        with open(outputfile, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow(['Emp ID', 'First', 'Last', 'DOB', 'SSN', 'State'])

            for row in csvreader:
                empid = str(row[0])
                name = str(row[1])
                DOB = (row[2])
                SSN = str(row[3])
                state = str(row[4])

                stateabbreviation = usstateabre.us_state_abbrev[state]
                full = name.split()
                fname = full[0]
                lname = full[1]
#                DOB = datetime.datetime.strptime(str(row[2]), "%m/%d/%Y").strftime("%d/%m/%Y")
                DOB = str(row[2])
                bdob = DOB.split("-")
                byr= bdob[0]
                bmon=bdob[1]
                bday=bdob[2]
                dobn = str(bday) + "/" + str(bmon) + "/" + str(byr)
                finalssn = "*" * (len(SSN) - 6) + SSN[-4:]

                csvwriter.writerow([empid, str(fname), str(lname), dobn, str(finalssn), str(stateabbreviation)])

employees("employee_data1.csv", "employee_data1out.csv")
employees("employee_data2.csv", "employee_data2out.csv")