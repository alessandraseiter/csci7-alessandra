#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Display whether the current year is a leap year
year = 2020
if year % 400 == 0:
    print('2020 is a leap year')
elif year % 4 == 0 and year % 100 != 0:
    print('2020 is a leap year')
else:
    print('2020 is not a leap year')


# In[ ]:




