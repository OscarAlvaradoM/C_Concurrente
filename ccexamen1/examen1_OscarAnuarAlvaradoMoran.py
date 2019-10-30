#!/usr/bin/env python
# coding: utf-8

# In[2]:


import multiprocessing as mp


# # Programa 1

# ### Realiza el programa *programa1* que instancie tres procesos. Cada uno de los procesos hijos recibirá un valor n y un caracter s enviados por el proceso padre, los procesos escribirán en la salida estándar n veces el caracter s.

# In[6]:


def Imprimir(n, s):
    '''
    Esta función imprime n veces el caracter s, además muestra los datos enumerados.
    '''
    for idx, i in enumerate(range(n)): #Ciclo for que hace el trabajo
        print(idx, s)

def Hijos(n,s):
    '''
    Esta función crea hijos desde un proceso Padre y les asigna lo que tiene que hacer cada uno. Los inicializa también.
    '''
    Hijo1 = mp.Process(target = Imprimir, args = (n[0], s[0])) # Primer hijo
    Hijo2 = mp.Process(target = Imprimir, args = (n[1], s[1])) # Segundo hijo
    Hijo3 = mp.Process(target = Imprimir, args = (n[2], s[2])) # Tercer hijo
                       
    Hijo1.start()
    Hijo2.start()
    Hijo3.start()
                 
    Hijo1.join()
    Hijo2.join()
    Hijo3.join()
            
n = [4, 8, 16]
s = ['s1', 's2', 's3']

Padre = mp.Process(target = Hijos, args = (n,s))
Padre.start()
Padre.join()


# # Programa 2

# ### Refactoriza (reescribe) el programa anterior y elabora el programa2 donde construyas un mecanismo de sincronización el cual permita escribir en orden todos los caracteres de cada proceso. Es decir que se obtenga la secuencia s<sub>1</sub> ... s<sub>1</sub>, s<sub>2</sub> ... s<sub>2</sub>, s<sub>3</sub> ... s<sub>3</sub> donde cada s<sub>i</sub> ... s<sub>i</sub> para cada i = 1, 2, 3 es la secuencia de caracteres del proceso<sub>i</sub> con longitud n<sub>i</sub> 

# In[5]:


def Imprimir(n, s, turno_fijo):
    '''
    Esta función imprime n veces el caracter s, además muestra los datos enumerados. Se implementa aquí la utilización de 
    turnos y de bandera.
    '''
    bandera = 0
    while bandera != 1:
        while turno.value == turno_fijo:
            for idx, i in enumerate(range(n)):
                print(idx, s)
            turno.value = turno.value + 1
            bandera = bandera + 1

def Hijos(n, s):
    '''
    Esta función crea hijos desde un proceso Padre y les asigna lo que tiene que hacer cada uno. Los inicializa también.
    '''
    Hijo1 = mp.Process(target = Imprimir, args = (n[0], s[0], 0))
    Hijo2 = mp.Process(target = Imprimir, args = (n[1], s[1], 1))
    Hijo3 = mp.Process(target = Imprimir, args = (n[2], s[2], 2))

    Hijo1.start()
    Hijo2.start()
    Hijo3.start()         

n = [4, 8, 16] # Vector con los valores de n distintos para cada proceso
s = ['s1', 's2', 's3'] # Vector con los caracteres distintos para cada proceso
turno = mp.Value('i', 0) #Inicializo los turnos como variable compartida.
Padre = mp.Process(target = Hijos, args = (n, s))
Padre.start()
Padre.join()


# In[ ]:




