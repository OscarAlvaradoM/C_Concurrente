#!/usr/bin/env python
# coding: utf-8

# # Multiprocessing

# `multiprocessing` es un paquete de python que permite la generación de  procesos, ofrece concurrencia local como remota.

# In[2]:


import multiprocessing as mp
from multiprocessing import Process
import os
import time


# In[1]:


def calc_cuad(numeros):
    print("calcula el cuadrado:")
    for n in numeros:
        time.sleep(0.2)
        print('cuadrado:', n * n )
        
def calc_cubo(numeros):
    print("calcula cubo el cubo:")
    for n in numeros:
        time.sleep(0.2)
        print('cubo:', n * n )
        
nums = range(10)

t = time.time()
calc_cuad(nums)
calc_cubo(nums)

print("Tiempo de ejecución: ", time.time()-t)
print("Finaliza ejecución")


# Una manera sencilla de generar un proceso es por medio de la creación del objeto `Process` y llamarlo por medio del método `start()`

# In[6]:


def tarea(nombre):
    print('Hola', nombre,'!')

#if __name__ == '__main__':
p = mp.Process(target=tarea, args=('Óscar',))
p.start()
p.join()


# In[9]:


def calc_cuad(numeros):
    print("calcula cuadrado de números")
    for n in numeros:
        time.sleep(0.2)
        print('cuadrado:', n * n )

nums = range(10)

t = time.time()
p1 = mp.Process(target=calc_cuad, args=(nums,))

p1.start()
p1.join()

print("Tiempo de ejecución: ", time.time()-t)
print("Finaliza ejecución")


# In[11]:


def calc_cuad(numeros):
    print("calcula cuadrado de números")
    for n in numeros:
        time.sleep(0.2)
        print('cuadrado:', n * n )
        
def calc_cubo(numeros):
    print("calcula cubo de números")
    for n in numeros:
        time.sleep(0.2)
        print('cubo:', n * n * n)


nums = range(10)

t = time.time()
p1 = mp.Process(target=calc_cuad, args=(nums,))
p2 = mp.Process(target=calc_cubo, args=(nums,))

p1.start()
p2.start()

p1.join()
p2.join()


print("Tiempo de ejecución: ", time.time()-t)
print("Finaliza ejecución")


# ## Tabla de procesos

# In[12]:


def calc_cuad(numeros):
    print("calcula cuadrado de números")
    for n in numeros:
        time.sleep(5)
        print('cuadrado:', n * n )
        
def calc_cubo(numeros):
    print("calcula cubo de números")
    for n in numeros:
        time.sleep(5)
        print('cubo:', n * n * n)


nums = range(10)

t = time.time()
p1 = mp.Process(target=calc_cuad, args=(nums,))
p2 = mp.Process(target=calc_cubo, args=(nums,))

p1.start()
p2.start()

p1.join()
p2.join()


print("Tiempo de ejecución: ", time.time()-t)
print("Finaliza ejecución")


# ## Identificadores pid, ppid

# In[13]:


print('module name:', __name__)
print('parent process:', os.getppid())
print('process id:', os.getpid())


# In[33]:


def info(titulo):
    print(titulo)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(nombre):
    info('funcion f')
    print('Hola', nombre)
    print("---------")

#f __name__ == '__main__':
info('Primera linea')
p = Process(target = f, args=('Óscar',))
p.start()
p.join()


# ## Visibilidad variables

# In[7]:


nums_res = []

def calc_cuad(numeros):
    global nums_res
    for n in numeros:
        print('cuadrado:', n * n )
        nums_res.append(n * n)
        
    #print("Resultado del proceso:", nums_res)    

    
nums = range(10)

t = time.time()
p1 = mp.Process(target=calc_cuad, args=(nums,))

p1.start()
p1.join()

print("Tiempo de ejecución: ", time.time()-t)
print("Resultado del proceso:", nums_res)    
print("Finaliza ejecución")
        


# Los procesos tienen su propio espacio de memoria. Así, las variables del programa no se comparten entre procesos. Es necesario crear comunicación entre procesos (IPC) si se desea compartir datos entre procesos.

# In[8]:


nums_res = []

def calc_cuad(numeros):
    global nums_res
    for n in numeros:
        print('cuadrado:', n * n )
        nums_res.append(n * n)
        
    print("Resultado del proceso:", nums_res)    

nums = range(10)

t = time.time()
p1 = mp.Process(target=calc_cuad, args=(nums,))

p1.start()
p1.join()

print("Tiempo de ejecución: ", time.time()-t)
print("Finaliza ejecución")
        

