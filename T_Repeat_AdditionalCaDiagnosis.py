#create time: 2023-09-22
#created by Paul.
#create a simple function to Replace "{null}" with empty cells
#def replace_null_with_empty(cell_value):

import pandas as pd
import numpy as np  # Import numpy for NaN values


df_get = pd.read_csv(r'C:\A_TEMPUS_project\TEMPUS_Original_Data_PaulWork.csv')
#change to lowercase
df_get.columns = map(str.lower, df_get.columns)
# Rename one column name 'participant_id' to 'record_id'
df_get.rename(columns={'participant_id': 'record_id'}, inplace=True)
df_get.rename(columns={'additional cancer diagnosis_complete': 'additional_cancer_diagnosis_complete'}, inplace=True )

df_tem = pd.read_excel(r'C:\A_TEMPUS_project\Paul_Test_Repeat_AdditionalCancerDiagnosis_Template.xlsx')
print(df_tem)

# Initialize variables outside of the loop
record_id = None
repeat_Time = None
mh2yn = None
mh2stdt = None
mh2icd10 = None
mh2stgdx = None
mh2stgcr = None
additional_cancer_diagnosis_complete = None

# Loop through the column names
for column_name in df_get.columns:
    if column_name == 'mh2stdt(1)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'additional_cancer_diagnosis'
      repeat_Time = 1
      mh2yn = df_get['mh2yn']
      mh2stdt = df_get['mh2stdt(1)']
      mh2icd10 = df_get['mh2icd10(1)']
      mh2stgdx = df_get['mh2stgdx(1)']
      mh2stgcr = df_get['mh2stgcr(1)']
      additional_cancer_diagnosis_complete = df_get['additional_cancer_diagnosis_complete']
     
      print(column_name)
      print(record_id)
      print(repeat_Time)
      print(mh2yn)
      print(mh2stdt)
      print(mh2icd10)

      data1 = {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' :repeat_Time,
            'mh2yn' :  mh2yn,
            'mh2stdt' : mh2stdt,
            'mh2icd10' : mh2icd10,
            'mh2stgdx' :mh2stgdx,
            'mh2stgcr' : mh2stgcr,
            'additional_cancer_diagnosis_complete' : additional_cancer_diagnosis_complete,
             }
      original_df1 = pd.DataFrame(data1)
      print(original_df1)

      # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df1, ignore_index=True)
      print(df_tem)

    if column_name == 'mh2stdt(2)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'additional_cancer_diagnosis'
      repeat_Time = 2
      mh2yn =  df_get['mh2yn']
      mh2stdt = df_get['mh2stdt(2)']
      mh2icd10 = df_get['mh2icd10(2)']
      mh2stgdx = df_get['mh2stgdx(2)']
      mh2stgcr = df_get['mh2stgcr(2)']
      additional_cancer_diagnosis_complete = df_get['additional_cancer_diagnosis_complete']

      print(column_name)
      print(repeat_Time)
      print(mh2yn)
      print(mh2stdt)
      print(mh2icd10)
      print( mh2stgdx)
      print(mh2stgcr)
      data2 = {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' :repeat_Time,
            'mh2yn' :  mh2yn,
            'mh2stdt' : mh2stdt,
            'mh2icd10' : mh2icd10,
            'mh2stgdx' :mh2stgdx,
            'mh2stgcr' : mh2stgcr,
            'additional_cancer_diagnosis_complete' : additional_cancer_diagnosis_complete,
             }
      original_df2 = pd.DataFrame(data2)
      print(original_df2)

      # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df2, ignore_index=True)
      print(df_tem)

    if column_name == 'mh2stdt(3)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'additional_cancer_diagnosis'
      repeat_Time = 3
      mh2yn = df_get['mh2yn']
      mh2stdt = df_get['mh2stdt(3)']
      mh2icd10 = df_get['mh2icd10(3)']
      mh2stgdx = df_get['mh2stgdx(3)']
      mh2stgcr = df_get['mh2stgcr(3)']
      additional_cancer_diagnosis_complete = df_get['additional_cancer_diagnosis_complete']
      print(column_name)
      print(repeat_Time)
      print(mh2yn)
      print(mh2stdt)
      print(mh2icd10)
      print( mh2stgdx)
      print(mh2stgcr)

      data3 = {
      
            'record_id' : record_id,
            'redcap_event_name' : redcap_event_name,
            'redcap_repeat_instrument' : redcap_repeat_instrument,
            'redcap_repeat_instance' :repeat_Time,
            'mh2yn' :  mh2yn,
            'mh2stdt' : mh2stdt,
            'mh2icd10' : mh2icd10,
            'mh2stgdx' :mh2stgdx,
            'mh2stgcr' : mh2stgcr,
            'additional_cancer_diagnosis_complete' : additional_cancer_diagnosis_complete,
             }
      original_df3 = pd.DataFrame(data3)
      print(original_df3)

      # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df3, ignore_index=True)
      print(df_tem)




df_tem.to_excel(r'C:\A_TEMPUS_project\Repeat_AdditionalCaDiagnosis_Data_Template.xlsx', index=False)

#since found {nul} value in some cells and canot load into RedCap. have to solve it. see below
# Replace "{null}" with empty cells
def replace_null_with_empty(cell_value):
    return '' if cell_value == '{null}' else cell_value

# Load the Excel file into a DataFrame
df_clean = pd.read_excel(r'C:\A_TEMPUS_project\Repeat_AdditionalCaDiagnosis_Data_Template.xlsx')

# Apply the replacement function to all cells in the DataFrame
df_clean = df_clean.applymap(replace_null_with_empty)



# Change the value in cell if it equals 'V5_2' to '2'
df_clean.loc[df_clean['additional_cancer_diagnosis_complete'] == 'V5_2', 'additional_cancer_diagnosis_complete'] = '2'
df_clean.loc[df_clean['additional_cancer_diagnosis_complete'] == 'V5_6', 'additional_cancer_diagnosis_complete'] = '2'
df_clean.loc[df_clean['additional_cancer_diagnosis_complete'] == 'V4_2', 'additional_cancer_diagnosis_complete'] = '2'
df_clean.loc[df_clean['additional_cancer_diagnosis_complete'] == 'V4_8', 'additional_cancer_diagnosis_complete'] = '2'


# Delete rows where all specified columns are null
df_clean = df_clean.dropna(subset=["mh2stdt", "mh2icd10", "mh2stgdx","mh2stgcr"], how="all")
df_clean.reset_index


# Print the resulting DataFrame
#print(df_clean)

df_clean.to_excel(r'C:\A_TEMPUS_project\Repeat_AdditionalCaDiagnosis_Data_cleaned.xlsx', index=False)
