import pandas as panda
import openpyxl 

# Make an excel sheet of all Creators+Dates+VIAF_URLs to use as a database
# GG1 is the first 294 entries of the radiofreerainforest cassettes
# Converted from Swallow JSON to .xlsx

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = panda.ExcelWriter('demo.xlsx', engine='xlsxwriter')

# Number of Sheets (No. of Creator Columns in Total) 
n=0

# Set Up which page we're going to make the dataframe from (20 pages)
# Save every separate page as GG+ number
for gg in range(21):
    p = str(gg)
    Page_no= 'GG+'+p+'.xlsx'
    df = panda.read_excel (Page_No)
    # Create Dataframe From Sheet
    for x in range(29):
        s = str(x)
        s1 = str(n)
        n= n+1
        Creators_name = 'Creators/'+ s +'/name' 
        Creators_dates = 'Creators/'+ s +'/dates'
        Creators_url = 'Creators/'+ s +'/url'
        daf = panda.DataFrame({'Creators': (df[Creators_name].drop_duplicates()),
                               'Dates': (df[Creators_dates].drop_duplicates()),
                               'URLs': (df[Creators_url]).drop_duplicates()})
        
        Sheet = 'Sheet' + s1
        # Convert the dataframe to an XlsxWriter Excel object.
        daf.to_excel(writer, sheet_name=Sheet, index=False)
        
        print(n)

# Close the Pandas Excel writer and output the Excel file.
writer.save()


