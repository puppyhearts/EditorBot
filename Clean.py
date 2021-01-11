import pandas as panda
import openpyxl
# Combines Sheets of Creators into a single, Alphabetically organized list 

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = panda.ExcelWriter('demo.xlsx', engine='xlsxwriter')
# Concatenate all Sheets into one   
df = panda.concat(panda.read_excel('demo.xlsx', sheet_name=None), ignore_index=True)
# Remove duplicates
df = panda.DataFrame.drop_duplicates(df)
# Arrange Alphabetically
df = df.sort_values('Creators')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='SheetClean', index=False)
# Close the Pandas Excel writer and output the Excel file.
writer.save()
