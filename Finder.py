import pandas as panda
import openpyxl

# Find Empty/Missing Values in a Swallow Entry
df = panda.read_excel (r'GG1.xlsx')

for x in range(295):
    row = df.loc[x]
    id = row.swallow_id
    print ()
    print (id)
    v = False
  
    if panda.isna(df.loc[x,'Rights/rights']):
        print ('Rights Not Specified')
        v = True
    if panda.isna(df.loc[x,'Item_Description/genre/0/id']):
        print ('Genre not mentioned in Item Description')
        v = True
    if panda.isna(df.loc[x,'Item_Description/title_source']):
        print ('Source not mentioned for Title')
        v = True
    if panda.isna(df.loc[x,'Item_Description/production_context']):
        print ('Production Context not mentioned')
        v = True
    if panda.isna(df.loc[x,'Institution_and_Collection/item_ID']):
        print ('Item ID not Mentioned')
        v = True
        
    if panda.isna(df.loc[x,'Dates/0/id']):
        print ('No entry for Date of Recording')
        v = True
    else:
        if panda.isna(df.loc[x,'Dates/0/type']):
            print ('Type of Date not Specified')
            v = True
        if panda.isna(df.loc[x,'Dates/0/date']):
            print ('Date of recording not mentioned')
            v = True
        if panda.isna(df.loc[x,'Dates/0/source']):
            print ('Source of Date not Mentioned')
            v = True 
        
    for x1 in range(29):
        s = str(x1)
        Creators_name = 'Creators/'+ s +'/name' 
        Creators_dates = 'Creators/'+ s +'/dates'
        Creators_url = 'Creators/'+ s +'/url'
        Creators_id = 'Creators/'+ s +'/id'
        Creators_role = 'Creators/'+ s +'/role/0/id'
        if panda.notna(df.loc[x,Creators_id]):
            if panda.isna(df.loc[x,Creators_name]):
                print ('Creator ' + s + 's Name Missing')
                v = True
            if panda.isna(df.loc[x,Creators_dates]):
                print ('Creator ' + s + 's Date Missing')
                v = True
            if panda.isna(df.loc[x,Creators_url]):
                print ('Creator ' + s + 's URL Missing')
                v = True
            if panda.isna(df.loc[x,Creators_role]):
                print ('Creator ' + s + 's Role Missing')
                v = True
                
    for x2 in range(5):
        s = str(x2)
        Contributors_name = 'Contributors/'+ s +'/name' 
        Contributors_dates = 'Contributors/'+ s +'/dates'
        Contributors_url = 'Contributors/'+ s +'/url'
        Contributors_id = 'Contributors/'+ s +'/id'
        Contributors_role = 'Contributors/'+ s +'/role/0/id'
        if panda.notna(df.loc[x,Contributors_id]):
            if panda.isna(df.loc[x,Contributors_name]):
                print ('Contributor ' +s+ 's Name Missing')
                v = True
            if panda.isna(df.loc[x,Contributors_dates]):
                print ('Contributor ' +s+ 's Date Missing')
                v = True
            if panda.isna(df.loc[x,Contributors_url]):
                print ('Contributor ' +s+ 's URL Missing')
                v = True
            if panda.isna(df.loc[x,Contributors_role]):
                print ('Contributor ' +s+ 's Role Missing')
                v = True
            
    if panda.isna(df.loc[x,'Material_Description/0/id']):
        print ('No Entry Under Material Description')
        v = True
    else:
        if panda.isna(df.loc[x,'Material_Description/0/image'])and panda.isna(df.loc[x,'Material_Description/1/image']):
            print ('Image Missing')
            v = True
        if panda.isna(df.loc[x,'Material_Description/0/physical_condition']):
            print ('Physical Condition not Mentioned')
            v = True
        if (df.loc[x,'Material_Description/0/recording_type']) == -1:
            print ('Recording Type not mentioned')
            v = True
        if (df.loc[x,'Material_Description/0/sound_quality']) == -1:
            print ('Sound Quality not Mentioned')
            v = True
        if (df.loc[x,'Material_Description/0/extent']) == -1:
            print ('Extent not mentioned under Material Description')
            v = True 
        if (df.loc[x,'Material_Description/0/material_designation']) == -1:
            print ('Material Designation not Mentioned')
            v = True
        if (df.loc[x,'Material_Description/0/physical_composition']) == -1:
            print ('Physical Composition not mentioned')
            v = True
        if (df.loc[x,'Material_Description/0/AV_type']) == -1:
            print ('AV Type not mentioned')
            v = True           
    
    if panda.isna(df.loc[x,'Digital_File_Description/0/id']):
        print ('No Entry Under Digital File Description')
        v = True
    else:
        if panda.isna(df.loc[x,'Digital_File_Description/0/size']):
            print ('Size of Digital File Missing')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/0/duration']):
            print ('Duration of Audio not Mentioned')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/0/encoding']):
            print ('File Type not Mentioned')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/0/filename']):
            print ('File Name not Mentioned')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/0/duration']):
            print ('Duration of Audio not Mentioned')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/0/duration']):
            print ('Duration of Audio not Mentioned')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/0/duration']):
            print ('Duration of Audio not Mentioned')
            v = True           
    
    if panda.isna(df.loc[x,'Digital_File_Description/1/id']):
        print ('No Entry Under Digital File Description')
        v = True
    else:
        if panda.isna(df.loc[x,'Digital_File_Description/1/size']):
            print ('Size of Digital File Missing')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/1/duration']):
            print ('Duration of Audio not Mentioned')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/1/encoding']):
            print ('File Type not Mentioned')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/1/filename']):
            print ('File Name not Mentioned')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/1/duration']):
            print ('Duration of Audio not Mentioned')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/1/duration']):
            print ('Duration of Audio not Mentioned')
            v = True
        if panda.isna(df.loc[x,'Digital_File_Description/1/duration']):
            print ('Duration of Audio not Mentioned')
            v = True
            
    if v == False :
        print ('Nothing Missing')
