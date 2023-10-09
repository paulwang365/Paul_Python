#create time: 2023-09-26
#created by Paul.

import pandas as pd
import numpy as np  # Import numpy for NaN values
import time


df_get = pd.read_csv(r'C:\A_TEMPUS_project\TEMPUS_Original_Data_PaulWork.csv')

#change to lowercase
df_get.columns = map(str.lower, df_get.columns)
# Rename one column name 'participant_id' to 'record_id'
df_get.rename(columns={'participant_id': 'record_id'}, inplace=True)
df_get.rename(columns={'prior cancer therapies_complete': 'prior_cancer_therapies_complete'}, inplace=True )

# check data and clean data
df_get.loc[df_get['cmpryn'] == 'TRUE', 'cmpryn'] = '1'
df_get.loc[df_get['cmpryn'] == 'not_available', 'cmpryn'] = ''

# Drop rows where column is empty (NaN or None)
df_get.dropna(subset=['cmpryn'], inplace=True)

df_tem = pd.read_excel(r'C:\A_TEMPUS_project\Paul_Test_Repeat_PriorCaTherapies_Template.xlsx')




# Loop through the column names
for column_name in df_get.columns:
    
    if column_name == 'cmline(1)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 1
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(1)']
      cmtrt_1 = df_get['cmtrt_1(1)']
      cmtrtoth = df_get['cmtrtoth(1)']
      cmstdat = df_get['cmstdat(1)']
      cmongo = df_get['cmongo(1)']
      cmendat = df_get['cmendat(1)']
      cmdstxt	= df_get['cmdstxt(1)']
      cmtrtst1 = df_get['cmtrtst1(1)']
      cmbresp = df_get['cmbresp(1)']
      cmrespcf = df_get['cmrespcf(1)']
      cmrecurr = df_get['cmrecurr(1)']
      cmtxrpt	= df_get['cmtxrpt(1)']
      assoc_diag = df_get['assoc_diag(1)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data1 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'	 :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr, #original data is NA; to here is NaN and don't show in result file
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df1 = pd.DataFrame(data1)
       # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df1, ignore_index=True)
     
    if column_name == 'cmline(2)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 2
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(2)']
      cmtrt_1 = df_get['cmtrt_1(2)']
      cmtrtoth = df_get['cmtrtoth(2)']
      cmstdat = df_get['cmstdat(2)']
      cmongo = df_get['cmongo(2)']
      cmendat = df_get['cmendat(2)']
      cmdstxt	= df_get['cmdstxt(2)']
      cmtrtst1 = df_get['cmtrtst1(2)']
      cmbresp = df_get['cmbresp(2)']
      cmrespcf = df_get['cmrespcf(2)']
      cmrecurr = df_get['cmrecurr(2)']
      cmtxrpt	= df_get['cmtxrpt(2)']
      assoc_diag = df_get['assoc_diag(2)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data2 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'	 :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df2 = pd.DataFrame(data2)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df2, ignore_index=True)
    
    if column_name == 'cmline(3)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 3
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(3)']
      cmtrt_1 = df_get['cmtrt_1(3)']
      cmtrtoth = df_get['cmtrtoth(3)']
      cmstdat = df_get['cmstdat(3)']
      cmongo = df_get['cmongo(3)']
      cmendat = df_get['cmendat(3)']
      cmdstxt	= df_get['cmdstxt(3)']
      cmtrtst1 = df_get['cmtrtst1(3)']
      cmbresp = df_get['cmbresp(3)']
      cmrespcf = df_get['cmrespcf(3)']
      cmrecurr = df_get['cmrecurr(3)']
      cmtxrpt	= df_get['cmtxrpt(3)']
      assoc_diag = df_get['assoc_diag(3)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data3 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'	 :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df3 = pd.DataFrame(data3)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df3, ignore_index=True)

    if column_name == 'cmline(4)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 4
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(4)']
      cmtrt_1 = df_get['cmtrt_1(4)']
      cmtrtoth = df_get['cmtrtoth(4)']
      cmstdat = df_get['cmstdat(4)']
      cmongo = df_get['cmongo(4)']
      cmendat = df_get['cmendat(4)']
      cmdstxt	= df_get['cmdstxt(4)']
      cmtrtst1 = df_get['cmtrtst1(4)']
      cmbresp = df_get['cmbresp(4)']
      cmrespcf = df_get['cmrespcf(4)']
      cmrecurr = df_get['cmrecurr(4)']
      cmtxrpt	= df_get['cmtxrpt(4)']
      assoc_diag = df_get['assoc_diag(4)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data4 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'	 :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df4 = pd.DataFrame(data4)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df4, ignore_index=True)

    if column_name == 'cmline(5)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 5
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(5)']
      cmtrt_1 = df_get['cmtrt_1(5)']
      cmtrtoth = df_get['cmtrtoth(5)']
      cmstdat = df_get['cmstdat(5)']
      cmongo = df_get['cmongo(5)']
      cmendat = df_get['cmendat(5)']
      cmdstxt	= df_get['cmdstxt(5)']
      cmtrtst1 = df_get['cmtrtst1(5)']
      cmbresp = df_get['cmbresp(5)']
      cmrespcf = df_get['cmrespcf(5)']
      cmrecurr = df_get['cmrecurr(5)']
      cmtxrpt	= df_get['cmtxrpt(5)']
      assoc_diag = df_get['assoc_diag(5)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data5 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'	 :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df5 = pd.DataFrame(data5)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df5, ignore_index=True)

    if column_name == 'cmline(6)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 6
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(6)']
      cmtrt_1 = df_get['cmtrt_1(6)']
      cmtrtoth = df_get['cmtrtoth(6)']
      cmstdat = df_get['cmstdat(6)']
      cmongo = df_get['cmongo(6)']
      cmendat = df_get['cmendat(6)']
      cmdstxt	= df_get['cmdstxt(6)']
      cmtrtst1 = df_get['cmtrtst1(6)']
      cmbresp = df_get['cmbresp(6)']
      cmrespcf = df_get['cmrespcf(6)']
      cmrecurr = df_get['cmrecurr(6)']
      cmtxrpt	= df_get['cmtxrpt(6)']
      assoc_diag = df_get['assoc_diag(6)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data6 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'	 :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df6 = pd.DataFrame(data6)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df6, ignore_index=True)

    if column_name == 'cmline(7)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 7
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(7)']
      cmtrt_1 = df_get['cmtrt_1(7)']
      cmtrtoth = df_get['cmtrtoth(7)']
      cmstdat = df_get['cmstdat(7)']
      cmongo = df_get['cmongo(7)']
      cmendat = df_get['cmendat(7)']
      cmdstxt	= df_get['cmdstxt(7)']
      cmtrtst1 = df_get['cmtrtst1(7)']
      cmbresp = df_get['cmbresp(7)']
      cmrespcf = df_get['cmrespcf(7)']
      cmrecurr = df_get['cmrecurr(7)']
      cmtxrpt	= df_get['cmtxrpt(7)']
      assoc_diag = df_get['assoc_diag(7)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data7 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'	 :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df7 = pd.DataFrame(data7)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df7, ignore_index=True)

    if column_name == 'cmline(8)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 8
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(8)']
      cmtrt_1 = df_get['cmtrt_1(8)']
      cmtrtoth = df_get['cmtrtoth(8)']
      cmstdat = df_get['cmstdat(8)']
      cmongo = df_get['cmongo(8)']
      cmendat = df_get['cmendat(8)']
      cmdstxt = df_get['cmdstxt(8)']
      cmtrtst1 = df_get['cmtrtst1(8)']
      cmbresp = df_get['cmbresp(8)']
      cmrespcf = df_get['cmrespcf(8)']
      cmrecurr = df_get['cmrecurr(8)']
      cmtxrpt = df_get['cmtxrpt(8)']
      assoc_diag = df_get['assoc_diag(8)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data8 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df8 = pd.DataFrame(data8)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df8, ignore_index=True)

    if column_name == 'cmline(9)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 9
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(9)']
      cmtrt_1 = df_get['cmtrt_1(9)']
      cmtrtoth = df_get['cmtrtoth(9)']
      cmstdat = df_get['cmstdat(9)']
      cmongo = df_get['cmongo(9)']
      cmendat = df_get['cmendat(9)']
      cmdstxt = df_get['cmdstxt(9)']
      cmtrtst1 = df_get['cmtrtst1(9)']
      cmbresp = df_get['cmbresp(9)']
      cmrespcf = df_get['cmrespcf(9)']
      cmrecurr = df_get['cmrecurr(9)']
      cmtxrpt = df_get['cmtxrpt(9)']
      assoc_diag = df_get['assoc_diag(9)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data9 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df9 = pd.DataFrame(data9)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df9, ignore_index=True)

    if column_name == 'cmline(10)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 10
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(10)']
      cmtrt_1 = df_get['cmtrt_1(10)']
      cmtrtoth = df_get['cmtrtoth(10)']
      cmstdat = df_get['cmstdat(10)']
      cmongo = df_get['cmongo(10)']
      cmendat = df_get['cmendat(10)']
      cmdstxt = df_get['cmdstxt(10)']
      cmtrtst1 = df_get['cmtrtst1(10)']
      cmbresp = df_get['cmbresp(10)']
      cmrespcf = df_get['cmrespcf(10)']
      cmrecurr = df_get['cmrecurr(10)']
      cmtxrpt = df_get['cmtxrpt(10)']
      assoc_diag = df_get['assoc_diag(10)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data10 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df10 = pd.DataFrame(data10)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df10, ignore_index=True)

    if column_name == 'cmline(11)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 11
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(11)']
      cmtrt_1 = df_get['cmtrt_1(11)']
      cmtrtoth = df_get['cmtrtoth(11)']
      cmstdat = df_get['cmstdat(11)']
      cmongo = df_get['cmongo(11)']
      cmendat = df_get['cmendat(11)']
      cmdstxt = df_get['cmdstxt(11)']
      cmtrtst1 = df_get['cmtrtst1(11)']
      cmbresp = df_get['cmbresp(11)']
      cmrespcf = df_get['cmrespcf(11)']
      cmrecurr = df_get['cmrecurr(11)']
      cmtxrpt = df_get['cmtxrpt(11)']
      assoc_diag = df_get['assoc_diag(11)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data11 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df11 = pd.DataFrame(data11)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df11, ignore_index=True)

    if column_name == 'cmline(12)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 12
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(12)']
      cmtrt_1 = df_get['cmtrt_1(12)']
      cmtrtoth = df_get['cmtrtoth(12)']
      cmstdat = df_get['cmstdat(12)']
      cmongo = df_get['cmongo(12)']
      cmendat = df_get['cmendat(12)']
      cmdstxt = df_get['cmdstxt(12)']
      cmtrtst1 = df_get['cmtrtst1(12)']
      cmbresp = df_get['cmbresp(12)']
      cmrespcf = df_get['cmrespcf(12)']
      cmrecurr = df_get['cmrecurr(12)']
      cmtxrpt = df_get['cmtxrpt(12)']
      assoc_diag = df_get['assoc_diag(12)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data12 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df12 = pd.DataFrame(data12)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df12, ignore_index=True)

    if column_name == 'cmline(13)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 13
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(13)']
      cmtrt_1 = df_get['cmtrt_1(13)']
      cmtrtoth = df_get['cmtrtoth(13)']
      cmstdat = df_get['cmstdat(13)']
      cmongo = df_get['cmongo(13)']
      cmendat = df_get['cmendat(13)']
      cmdstxt = df_get['cmdstxt(13)']
      cmtrtst1 = df_get['cmtrtst1(13)']
      cmbresp = df_get['cmbresp(13)']
      cmrespcf = df_get['cmrespcf(13)']
      cmrecurr = df_get['cmrecurr(13)']
      cmtxrpt = df_get['cmtxrpt(13)']
      assoc_diag = df_get['assoc_diag(13)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data13 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df13 = pd.DataFrame(data13)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df13, ignore_index=True)

    if column_name == 'cmline(14)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 14
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(14)']
      cmtrt_1 = df_get['cmtrt_1(14)']
      cmtrtoth = df_get['cmtrtoth(14)']
      cmstdat = df_get['cmstdat(14)']
      cmongo = df_get['cmongo(14)']
      cmendat = df_get['cmendat(14)']
      cmdstxt = df_get['cmdstxt(14)']
      cmtrtst1 = df_get['cmtrtst1(14)']
      cmbresp = df_get['cmbresp(14)']
      cmrespcf = df_get['cmrespcf(14)']
      cmrecurr = df_get['cmrecurr(14)']
      cmtxrpt = df_get['cmtxrpt(14)']
      assoc_diag = df_get['assoc_diag(14)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data14 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df14 = pd.DataFrame(data14)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df14, ignore_index=True)

    if column_name == 'cmline(15)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 15
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(15)']
      cmtrt_1 = df_get['cmtrt_1(15)']
      cmtrtoth = df_get['cmtrtoth(15)']
      cmstdat = df_get['cmstdat(15)']
      cmongo = df_get['cmongo(15)']
      cmendat = df_get['cmendat(15)']
      cmdstxt = df_get['cmdstxt(15)']
      cmtrtst1 = df_get['cmtrtst1(15)']
      cmbresp = df_get['cmbresp(15)']
      cmrespcf = df_get['cmrespcf(15)']
      cmrecurr = df_get['cmrecurr(15)']
      cmtxrpt = df_get['cmtxrpt(15)']
      assoc_diag = df_get['assoc_diag(15)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data15 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df15 = pd.DataFrame(data15)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df15, ignore_index=True)

    if column_name == 'cmline(16)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 16
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(16)']
      cmtrt_1 = df_get['cmtrt_1(16)']
      cmtrtoth = df_get['cmtrtoth(16)']
      cmstdat = df_get['cmstdat(16)']
      cmongo = df_get['cmongo(16)']
      cmendat = df_get['cmendat(16)']
      cmdstxt = df_get['cmdstxt(16)']
      cmtrtst1 = df_get['cmtrtst1(16)']
      cmbresp = df_get['cmbresp(16)']
      cmrespcf = df_get['cmrespcf(16)']
      cmrecurr = df_get['cmrecurr(16)']
      cmtxrpt = df_get['cmtxrpt(16)']
      assoc_diag = df_get['assoc_diag(16)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data16 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df16 = pd.DataFrame(data16)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df16, ignore_index=True)


    if column_name == 'cmline(17)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 17
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(17)']
      cmtrt_1 = df_get['cmtrt_1(17)']
      cmtrtoth = df_get['cmtrtoth(17)']
      cmstdat = df_get['cmstdat(17)']
      cmongo = df_get['cmongo(17)']
      cmendat = df_get['cmendat(17)']
      cmdstxt = df_get['cmdstxt(17)']
      cmtrtst1 = df_get['cmtrtst1(17)']
      cmbresp = df_get['cmbresp(17)']
      cmrespcf = df_get['cmrespcf(17)']
      cmrecurr = df_get['cmrecurr(17)']
      cmtxrpt = df_get['cmtxrpt(17)']
      assoc_diag = df_get['assoc_diag(17)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data17 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df17 = pd.DataFrame(data17)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df17, ignore_index=True)

    if column_name == 'cmline(18)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 18
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(18)']
      cmtrt_1 = df_get['cmtrt_1(18)']
      cmtrtoth = df_get['cmtrtoth(18)']
      cmstdat = df_get['cmstdat(18)']
      cmongo = df_get['cmongo(18)']
      cmendat = df_get['cmendat(18)']
      cmdstxt = df_get['cmdstxt(18)']
      cmtrtst1 = df_get['cmtrtst1(18)']
      cmbresp = df_get['cmbresp(18)']
      cmrespcf = df_get['cmrespcf(18)']
      cmrecurr = df_get['cmrecurr(18)']
      cmtxrpt = df_get['cmtxrpt(18)']
      assoc_diag = df_get['assoc_diag(18)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data18 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df18 = pd.DataFrame(data18)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df18, ignore_index=True)

    if column_name == 'cmline(19)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 19
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(19)']
      cmtrt_1 = df_get['cmtrt_1(19)']
      cmtrtoth = df_get['cmtrtoth(19)']
      cmstdat = df_get['cmstdat(19)']
      cmongo = df_get['cmongo(19)']
      cmendat = df_get['cmendat(19)']
      cmdstxt = df_get['cmdstxt(19)']
      cmtrtst1 = df_get['cmtrtst1(19)']
      cmbresp = df_get['cmbresp(19)']
      cmrespcf = df_get['cmrespcf(19)']
      cmrecurr = df_get['cmrecurr(19)']
      cmtxrpt = df_get['cmtxrpt(19)']
      assoc_diag = df_get['assoc_diag(19)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data19 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df19 = pd.DataFrame(data19)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df19, ignore_index=True)

    if column_name == 'cmline(20)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 20
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(20)']
      cmtrt_1 = df_get['cmtrt_1(20)']
      cmtrtoth = df_get['cmtrtoth(20)']
      cmstdat = df_get['cmstdat(20)']
      cmongo = df_get['cmongo(20)']
      cmendat = df_get['cmendat(20)']
      cmdstxt = df_get['cmdstxt(20)']
      cmtrtst1 = df_get['cmtrtst1(20)']
      cmbresp = df_get['cmbresp(20)']
      cmrespcf = df_get['cmrespcf(20)']
      cmrecurr = df_get['cmrecurr(20)']
      cmtxrpt = df_get['cmtxrpt(20)']
      assoc_diag = df_get['assoc_diag(20)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data20 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df20 = pd.DataFrame(data20)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df20, ignore_index=True)

    if column_name == 'cmline(21)':
      record_id = df_get['record_id']
      redcap_event_name ='baseline_g1_arm_1'
      redcap_repeat_instrument = 'prior_cancer_therapies'
      repeat_Time = 21
      cmpryn = df_get['cmpryn'] 
      cmline = df_get['cmline(21)']
      cmtrt_1 = df_get['cmtrt_1(21)']
      cmtrtoth = df_get['cmtrtoth(21)']
      cmstdat = df_get['cmstdat(21)']
      cmongo = df_get['cmongo(21)']
      cmendat = df_get['cmendat(21)']
      cmdstxt = df_get['cmdstxt(21)']
      cmtrtst1 = df_get['cmtrtst1(21)']
      cmbresp = df_get['cmbresp(21)']
      cmrespcf = df_get['cmrespcf(21)']
      cmrecurr = df_get['cmrecurr(21)']
      cmtxrpt = df_get['cmtxrpt(21)']
      assoc_diag = df_get['assoc_diag(21)']
      prior_cancer_therapies_complete = df_get['prior_cancer_therapies_complete']
      data21 = {
         'record_id' : record_id,
         'redcap_event_name' : redcap_event_name,
         'redcap_repeat_instrument' : redcap_repeat_instrument,
         'redcap_repeat_instance' : repeat_Time,
         'cmpryn' : cmpryn, 
         'cmline' : cmline,
         'cmtrt_1' : cmtrt_1,
         'cmtrtoth' :cmtrtoth,
         'cmstdat' : cmstdat,
         'cmongo' : cmongo,
         'cmendat' : cmendat,
         'cmdstxt'   :  cmdstxt,
         'cmtrtst1' : cmtrtst1,
         'cmbresp' : cmbresp,
         'cmrespcf' : cmrespcf,
         'cmrecurr' : cmrecurr,
         'cmtxrpt' : cmtxrpt,
         'assoc_diag' : assoc_diag,
         'prior_cancer_therapies_complete' : prior_cancer_therapies_complete

         
             }
      original_df21 = pd.DataFrame(data21)
        # Insert data from the original DataFrame into the empty DataFrame
      df_tem = df_tem.append(original_df21, ignore_index=True)


df_tem.to_excel(r'C:\A_TEMPUS_project\Forms_workOn\Repeat_PriorCaTherapies_Data_Template.xlsx', index=False)
print('Pre-Done! still working...')


# Load the Excel file into a DataFrame to another filnal data clean
df_clean = pd.read_excel(r'C:\A_TEMPUS_project\Forms_workOn\Repeat_PriorCaTherapies_Data_Template.xlsx')

#need clean data here:
#remove "not available"
condition_col_cmpryn = df_clean['cmpryn'] == 'not_available'
# Filter the DataFrame to exclude rows where 'cmpryn' is 'not_available'
df_clean = df_clean[~condition_col_cmpryn]


# Change the value in cell if it equals 'V5_2' to '2'
df_clean.loc[df_clean['prior_cancer_therapies_complete'] == 'V4.1_8', 'prior_cancer_therapies_complete'] = '2'
df_clean.loc[df_clean['prior_cancer_therapies_complete'] == 'V4.1_2', 'prior_cancer_therapies_complete'] = '2'
df_clean.loc[df_clean['prior_cancer_therapies_complete'] == 'V4_8', 'prior_cancer_therapies_complete'] = '2'
df_clean.loc[df_clean['prior_cancer_therapies_complete'] == 'V5_2', 'prior_cancer_therapies_complete'] = '2'
df_clean.loc[df_clean['prior_cancer_therapies_complete'] == 'V5_6', 'prior_cancer_therapies_complete'] = '2'
df_clean.loc[df_clean['cmtxrpt'] == 'TRUE', 'cmtxrpt'] = '1'
df_clean.loc[df_clean['cmtxrpt'] == 'FALSE', 'cmtxrpt'] = '0'
df_clean.loc[df_clean['cmongo'] == 'TRUE', 'cmongo'] = '1'
df_clean.loc[df_clean['cmongo'] == 'FALSE', 'cmongo'] = '0'



df_clean.to_excel(r'C:\A_TEMPUS_project\Forms_workOn\Repeat_PriorCaTherapies_Data_Cleaned.xlsx', index=False)

df_removeR = pd.read_excel(r'C:\A_TEMPUS_project\Forms_workOn\Repeat_PriorCaTherapies_Data_Cleaned.xlsx')


#need remove empty reows by some conditions.

# Combine the conditions using the logical AND operator
#since don't know columns's data type, so asign str type to thme (here is tricky )

df_removeR['cmline'] = df_removeR['cmline'].astype(str)
df_removeR['cmtrt_1'] = df_removeR['cmtrt_1'].astype(str)


# Define the condition to filter rows
condition_empty_cols = (df_removeR['cmline'] == 'nan') & (df_removeR['cmtrt_1'] == 'nan')
# Use the combined condition to filter the DataFrame and remove rows that meet all the conditions
df_removeR = df_removeR[~condition_empty_cols]

#replace {null} to '' so that data canbe load in RedCap
df_removeR.replace('{null}', '', inplace=True)

#since find cmtrt_1 =nan after did above, need remove it 
df_removeR.replace('nan', '', inplace=True)

df_removeR.to_excel(r'C:\A_TEMPUS_project\Forms_workOn\Repeat_PriorCaTherapies_Data_Cleaned1.xlsx', index=False)

#test many ways to change true to 1 and false to 0. but all failed
#make another py to try


#-------------------------------------------
df_iden = pd.read_excel(r'C:\A_TEMPUS_project\Forms_workOn\Repeat_PriorCaTherapies_Data_Cleaned1.xlsx')

time.sleep(5)
df_iden.to_csv(r'C:\A_TEMPUS_project\Forms_workOn\Repeat_PriorCaTherapies_Data_Cleaned1_1.txt', sep="\t",index=False)

time.sleep(5)

df = pd.read_csv(r'C:\A_TEMPUS_project\Forms_workOn\Repeat_PriorCaTherapies_Data_Cleaned1_1.txt', sep="\t")
df.replace({True: 1, False: 0}, inplace=True)

df.to_excel(r'C:\A_TEMPUS_project\Forms_workOn\Repeat_PriorCaTherapies_Data_Cleaned1_1Final.xlsx', index=False)
print('Final-Done!')











   
