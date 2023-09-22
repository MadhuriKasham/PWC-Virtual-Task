import pandas as pd
import numpy as np


df = pd.read_excel('KPMG_VI_New_raw_data_update_final.xlsx', 
                sheet_name= 'Transactions')
# print(df)
df.fillna('Nan', inplace=True)
df['standard_cost'].fillna(0, inplace=True, downcast='infer')
df.to_excel('Task1.xlsx')
# avg_std_cost= df['standard_cost'].mean()
# df['standard_cost'].replace(0,avg_std_cost)

# df.to_excel('Task1.xlsx')