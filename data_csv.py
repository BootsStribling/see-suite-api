#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


# ## Dictionaries

# In[ ]:


comm_names = {
    'Manager Community 8':'Cerca-la-Source Community Manager',
    'Entrepreneur Community 8':'Cerca-la-Source Entrepreneur Community',
    'Manager Community 9':'Mombin Crochus Community Manager',
    'Entrepreneur Community 9':'Mombin Crochus Entrepreneur Community',
    'Manager Community 10':'Pignon Community Manager',
    'Entrepreneur Community 10':'Pignon Entrepreneur Community',
    'Manager Community 11':'Lavictoire Community Manager',
    'Entrepreneur Community 11':'Lavictoire Entrepreneur Community',
    'Manager Community 12':'Hinche Community Manager',
    'Entrepreneur Community 12':'Hinche Entrepreneur Community',
    'Manager Community 13':'Cerca-Carvajal Community Manager',
    'Entrepreneur Community 13':'Cerca-Carvajal Entrepreneur Community',
    'Manager Community 14':'St-Raphael Community Manager',
    'Entrepreneur Community 14':'St-Raphael Entrepreneur Community',
    'Manager Community 15':'St.Michel Community Manager',
    'Entrepreneur Community 15':'St.Michel Entrepreneur Community',
    'Manager Community 16':'Bois De Lorence Community Manager',
    'Entrepreneur Community 16':'Bois De Lorence Entrepreneur Community',
    'Manager Community 18':'Lascahobas Community Manager',
    'Entrepreneur Community 18':'Lascahobas Entrepreneur Community',
    'Manager Community 19':'Dondon Community Manager',
    'Entrepreneur Community 19':'Dondon Entrepreneur Community',
    'Manager Community 20':'Ranquitte Community Manager',
    'Entrepreneur Community 20':'Ranquitte Entrepreneur Community',
    'Manager Community 21':'Jean Denis Community Manager',
    'Entrepreneur Community 21':'Jean Denis Entrepreneur Community',
    'Manager Community 22':'Deschapelle Community Manager',
    'Entrepreneur Community 22':'Deschapelle Entrepreneur Community',
}


# In[ ]:


comm_num = {
    'Manager Community 7': 'm',

}


# In[ ]:


col_names = {
    
}


# ## Sales Dataframe

# In[2]:


sales = pd.read_csv('./api/data/cash_data_test.csv')


# In[3]:


sales.columns = sales.iloc[0]
sales = sales.iloc[1:, :]
sales.head()


# In[4]:


sales['startDate'] = pd.to_datetime(sales['startDate'], format='%Y-%m-%d')
sales['startDate']


# In[5]:


sales['endDate'] = pd.to_datetime(sales['endDate'], format='%Y-%m-%d')
sales['endDate']


# In[24]:


sales.shape


# In[6]:


sales['Mobile User'].value_counts()


# In[64]:


sales['product_name'].value_counts()


# In[11]:


total_sales = sales[['Mobile User', 'deposit_amount_expected', 'montan_depoze_deposit_amount',
                    'payment_expected', 'cash_payment_amount']]
total_sales.head()


# In[20]:


total_sales.shape


# In[19]:


# sales.to_json('../data/sales_in_json')


# ## Loans Dataframe

# In[7]:


# loans = pd.read_csv('../data/TWSupport Loan Repayments (v5)_1_2426.csv')


# In[8]:


# loans.columns = loans.iloc[0]
# loans = loans.iloc[1:, :]
# loans.head()


# In[9]:


# loans.shape


# # In[10]:


# loans['Mobile User'].value_counts()


# # In[39]:


# loans['startDate'] = pd.to_datetime(loans['startDate'], format='%Y-%m-%d')
# loans['startDate']


# In[40]:


# loans['endDate'] = pd.to_datetime(loans['endDate'], format='%Y-%m-%d')
# loans['endDate']


# # ### DF using only loans and user

# # In[12]:


# total_loans = loans[['Mobile User', 'amount_owed', 'montan_peman_an_amount_paid']]
# total_loans.head()


# # In[21]:


# total_loans.shape


# ### Trying to separate loans by year

# In[42]:


# loans_2021 = loans[loans['startDate'].dt.year == 2021]
# loans_2021.shape


# # In[45]:


# loans_2021


# # In[51]:


# # Year 2021 Quarter 1
# loans_2021_q1 = loans_2021[loans_2021['startDate'].dt.quarter == 1]
# loans_2021_q1.shape


# In[59]:


# loans_2021_q1['Mobile User'].value_counts()


# # In[52]:


# # Year 2021 Quarter 2
# loans_2021_q2 = loans_2021[loans_2021['startDate'].dt.quarter == 2]
# loans_2021_q2.shape


# # In[58]:


# loans_2021_q2['Mobile User'].value_counts()


# # In[53]:


# # Year 2021 Quarter 3
# loans_2021_q3 = loans_2021[loans_2021['startDate'].dt.quarter == 3]
# loans_2021_q3.shape


# In[56]:


# loans_2021_q3['Mobile User'].value_counts()


# # In[54]:


# # Year 2021 Quarter 2
# loans_2021_q4 = loans_2021[loans_2021['startDate'].dt.quarter == 4]
# loans_2021_q4.shape


# # In[57]:


# loans_2021_q4['Mobile User'].value_counts()


# # In[43]:


# loans_2022 = loans[loans['startDate'].dt.year == 2022]
# loans_2022.shape


# In[60]:


# Year 2022 Quarter 1
# loans_2022_q1 = loans_2022[loans_2022['startDate'].dt.quarter == 1]
# loans_2022_q1.shape


# # In[62]:


# loans_2022_q1['Mobile User'].value_counts()


# # In[61]:


# # Year 2022 Quarter 2
# loans_2022_q2 = loans_2022[loans_2022['startDate'].dt.quarter == 2]
# loans_2022_q2.shape


# In[63]:


# loans_2022_q2['Mobile User'].value_counts()


# ### Attempt to merge the Total sales and loans

# In[29]:


# total_sales_and_loans = pd.merge(total_loans, total_sales, how='inner')


# In[30]:


# total_sales_and_loans.head()


# In[31]:


# total_sales_and_loans['Mobile User'].value_counts()


# In[32]:


# total_sales_and_loans.shape


# # By Product

# ## Water Filter

# In[68]:


water_filter_cash = sales[sales['product_name'] == 'Sistèm Filtraj ak Pye / Filter']
water_filter_cash['Mobile User'].value_counts()


# In[70]:


entrepreneur_filter_cash = sales[sales['product_name'] == 'Antreprenè Sistèm Filtraj ak Pye / Entrepreneur Filter']
entrepreneur_filter_cash['Mobile User'].value_counts()


# In[71]:


stove_cash = sales[sales['product_name'] == 'Recho / Stove']
stove_cash['Mobile User'].value_counts()


# # Export to PostgresSQL

# In[72]:


from sqlalchemy import create_engine

engine = create_engine(f'postgresql://localhost:5432/iaapi')

connection = engine.connect()

sales.to_sql('transactions', connection, if_exists='replace', index=False, chunksize=10)


# In[ ]:





# In[ ]:


# import psycopg2 #import the postgres library
# from datetime import datetime

# Create while loop to keep running: 
# while True:

#connect to the database
# conn = psycopg2.connect(host='127.0.0.1', dbname='iaapi',
#                        user='haziqnaeem',
# #                        password='****',
#                        port='5432')  
# #create a cursor object 
# #cursor object is used to interact with the database
# cur = conn.cursor()

# #create table with same headers as csv file
# for j, i in df[[list_of_columns]].iterrows():
#     cur.execute("""
#     INSERT INTO table (column_name, column_name, column_name)
#     VALUES (%s, %s, %s);
#     """,
#     (i[column_1], i[column_2], i[column_3])) # insert the table that we want from the csv


# #Commit Changes
# conn.commit()
# #Close connection
# conn.close()
    
    
# # add a sleep function: 
# if datetime.now() % 3600 == 0:
#     # run SQL querry
# # else:
#     # Pass

