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

table['CLP_Seq'] = (table[0] == 'CLP').cumsum()

da_list = []
for x in range(len(table)): 
    if table[0][x] == 'CLP':
        da_list_inner=[]
        da_list_inner.append(table[1][x])
        da_list_inner.append(table['CLP_Seq'][x])
        da_list.append(da_list_inner)

table_two = pandas.DataFrame(da_list, columns=['Inv_Num','CLP_Seq'])
#print(table_two)

table_three = pandas.merge(table, table_two, how='left', on=['CLP_Seq'])
#print(table_three)


final_list = []
for x in range(len(table_three)):
    if table[0][x] == 'CAS':
        y=2
        z=3
        while table_three[y][x]!=None:           
            final_list_inner=[]
            final_list_inner.append(table_three[1][x])
            final_list_inner.append(table_three[y][x])
            final_list_inner.append(table_three[z][x])
            final_list_inner.append(table_three['CLP_Seq'][x])
            final_list_inner.append(table_three['Inv_Num'][x])
            final_list.append(final_list_inner)
            y=y+3
            z=z+3
            
final_table = pandas.DataFrame(final_list, columns=['Adj_Group_Code',
                                                    'Adj_Reason',
                                                    'Adj_Amount',
                                                    'CLP_Seq',
                                                    'Inv_Num'])

print(final_table)

#print(max(table['CLPSEQ']))
#print(table.iloc[0][0])
#print(table)
