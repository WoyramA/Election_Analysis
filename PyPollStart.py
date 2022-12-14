#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

import csv
import os
dir(os)
# Add a variable to load a file from a path.
file_to_load = os.path.join("./Resources/election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("./analysis/election_analysis.txt")
#Open the election results and read the file
with open(file_to_load) as election_data:

#print the file object.
    print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
outfile = open(file_to_save, "w")
outfile.write("Hello World")

#Close the file
outfile.close()

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:


# Modify code 
    txt_file.write("Counties in the election\n--------------------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies.


# Open the election results and read the file.
with open(file_to_load) as election_data:    

#To do: Read and analyze the data here
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Print each row in the CSV file.
for row in file_reader:
    print(row)
    
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)
    print(headers)


    

