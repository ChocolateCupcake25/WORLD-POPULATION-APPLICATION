#!/usr/bin/env python
# coding: utf-8

# In[6]:


print("Name: Ziyah Virani // Fierce Bird ")
print("Build a GUI application for data visualization of word population and on various other parameters of world population")


# # Task - Build a GUI application for data visualization of word population and on various other parameters of world population

# In[34]:


#image 
#predefine code for image
from IPython.display import Image
Image(filename='map.jpg') 
#predefine code end


# In[12]:


from ipywidgets import widgets
from IPython.display import display, clear_output
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

df=pd.read_csv('population_by_country_2020.csv')
def print_dataframe(b):
    global df
    display(df)
    graph_type = ['Choose one.. ','bar','bubble']
    head_tail_list = ['head','tail']
    xlabel_widget = widgets.Dropdown(options = df.columns)
    ylabel_widget = widgets.Dropdown(options = df.columns)
    graph_widget = widgets.Dropdown(options = graph_type)
    head_tail_widget = widgets.Dropdown(options = head_tail_list)
    row_range_widget = widgets.Dropdown(options = [10,20,30])
    graph=widgets.interactive(display_plot,xaxis=xlabel_widget,yaxis=ylabel_widget,head_tail=head_tail_widget,number=row_range_widget,graph_type=graph_widget)
    display(graph)

def display_plot(xaxis,yaxis,head_tail,number,graph_type):
    global df
    if(head_tail == 'head'):
        dataframe=df.head(number)
    else:
        dataframe=df.tail(number)
    if(graph_type=='bubble'):
        if(dataframe[yaxis].dtypes == 'int64'):
            plt.subplots(figsize=(19,8))
            rgb=np.random.rand(3)
            plt.scatter(dataframe[xaxis],dataframe[yaxis],color=rgb,s=dataframe[yaxis]/40000)
            plt.xlabel(xaxis)
            plt.ylabel(yaxis)
            plt.xticks(rotation="vertical")
            plt.show()
        else:
            print("Bubble graph can't be displayed")
    elif(graph_type == "bar"):
            plt.bar(dataframe[xaxis],dataframe[yaxis],color=['red', 'green','blue','yellow','pink'])
            plt.xlabel(xaxis)
            plt.ylabel(yaxis)
            plt.xticks(rotation="vertical")
            plt.show()
    else:
        print("Choose valid graph")
        
show_dataframe=widgets.Button(description="Show Dataframe")
show_dataframe.on_click(print_dataframe)
display(show_dataframe)
            
        

    


# In[ ]:





# In[ ]:




