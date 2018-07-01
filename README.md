# Project003
### 835 Parsing

The goal is to take something like this:  
```
ISA****************~CLP*12345**25****~CAS*CO*45*10~CAS*PR*3*15~CLP*23456**50*****~CAS*CO*97*50**96*75~IEA*asdf**asdf**** 
```
And extract the adjustment infomation into a table something like this:

Adj_Group_Code | Adj_Reason | Adj_Amount | CLP_Seq | Inv_Num
--- | --- | --- | --- | ---
CO | 45 | 10 | 1 | 12345
PR | 3 | 15 | 1 | 12345
CO | 97 | 50 | 2 | 23456
CO | 96 | 75 | 2 | 23456


Put these four files in your active directory:

Project003_835_Parsing_v3.py  
Project003_835_Parsing_v3-1_MakeSQL.py  
Project003_835_Parsing_v3-2_ReadSQL.py  
Project003_835_Test_File_Hor.txt  

Typing `python Project003_835_Parsing_v3.py` from the command line will output the table in the command line  
Typing `python Project003_835_Parsing_v3-1_MakeSQL.py` from the command line will output the table into a sqlite3 database  
Typing `python Project003_835_Parsing_v3-2_ReadSQL.py` from the command line will read from the sqlite3 database

Tested with:  
python 3.6.4  
pandas 0.22.0  
