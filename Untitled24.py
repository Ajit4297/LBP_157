#!/usr/bin/env python
# coding: utf-8

# In[4]:


class FiveDivisionError(Exception):
    pass
try:
    n1=int(input('enter 1st number'))
    n2=int(input('enter 2nd number'))
    if n2==5:
        raise FiveDivisionError('cannot divided by 5')
    div=n1/n2
    print(div)
except (FiveDivisionError,ZeroDivisionError) as res :
    print(res)
    


# In[ ]:




