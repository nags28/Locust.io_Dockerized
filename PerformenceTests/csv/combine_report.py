from pandas import ExcelWriter
import glob
import os
import pandas as pd

writer = ExcelWriter("ConsolidateOutput.xlsx")

for filename in glob.glob("*.xlsx"):
    excel_file = pd.ExcelFile(filename)
    (_, f_name) = os.path.split(filename)
    (f_short_name, _) = os.path.splitext(f_name)
    for sheet_name in excel_file.sheet_names:
        df_excel = pd.read_excel(filename, sheet_name=sheet_name)
        df_excel.to_excel(writer, f_short_name, index=False)
        #+'_'+sheet_name
writer.save()
