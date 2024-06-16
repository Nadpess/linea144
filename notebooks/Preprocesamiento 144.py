#!/usr/bin/env python
# coding: utf-8

# ## Se importan las librerías

# In[1]:


import numpy as np
import pandas as pd


# ## Se cargan los dataframes

# In[2]:


data_2020 = pd.read_csv(r'C:\Users\nadpe\OneDrive\Documentos\Tec. Datos\Aprendizaje automático\linea144\Data\external\linea144-2020.csv')
data_2020.head(10)


# In[3]:


data_2020.shape


# In[4]:


data_2021 = pd.read_csv(r'C:\Users\nadpe\OneDrive\Documentos\Tec. Datos\Aprendizaje automático\linea144\Data\external\linea144-2021.csv')
data_2021.head(10)


# In[5]:


data_2021.shape


# In[6]:


data_2022 = pd.read_csv(r'C:\Users\nadpe\OneDrive\Documentos\Tec. Datos\Aprendizaje automático\linea144\Data\external\linea144-enero-diciembre-2022.csv')
data_2022.head(10)


# In[7]:


data_2022.shape


# In[8]:


data_2023 = pd.read_csv(r'C:\Users\nadpe\OneDrive\Documentos\Tec. Datos\Aprendizaje automático\linea144\Data\external\linea144-enero-junio-2023.csv')
data_2023.head(10)


# In[ ]:





# In[9]:


data_2023.shape


# ## Se unen los dataframes

# In[10]:


data_total = pd.concat([data_2020, data_2021, data_2022, data_2023])
data_total.head(10)


# In[11]:


data_total.shape
data_total.info()


# ## Se limpia el data frame

# In[12]:


data_total = data_total.drop(["Unnamed: 19"], axis = 1)
#Se elimina una columna que estaba vacía


# In[13]:


data_total.info()
#Se observa que en la unión se han duplicado las columnas de fecha por tener distinto nombre.


# In[16]:


data_total.tail(40)
#Se comprueba la duplicación de columnas de fecha. Corresponden a las últimas cargadas.


# In[17]:


data_total['fecha'].fillna(data_total['Fecha'], inplace=True)
data_total.tail(40)


# In[19]:


data_total = data_total.drop(["Fecha"], axis = 1) 
data_total.info()
#Se elimina la columna Fecha y se chequea que estén la totalidad de los datos dispuestos en la varible fecha

