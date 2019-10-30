#!/usr/bin/env python
# coding: utf-8

# # Multiprocessing

# Este es un ejemplo básico del uso del módulo `multiprocessing` de Python

# ## Versión secuencial

# In[1]:


def sqr(num):
    res = num * num
    print(f"El cuadrado del número {num} es {res}.")


# In[2]:


numeros = [2, 4, 6, 8]

for numero in numeros:
    sqr(numero)
    


# ## Versión concurrente

# In[3]:


import os
from multiprocessing import Process, current_process


# In[4]:


def square(num):
    res = num * num
    
    proceso_Id = os.getpid()
    print(f"Id del proceso: {proceso_Id}")
    
    print(f"El cuadrado del número {num} es {res}.")
    


# In[7]:


procesos = []
numeros = [2, 4, 6, 8]

for numero in numeros:
    proceso = Process(target=square, args=(numero,))
    procesos.append(proceso)
    
    proceso.start() 
    


# In[ ]:




