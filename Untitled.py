


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt





dataset = sns.load_dataset("tips")


# In[3]:


dataset.head(2)


# In[12]:


print(dataset['size'].sum())


# In[10]:


sns.barplot(x = "day",y="size",data=dataset,estimator="sum",errorbar=("ci",0))
plt.savefig("Days wise no of people.jpg")
plt.show()


# In[9]:


sns.lineplot(x = "total_bill",y = "tip",data=dataset,errorbar=("ci",0))
plt.savefig("total bill vs tips .jpg")
plt.show()


# In[7]:


sns.barplot(x = "sex",y="size",data=dataset,estimator="sum",errorbar=("ci",0))
plt.savefig("total no of male and female.jpg")
plt.show()


# In[ ]:




