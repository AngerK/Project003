#! python3
# Project003_835_Parsing.py

"""
This script parses necessary elements of an 835 remit file.
"""

import pandas

# Extract Data from 835 file
def get_data():
    with open(r'C:\Users\KEITH\PythonScripts\Project003_835_Test_File_Hor.txt') as raw_file:
        file_content = raw_file.readlines()
        segments_list_get = file_content[0].split("~")
        return segments_list_get

# Load 835 segments into pandas
def load_data(data_to_load):
    df = pandas.DataFrame(data_to_load)
    df = df[0].str.split('*', expand=True)
    return df
        
segments_list = get_data()

table = load_data(segments_list)

da_list = []

CLP_Seq = 0

for x in range(len(table)): 
    if table[0][x] == 'CLP':    #obtain CLP level data
        CLP_Seq = CLP_Seq + 1
        Inv_Num = table[1][x]

    if table[0][x] == 'CAS':    #obtain CAS level data
        y=2
        z=3
        while table[y][x]!=None:           
            da_list_inner=[]
            da_list_inner.append(table[1][x])   #Adj_Group_Code
            da_list_inner.append(table[y][x])   #Adj_Reason
            da_list_inner.append(table[z][x])   #Adj_Amount
            da_list_inner.append(CLP_Seq)
            da_list_inner.append(Inv_Num)
            da_list.append(da_list_inner)
            y=y+3
            z=z+3
            
final_table = pandas.DataFrame(da_list, columns=['Adj_Group_Code',
                                                 'Adj_Reason',
                                                 'Adj_Amount',
                                                 'CLP_Seq',
                                                 'Inv_Num'])

print(final_table)