#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### no. 12

import maul_main

message = maul_main.greet("Maul")
print(message)

radius = 5
area = maul_main.pi * maul_main.square(radius)
print(f'Luas lingkarang dengan radius {radius} adalah {area:.2f}')

