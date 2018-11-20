
#!/usr/bin/env python
# coding: utf-8

# SCiPy:
#     We have a min and max temprature in a city in india for each months of the year .We would like to find a function to describe this and show it graphically, the dataset given below .
#     Task:
#         1. fitting it to the periodic function
#         2. plot the fit
#     Data:
#         Max=39,41,43,47,49,51,45,38,37,29,27,25
#         Min=21,23,27,28,32,35,31,28,21,19,17,18

# In[46]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[48]:


months=np.arange(12)


# In[55]:


Max_temp=np.array([39,41,43,47,49,51,45,38,37,29,27,25])
Min_temp=np.array([21,23,27,28,32,35,31,28,21,19,17,18])


# In[56]:


plt.plot(months,Max_temp)
plt.plot(months,Min_temp)
plt.xlabel('months')
plt.ylabel('Max and Min Temprature')


# 1. fitting it to a periodic function

# In[57]:


from scipy import optimize
def yearly_temps(times, avg, ampl, time_offset):
    return (avg + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))

res_max, cov_max = optimize.curve_fit(yearly_temps, months,Max_temp, [20, 10, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months,Min_temp, [-40, 20, 0])


#         2. plot the fit


days = np.linspace(0, 12, num=365)

plt.figure()
plt.plot(months, Max_temp, 'ro')
plt.plot(days, yearly_temps(days, *res_max), 'r-')
plt.plot(months, Min_temp, 'bo')
plt.plot(days, yearly_temps(days, *res_min), 'b-')
plt.xlabel('Month')
plt.ylabel('Temperature ($^\circ$C)')

plt.show()


# matplotlib:
#     1. create a pie chart presenting the male/female proportion
#     2. create a scatterplot with the Fare paid and the age, differ the plot color by gender

# In[69]:


import pandas as pd
titanic=pd.read_csv("https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv")
titanic.info()


# 1.create a pie chart presenting the male/female proportion

# In[70]:


titanic.sex.value_counts().plot(kind='pie')
plt.axis('equal')
plt.title('Male and Female proportion')


# 2. create a scatterplot with the Fare paid and the age, differ the plot color by gender


titanic=titanic.dropna(subset=['sex'])

mapping={'male':'blue','female':'red'}

plt.scatter(titanic['age'],titanic['fare'],alpha=0.5,c=titanic['sex'].map(mapping))




