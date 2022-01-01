#!/usr/bin/env python
# coding: utf-8

# In[7]:


print('''\nTwinkle, twinkle, little star,\n       How I wonder what you are!,\n         Up above the world so high,\n         Like a diamond in the sky.
Twinkle, twinkle, little star,\n       How I wonder what you are''')


# In[6]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[1]:


r=int(input("enter number="))
pie=3.14
a=(r**2)*pie
print(a)


# In[2]:


first,last=str(input("enter your first and last name,\ngive input in space between them=")).split()
print(last[::-1],first[::-1])
print()


# In[17]:


num1=int(input("enter number="))
num2=int(input("enter number="))
print(num1+num2)


# In[8]:


import datetime
now = datetime.datetime.now()
print("Current date and time: ")
print(str(now))


# In[ ]:




