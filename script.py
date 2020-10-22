import pandas as pd

xl = pd.ExcelFile("C:\\Users\\think\\Desktop\\test.xlsx")

dfs = pd.read_excel(xl, sheet_name=None, na_values="Missing")

print(dfs)
print(dfs['Sheet1'])
