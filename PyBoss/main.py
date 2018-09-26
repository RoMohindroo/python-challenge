import os           # os library
import csv          # csv library
import datetime     # datetime library

# Function returns the state abbreviation indexed by state name
def get_stateabbrev(state):
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }

    if state in us_state_abbrev:        # Checks if index in dictionary
        return us_state_abbrev[state]   # Returns state abbreviation
    else:
        return "State"                  # Returns text for csv header

# Function converts datetime to desired output format
def get_date(datevar):
    try:                                # Error trap for csv header
        d = datetime.datetime.strptime(datevar, '%Y-%m-%d')
        # returns datetime in mm/dd/yyyy format
        return datetime.date.strftime(d, '%m/%d/%Y')
    except ValueError:                  # Value error, csv header
        return "DOB"                    # Returns text for csv header

# Function returns first name by splitting name field
def get_firstname(name):
    namelist = name.split()             # Splits on whitespace (default)
    if namelist[0] == 'Name':           # Checks for csv header
        namelist[0] = 'First Name'      # Writes corrected csv header to list
    return namelist[0]                  # Returns first item in split list

# Function returns last name by splitting name field
def get_lastname(name):
    namelist = name.split()             # Splits on whitespace (default)
    if namelist[-1] == 'Name':          # Checks for csv header
        namelist[-1] = 'Last Name'      # Writes corrected csv header to list
    return namelist[-1]                 # Returns last item in split list

# Function returns SSN in masked format
def get_ssn(ssn):
    if ssn == 'SSN':                    # Checks for csv header
        return ssn                      # Returns csv header
    else:
        ssnlist = ssn.split('-')        # Splits on '-' character
        # Returns masked SSN using last item in split list
        return ('***' + '-' + '**' + '-' + ssnlist[-1])

# Defines import file list
files = ['employee_data1.csv','employee_data2.csv']

for filename in files:                  # Iterates through file list

    # Specifies import path and file
    csv_in = os.path.join(".", "raw_data", filename)

    # Specifies export path and file
    csv_out = os.path.join(".", "output", filename)

    # Declares empty lists for each column of data
    emp_id = []
    emp_fname = []
    emp_lname = []
    emp_dob = []
    emp_ssn = []
    emp_state = []

    # Opens and reads csv
    with open(csv_in, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Iterates through each row in csv
        for row in csvreader:

            # Dsitributes csv data to associated lists
            emp_id.append(str(row[0]))

            emp_fname.append(get_firstname(row[1]))

            emp_lname.append(get_lastname(row[1]))

            emp_dob.append(get_date(str(row[2])))

            emp_ssn.append(get_ssn(row[3]))

            emp_state.append(get_stateabbrev(row[4]))

        # Combines lists into tuple
        combined_tuple = zip(emp_id, emp_fname, emp_lname, emp_dob, emp_ssn, emp_state)

    # Opens and writes csv
    with open(csv_out, "w", newline='') as output:
        csvfile = csv.writer(output)

        # Iterates through each row in tuple
        for line in combined_tuple:

            csvfile.writerow(line)      # Writes tuple row to csv

print("Process Complete!")              # Notifies user
