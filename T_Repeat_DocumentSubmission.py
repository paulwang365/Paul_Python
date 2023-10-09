#create time: 2023-09-25
#created by Paul.

import pandas as pd
import numpy as np  # Import numpy for NaN values

df_get = pd.read_csv(r'C:\A_TEMPUS_project\TEMPUS_Original_Data_PaulWork.csv')
#change to lowercase
df_get.columns = map(str.lower, df_get.columns)
# Rename one column name 'participant_id' to 'record_id'
df_get.rename(columns={'participant_id': 'record_id'}, inplace=True)
df_get.rename(columns={'document submission_complete': 'document_submission_complete'}, inplace=True )

# create an Empty DataFrame, since not too much columns
# object With column names only
df_tem = pd.DataFrame(columns = ['record_id', 'redcap_event_name', 'redcap_repeat_instrument','redcap_repeat_instance','docsubyn',
                             'doctype1','doccert','document_submission_complete'])
#print(df)

# Initialize variables outside of the loop
record_id = None
repeat_Time = None
docsubyn = None
doctype1 = None
doctype2 = None
doctype3 = None
doctype4 = None
doctype5 = None
doctype6 = None
doctype7 = None
doctype8 = None
doctype9 = None
doctype10 = None
doctype11 = None
doccert = None
document_submission_complete = None

#docsubyn
#doctype1(1)--doctype1(2)   ---doctype1(11)
#doccert
#document_submission_complete

# Loop through the column names
for column_name in df_get.columns:
    if column_name == 'doctype1(1)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'document_submission'
      repeat_Time = 1
      docsubyn = df_get['docsubyn']
      doctype1 = df_get['doctype1(1)']
      doccert = df_get['doccert']
      document_submission_complete = df_get['document_submission_complete']

      
      data1 = {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' : repeat_Time,
            'docsubyn' : docsubyn,
            'doctype1' : doctype1,
            'doccert' : doccert,
            'document_submission_complete' : document_submission_complete,
           
             }
      original_df1 = pd.DataFrame(data1)
      
    if column_name == 'doctype1(2)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'document_submission'
      repeat_Time = 2
      docsubyn = df_get['docsubyn']
      doctype2 = df_get['doctype1(2)']
      doccert = df_get['doccert']  #??need ask
      document_submission_complete = df_get['document_submission_complete']
      data2 = {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' : repeat_Time,
            'docsubyn' : docsubyn,
            'doctype1' : doctype2,
            'doccert' : doccert,
            'document_submission_complete' : document_submission_complete,
           
             }
      original_df2 = pd.DataFrame(data2)
      

    if column_name == 'doctype1(3)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'document_submission'
      repeat_Time = 3
      docsubyn = df_get['docsubyn']
      doctype3 = df_get['doctype1(3)']
      doccert = df_get['doccert']  #???
      document_submission_complete = df_get['document_submission_complete']
      data3 = {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' : repeat_Time,
            'docsubyn' : docsubyn,
            'doctype1' : doctype3,
            'doccert' : doccert,
            'document_submission_complete' : document_submission_complete,
           
             }
      original_df3 = pd.DataFrame(data3)

    if column_name == 'doctype1(4)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'document_submission'
      repeat_Time = 4
      docsubyn = df_get['docsubyn']
      doctype4 = df_get['doctype1(4)']
      doccert = df_get['doccert']  #???
      document_submission_complete = df_get['document_submission_complete']
      data4= {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' : repeat_Time,
            'docsubyn' : docsubyn,
            'doctype1' : doctype4,
            'doccert' : doccert,
            'document_submission_complete' : document_submission_complete,
           
             }
      original_df4 = pd.DataFrame(data4)

    if column_name == 'doctype1(5)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'document_submission'
      repeat_Time = 5
      docsubyn = df_get['docsubyn']
      doctype5 = df_get['doctype1(5)']
      doccert = df_get['doccert']  #???
      document_submission_complete = df_get['document_submission_complete']
      data5= {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' : repeat_Time,
            'docsubyn' : docsubyn,
            'doctype1' : doctype5,
            'doccert' : doccert,
            'document_submission_complete' : document_submission_complete,
           
             }
      original_df5 = pd.DataFrame(data5)

    if column_name == 'doctype1(6)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'document_submission'
      repeat_Time = 6
      docsubyn = df_get['docsubyn']
      doctype6 = df_get['doctype1(6)']
      doccert = df_get['doccert']  #???
      document_submission_complete = df_get['document_submission_complete']
      data6= {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' : repeat_Time,
            'docsubyn' : docsubyn,
            'doctype1' : doctype6,
            'doccert' : doccert,
            'document_submission_complete' : document_submission_complete,
           
             }
      original_df6 = pd.DataFrame(data6)

    if column_name == 'doctype1(7)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'document_submission'
      repeat_Time = 7
      docsubyn = df_get['docsubyn']
      doctype7 = df_get['doctype1(7)']
      doccert = df_get['doccert']  #???
      document_submission_complete = df_get['document_submission_complete']
      data7= {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' : repeat_Time,
            'docsubyn' : docsubyn,
            'doctype1' : doctype7,
            'doccert' : doccert,
            'document_submission_complete' : document_submission_complete,
           
             }
      original_df7 = pd.DataFrame(data7)

    
    if column_name == 'doctype1(8)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'document_submission'
      repeat_Time = 8
      docsubyn = df_get['docsubyn']
      doctype8 = df_get['doctype1(8)']
      doccert = df_get['doccert']  #???
      document_submission_complete = df_get['document_submission_complete']
      data8= {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' : repeat_Time,
            'docsubyn' : docsubyn,
            'doctype1' : doctype8,
            'doccert' : doccert,
            'document_submission_complete' : document_submission_complete,
           
             }
      original_df8 = pd.DataFrame(data8)

      
    if column_name == 'doctype1(9)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'document_submission'
      repeat_Time = 9
      docsubyn = df_get['docsubyn']
      doctype9 = df_get['doctype1(9)']
      doccert = df_get['doccert']  #???
      document_submission_complete = df_get['document_submission_complete']
      data9= {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' : repeat_Time,
            'docsubyn' : docsubyn,
            'doctype1' : doctype9,
            'doccert' : doccert,
            'document_submission_complete' : document_submission_complete,
           
             }
      original_df9 = pd.DataFrame(data9)

         
    if column_name == 'doctype1(10)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'document_submission'
      repeat_Time = 10
      docsubyn = df_get['docsubyn']
      doctype10 = df_get['doctype1(10)']
      doccert = df_get['doccert']  #???
      document_submission_complete = df_get['document_submission_complete']
      data10= {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' : repeat_Time,
            'docsubyn' : docsubyn,
            'doctype1' : doctype10,
            'doccert' : doccert,
            'document_submission_complete' : document_submission_complete,
           
             }
      original_df10 = pd.DataFrame(data10)

    if column_name == 'doctype1(11)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'document_submission'
      repeat_Time = 11
      docsubyn = df_get['docsubyn']
      doctype11 = df_get['doctype1(11)']
      doccert = df_get['doccert']  #???
      document_submission_complete = df_get['document_submission_complete']
      data11= {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' : repeat_Time,
            'docsubyn' : docsubyn,
            'doctype1' : doctype11,
            'doccert' : doccert,
            'document_submission_complete' : document_submission_complete,
           
             }
      original_df11 = pd.DataFrame(data11)

      df_tem = pd.concat([original_df1, original_df2, original_df3,original_df4,original_df5,original_df6,original_df7,original_df8,original_df9,original_df10,original_df11])

      df_tem.to_excel(r'C:\A_TEMPUS_project\Repeat_DocumentSubmission_Data_Template.xlsx', index=False)
      print('Done!')

      #since found {nul} value in some cells and cannot load into RedCap. have to solve it. see below
