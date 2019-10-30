#!/usr/bin/env python
# coding: utf-8

# In[42]:


def inversa(cadena):
    '''
    Esta función recibe una cadena como argumento y devuelve esa cadena pero invertida.
    
    Ejemplo 1:
    >>> inversa('oscar') = 'racso'
    
    Ejemplo 2:
    >>> inversa('oscar es mi nombre') = 'erbmon im se racso'
    '''
    rev = ''
    for i in range(len(cadena)):
        rev += cadena[- i - 1]
    return rev

