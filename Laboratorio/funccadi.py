#!/usr/bin/env python
# coding: utf-8

# In[12]:


def pendiente(x1, y1, x2 = 0, y2 = 0):
    '''Definimos la función pendiente para calculkar la pendiente dadas 
   las coordenadas de dos puntos. La función puede recibir las coordenadas 
   del primer punto y omitir las del segundo que sería considerado como el punto (0,0)
    Ejemplo: 
    >>> pendiente(2,3,7,4) = 0.2 
    Ejemplo: 
    >>> pendiente(5,4) = 0.8 '''
    #Calculamos la pendiente, utilizando la fórmula
    m = (y2 - y1) / (x2 - x1)
 
    #Regresamos el valor de la pendiente 
    return m


# In[14]:


def distancia(x1, y1, x2=0, y2=0): #Definimos la funcion con el nombre de distancia con sus 4 atributos
    ''' Esta funcion mide la distancia que existe entre un punto A y un punto B definidos por "x" y "y" 
    Ejemplo:
    >>>distancia(1, 2, 1, 0)'''
    d = pow(((x2-x1)*2)+((y2-y1)*2),0.5) #Declaramos la variable d como el resultado de la raiz cuadrada de x2-x1 **2 + y1-y2 **2
    return d #Regresamos el valor de d


# In[ ]:




