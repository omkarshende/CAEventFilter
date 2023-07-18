import pandas as pd
import sys

check_file = sys.argv[1]
input_files = sys.argv[2:]
num_files = len(input_files)

check_file_data = pd.read_csv(check_file, header=None)
input_data = pd.DataFrame()

for i in range(num_files):
    temp =  pd.read_csv(input_files[i], encoding='latin-1', header=0, usecols=['Email', 'Spouse/Partner Email'])
    input_data = pd.concat([input_data, temp])

check_file_data['isvalid'] = (check_file_data.iloc[:,0].isin(input_data.iloc[:,0]) | check_file_data.iloc[:,0].isin(input_data.iloc[:,1]))
output_data = check_file_data[check_file_data['isvalid'] == True]
output_data.iloc[:,0].to_csv('output.csv',index=False, header=False)
