#!/usr/bin/env python
# coding: utf-8

# In[12]:


import plotly.express as px 
gapminder = px.data.gapminder()
display(gapminder)


# In[13]:


import plotly.express as px
gapminder = px.data.gapminder()
px.choropleth(gapminder,               
              locations="iso_alpha",               
              color="lifeExp",
              hover_name="country",  
              animation_frame="year",    
              color_continuous_scale='Plasma',  
              height=600             
)


# In[ ]:




