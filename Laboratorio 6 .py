#!/usr/bin/env python
# coding: utf-8

# In[25]:


import re


# In[26]:


#1. Genere una expresión regular que detecte placas de vehiculos particulaes
placas_p = ['P250FVP','P457DRF','P567FBC','C904HJG']
print(placas_p)


# In[27]:


p = re.compile('P+[\d]+[\w]')
placaspar = list(filter(p.match, placas_p))
print(placaspar)
               


# In[28]:


#2. Genere una expresión regularar para ver si un arhivo es pdf o jpg
archivos = ['Ejemplo1.pdf','prueba2.PDF','respuestas_del_examen.jpg','amor.JPG','paraver.csv']
print(archivos)


# In[29]:


ar = re.compile('\w+\.+[pdf|PDF|jpg|JPG]')
ar2 = list(filter(ar.match, archivos))
print(ar2)


# In[56]:


# 3.Genere una exprasión regular para validar una contraseña
contra = ['Diegoralon#','diegoRalon!','pruebanocumple']


# In[57]:


# 8 caracteres, una mayuscula y un caracter especia
c = re.compile('(?=.*[A-Z])(?=.*[!@#$&*]).{8}')
con_2 = list(filter(c.match, contra))
print(con_2)


# In[98]:


# Reconocer numeros de telefono de guatemala 
telefonos = ['+50254821151','4210-7640','520018150','24346854','11234568','50211234578'] 


# In[192]:


# Reconocer telefonos de gt
t = re.compile('((\+)?(502)?)[4|5|6|2]\d{3,12}')
teprueba = list(filter(t.match, telefonos))
print(teprueba)


# In[179]:


# Expresión regular que sea capaz de obtener correos de la uf, 
correos = ['diegoralon@ufm.edu','diegoralon@uvg.edu','diegoralon@url.edu','diegoralon@ufm']


# In[180]:


cor = re.compile('\w+\@+(ufm)\.+(edu)')
corpruebas = list(filter(cor.match, correos))
print(corpruebas)


# In[193]:


# Solo mostrar las primeras palabras y no las de segunda linea
palabras = ['pit','spot','spate','slap two','respite','pt','Pot','peat','part']


# In[226]:


pal = re.compile('p.t')
palpr = list(filter(pal.search, palabras))
print(palpr)


# In[ ]:




