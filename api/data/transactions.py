#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


sales = pd.read_csv('../data/Trans_TWSupport Sale w. Cash Discount (v15)_1_935.csv')
loans = pd.read_csv('../data/TWSupport Loan Repayments (v5)_1_2426.csv')


# ## Dictionaries

# In[52]:


manager_id = {
    'Manager Community 7':'m',
    'Entrepreneur Community 7':'e',
    'Manager Community 8':'m',
    'Entrepreneur Community 8':'e',
    'Manager Community 9':'m',
    'Entrepreneur Community 9':'e',
    'Manager Community 10':'m',
    'Entrepreneur Community 10':'e',
    'Manager Community 11':'m',
    'Entrepreneur Community 11':'e',
    'Manager Community 12':'m',
    'Entrepreneur Community 12':'e',
    'Manager Community 13':'m',
    'Entrepreneur Community 13':'e',
    'Manager Community 14':'m',
    'Entrepreneur Community 14':'e',
    'Manager Community 15':'m',
    'Entrepreneur Community 15':'e',
    'Manager Community 16':'m',
    'Entrepreneur Community 16':'e',
    'Manager Community 18':'m',
    'Entrepreneur Community 18':'e',
    'Manager Community 19':'m',
    'Entrepreneur Community 19':'e',
    'Manager Community 20':'m',
    'Entrepreneur Community 20':'e',
    'Manager Community 21':'m',
    'Entrepreneur Community 21':'e',
    'Manager Community 22':'m',
    'Entrepreneur Community 22':'e',
    'Manager Community 23':'m',
    'Entrepreneur Community 23':'e',
    'Manager Community 25':'m',
    'Entrepreneur Community 25':'e',
    'Manager Community 26':'m',
    'Entrepreneur Community 26':'e',
    'Manager Community 28':'m',
    'Entrepreneur Community 28':'e',
    'Manager Community 29':'m',
    'Entrepreneur Community 29':'e',
    'Manager Community 30':'m',
    'Entrepreneur Community 30':'e',
    'Manager Community 32':'m',
    'Entreprneuer Community 32':'e',
    'Manager Community 33':'m',
    'Entreprneuer Community 33':'e',
    'Manager Community 34':'m',
    'Entreprneuer Community 34':'e',
    'Manager Community 35':'m',
    'Entreprneuer Community 35':'e',
    'Manager Community 36':'m',
    'Entreprneuer Community 36':'e',
    'Manager Community 37':'m',
    'Entreprneuer Community 37':'e'
}


# In[53]:


community_id = {
    'Manager Community 7':7,
    'Entrepreneur Community 7':7,
    'Manager Community 8':8,
    'Entrepreneur Community 8':8,
    'Manager Community 9':9,
    'Entrepreneur Community 9':9,
    'Manager Community 10':10,
    'Entrepreneur Community 10':10,
    'Manager Community 11':11,
    'Entrepreneur Community 11':11,
    'Manager Community 12':12,
    'Entrepreneur Community 12':12,
    'Manager Community 13':13,
    'Entrepreneur Community 13':13,
    'Manager Community 14':14,
    'Entrepreneur Community 14':14,
    'Manager Community 15':15,
    'Entrepreneur Community 15':15,
    'Manager Community 16':16,
    'Entrepreneur Community 16':16,
    'Manager Community 18':18,
    'Entrepreneur Community 18':18,
    'Manager Community 19':19,
    'Entrepreneur Community 19':19,
    'Manager Community 20':20,
    'Entrepreneur Community 20':20,
    'Manager Community 21':21,
    'Entrepreneur Community 21':21,
    'Manager Community 22':22,
    'Entrepreneur Community 22':22,
    'Manager Community 23':23,
    'Entrepreneur Community 23':23,
    'Manager Community 25':25,
    'Entrepreneur Community 25':25,
    'Manager Community 26':26,
    'Entrepreneur Community 26':26,
    'Manager Community 28':28,
    'Entrepreneur Community 28':28,
    'Manager Community 29':29,
    'Entrepreneur Community 29':29,
    'Manager Community 30':30,
    'Entrepreneur Community 30':30,
    'Manager Community 32':32,
    'Entreprneuer Community 32':32,
    'Manager Community 33':33,
    'Entreprneuer Community 33':33,
    'Manager Community 34':34,
    'Entreprneuer Community 34':34,
    'Manager Community 35':35,
    'Entreprneuer Community 35':35,
    'Manager Community 36':36,
    'Entreprneuer Community 36':36,
    'Manager Community 37':37,
    'Entreprneuer Community 37':37
}


# ## Sales

# In[3]:


sales.columns = sales.iloc[0]
sales = sales.iloc[1:, :]
sales.head()


# In[4]:


sales.dtypes


# In[5]:


# sales.drop(sales.index[sales['Mobile User'] == 'Bedrige Pierre'], inplace=True)
sales.drop(sales.index[sales['Mobile User'] == 'Bedrige Pierre'], inplace=True)
sales.drop(sales.index[sales['Mobile User'] == 'Ernso Sylvain'], inplace=True)
sales.drop(sales.index[sales['Mobile User'] == 'Fenson Cherenfant'], inplace=True)
sales.drop(sales.index[sales['Mobile User'] == 'Mobile Test'], inplace=True)
sales.drop(sales.index[sales['Mobile User'] == 'UC TaroWorks Admin'], inplace=True)


# In[70]:


sales['cash_total'] = sales['cash_payment_amount']
sales_total = sales[['Mobile User', 'cash_total']]


# In[71]:


sales_total['cash_total'] = sales_total['cash_total'].astype(float).fillna(0)


# In[72]:


sales_total.dtypes


# In[73]:


sales_total = sales_total.groupby(['Mobile User']).sum()


# In[74]:


sales_total


# ## Loans

# In[10]:


loans.columns = loans.iloc[0]
loans = loans.iloc[1:, :]


# In[22]:


loans.drop(loans.index[loans['Mobile User'] == 'Bedrige Pierre'], inplace=True)
loans.drop(loans.index[loans['Mobile User'] == 'Ernso Sylvain'], inplace=True)
loans.drop(loans.index[loans['Mobile User'] == 'Fenson Cherenfant'], inplace=True)
loans.drop(loans.index[loans['Mobile User'] == 'Mobile Test'], inplace=True)
loans.drop(loans.index[loans['Mobile User'] == 'UC TaroWorks Admin'], inplace=True)
loans.drop(loans.index[loans['Mobile User'] == 'Hinche Intern 3'], inplace=True)
loans.drop(loans.index[loans['Mobile User'] == 'Hinche Office'], inplace=True)


# In[23]:


loans # Combine amount owed and amount paid into total loan amount


# In[24]:


loans['montan_peman_an_amount_paid'].value_counts()


# In[25]:


loans['amount_owed'] = loans['amount_owed'].astype(float).fillna(0)
loans['montan_peman_an_amount_paid'] = loans['montan_peman_an_amount_paid'].astype(float).fillna(0)


# In[65]:


sum_column = loans['amount_owed'] + loans['montan_peman_an_amount_paid']
loans['loan_total'] = sum_column
loans['loan_total']


# In[66]:


total_loans = loans[['Mobile User', 'loan_total']]
total_loans = total_loans.groupby('Mobile User').sum()
total_loans


# In[75]:


transactions = pd.merge(sales_total, total_loans, on='Mobile User', how='outer')
transactions.reset_index(inplace=True)
transactions['community_id'] = transactions['Mobile User'].map(community_id)
transactions['manager'] = transactions['Mobile User'].map(manager_id)
transactions.drop([5,8,18,21,40], axis=0, inplace=True)
transactions = transactions.fillna(0)


# In[76]:


transactions['community_id'] = transactions['community_id'].astype(int)


# In[78]:


transaction_sum = transactions['cash_total'] + transactions['loan_total']
transactions['transaction_total'] = transaction_sum


# In[79]:


transactions


# In[ ]:




