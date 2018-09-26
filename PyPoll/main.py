import os
import csv

# Function generates and returns a separator line
def gensepline(char, count):
    sepline = str(char) * count
    return sepline

# Function receives dictionary and displays results to stdout
def displayoutput(candidates):
    print(gensepline('-', 25))

    # Calcualtes total votes by summing values in dictionary
    totalvotes = sum(candidates.values())

    # Displays total votes
    print(f"Total Votes: {totalvotes}")

    print(gensepline('-', 25))

    # Iterates through key-value pairs in dictionary
    for candidate, votes in candidates.items():

        # Calculates percentage of votes for each candidate
        cand_percent = round(((votes / totalvotes) * 100), 1)

        # Displays summary line for each candidate
        print(candidate + ": " + str(cand_percent) + '% (' + str(votes) + ')')

    print(gensepline('-', 25))

    # Finds winner by finding max value in dictionary
    winner = max(candidates, key=lambda key: candidates[key])

    print(f"Winner: {winner}")      # Displays winner

    print(gensepline('-', 25))

    print('\n')                     # Displays newline to separate results

# Function receives dictionary and writes results to output file
def writeoutput(cadidates):

    outfile = 'output.txt'          # Declares output file

    # Opens output file for write in append mode
    with open(outfile, 'a') as file_object:

        # Writes separator line, repeats
        file_object.write(gensepline('-', 25) + '\n')

        # Calcualtes total votes by summing values in dictionary
        totalvotes = sum(candidates.values())

        # Writes total votes to output file
        file_object.write("Total Votes: " + str(totalvotes) + '\n')

        file_object.write(gensepline('-', 25) + '\n')

        # Iterates through key-value pairs in dictionary
        for candidate, votes in candidates.items():

            # Calculates percentage of votes for each candidate
            cand_percent = round(((votes / totalvotes) * 100), 1)

            # Writes a summary line for each candidate to output file
            file_object.write(candidate + ": " + str(cand_percent) + '% (' + str(votes) + ')' + '\n')

        file_object.write(gensepline('-', 25) + '\n')

        # Finds winner by finding max value in dictionary
        winner = max(candidates, key=lambda key: candidates[key])

        # Writes winner to output file
        file_object.write("Winner: " + winner + '\n')

        file_object.write(gensepline('-', 25) + '\n')

        file_object.write('\n')         # Displays newline to separate results

# Defines import file list
files = ['election_data_2.csv','election_data_1.csv']

for filename in files:                  # Iterates through file list

    candidates = {}                     # Initializes empty dictionary

    # Specifies import path and file
    csv_in = os.path.join(".", "raw_data", filename)

    # Opens and reads csv
    with open(csv_in, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        next(csvreader)                 # skips header row

        # Iterates through each row in csv
        for row in csvreader:

            # if candidate not in dict, adds key and initializes value
            if row[2] not in candidates:
                candidates[row[2]] = 0

            candidates[row[2]] += 1     # increments dictionary value

    displayoutput(candidates)           # Calls function, passes dictionary

    writeoutput(candidates)             # Calls function, passes dictionary