# Replace "{null}" with empty cells, I create a function to remove {null}
def replace_null_with_empty(cell_value):
    return '' if cell_value == '{null}' else cell_value

# Load the Excel file into a DataFrame
df_clean = pd.read_excel(r'C:\A_TEMPUS_project\Repeat_DocumentSubmission_Data_Template.xlsx')

# Apply the replacement function to all cells in the DataFrame
df_clean = df_clean.applymap(replace_null_with_empty)


# Change the value in cell if it equals 'V5_2' to '2'
df_clean.loc[df_clean['document_submission_complete'] == 'V4_0', 'document_submission_complete'] = '2'
df_clean.loc[df_clean['document_submission_complete'] == 'V4_2', 'document_submission_complete'] = '2'
df_clean.loc[df_clean['document_submission_complete'] == 'V4_8', 'document_submission_complete'] = '2'
df_clean.loc[df_clean['document_submission_complete'] == 'V5_0', 'document_submission_complete'] = '0'
df_clean.loc[df_clean['document_submission_complete'] == 'V5_2', 'document_submission_complete'] = '2'
df_clean.loc[df_clean['document_submission_complete'] == 'V5_6', 'document_submission_complete'] = '2'
df_clean.loc[df_clean['doccert'] == 'TRUE', 'doccert'] = '1'
df_clean.loc[df_clean['doccert'] == 'FALSE', 'doccert'] = '0'



# Delete rows where all specified columns are null
df_clean = df_clean.dropna(subset=["doctype1"], how="all")
df_clean.reset_index


df_clean.to_excel(r'C:\A_TEMPUS_project\Repeat_DocumentSubmission_Data_cleaned.xlsx', index=False)


