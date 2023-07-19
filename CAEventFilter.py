import pandas as pd
import sys

# Read in command line arguments for files
email_file = sys.argv[1]
roster_files = sys.argv[2:]
num_rosters = len(roster_files)

emails = pd.read_csv(email_file, header=None)
roster = pd.DataFrame()

# Iterate through roster files using Ahad's formatting and build up a database of emails
for i in range(num_rosters):
    new_roster = pd.read_csv(roster_files[i], encoding='latin-1', header=0, usecols=['Email', 'Spouse/Partner Email'])
    roster = pd.concat([roster, new_roster])

# Check if the input emails exist in the database in either student or partner columns
output = emails[ emails.iloc[:,0].isin(roster.iloc[:,0]) | emails.iloc[:,0].isin(roster.iloc[:,1]) ]

# Print out the data as a list
output.iloc[:,0].to_csv('output.csv',index=False, header=False)
print("{0:5d} emails matched from {1:5d} submissions".format(len(output.index),len(emails.index)))