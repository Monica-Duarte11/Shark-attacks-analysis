#!/usr/bin/env python
# coding: utf-8


import pandas as pd 
import numpy as np
import regex as re
from datetime import date, datetime, timedelta 
import requests 
import seaborn as sns


def fecha_limpia(x):
    try:
        if re.match('[0-9]{2}-[a-zA-Z]{3}--[0-9]{4}',x):
            return datetime.strptime(x,"%d-%b--%Y").date()
    
        elif re.match('[a-zA-Z]{3}-[0-9]{4}',x):
            return datetime.strptime(x, "%b-%Y").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}[0-9]{4}',x):
            return datetime.strptime(x,"%d-%b%Y").date()
        elif re.match('[a-zA-Z]{3} [0-9]{4}',x):
            return datetime.strptime(x, "%b %Y").date()
        elif re.match('[a-zA-Z]{3}[0-9]{4}',x):
            return datetime.strptime(x, "%b%Y").date()
        elif re.match('\s[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}',x):
            return datetime.strptime(x," %d-%b-%Y").date()
        elif re.match('[0-9]{4}$',x):
            return datetime.strptime(x,"%Y").date()
        elif re.match('[a-zA-Z]+ [0-9]{4}',x):
            return datetime.strptime(x, "%B %Y").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}.+',x):
            return datetime.strptime(x.split('.')[0],"%d-%b-%Y").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}.+',x):
            return datetime.strptime(x,"%d-%b-%Y ").date()
        elif re.match('[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}', x):
            return datetime.strptime(x,"%d-%b-%Y").date()   
        elif 'or' in x:
            return datetime.strptime(x.split('or')[0],"%d-%b-%Y").date()
                                     
        else : 
            x = '01-01-1000'
            return datetime.strptime(x,"%d-%m-%Y").date()
    except ValueError as e:
        x = '01-01-1000'
        return datetime.strptime(x,"%d-%m-%Y").date()
        pass


def Check_URL (x):
    
    try:
        r = requests.get(x)
        if r.status_code > 400:
            return ('URL invalid', ': ',x)

    except requests.exceptions.MissingSchema as e:
        print (e)
    except Exception as e:
        print(e)



def value_to_num(x):
    if type(x) == int:
        return x
    elif type(x) == float:
        return  x
    else:
        re.sub('[^0-9]', '', x)
        if re.match('[0-9]+',x):
            x =  x [0:2]
        return x
    
# In[5]:


def Species_limpia (x):
    try:
    
        if re.match('.*white shark.*' , x):
            x = 'white shark'
            return x

        elif re.match('.*bull shark.*' , x):
            x = 'bull shark'
            return x

        elif re.match('.*mako shark.*' , x):
            x = 'mako shark'
            return x

        elif re.match('.*tiger shark.*' , x):
            x = 'tiger shark'
            return x

        elif re.match('.*nurse shark.*' , x):
            x = 'nurse shark'
            return x

        elif re.match('.*wobbegong shark.*' , x):
            x = 'wobbegong shark'    

        elif re.match('.*blacktip shark.*' , x):
            x = 'blacktip shark'  
            return x

        elif re.match('.*bronze whaler shark.*' , x):
            x = 'bronze whaler shark'
            return x

        elif re.match('.*raggedtooth shark.*' , x):
            x = 'raggedtooth shark'
            return x

        elif re.match('.*Zambesi shark.*' , x):
            x = 'Zambesi shark' 

        elif re.match('.*small shark.*' , x):
            x = 'small shark' 
            return x

        elif re.match('.*blue shark.*' , x):
            x = 'blue shark' 
            return x

        elif re.match('.*grey nurse shark.*' , x):
            x = 'grey nurse shark' 
            return x

        elif re.match('.*spinner  shark.*' , x):
            x = 'spinner shark'
            return x
        
        elif re.match('.*lemon  shark.*' , x):
            x = 'lemon shark'
            return x
        
        elif re.match('.*grey nurse shark.*' , x):
            x = 'grey nurse shark'
            return x
        
        elif re.match('.*sandtiger shark.*' , x):
            x = 'sand tiger shark'
            return x
        
        elif re.match('.*reef shark.*' , x):
            x = 'reef shark'
            return x
            
        else: 
            return x
    except ValueError as e:
        print (e)
        return x
        pass
    except TypeError as e:
        print (e)
        return x
        pass


def hora_limpia(x):
    try:
        if re.match('Late afternoon',x):
            x = '15h00'
            return datetime.strptime(x,"%Hh%M").time()
        elif re.match('Afternoon',x):
            x = '14h00'
            return datetime.strptime(x,"%Hh%M").time()
        elif re.match('Night',x):
            x = '21h00'
            return datetime.strptime(x,"%Hh%M").time()
        elif re.match('Morning',x):
            x = '08h00'
            return datetime.strptime(x,"%Hh%M").time()
        elif re.match('afternoon',x):
            x = '13h00'
            return datetime.strptime(x,"%Hh%M").time()
        elif re.match('Mid-morning',x):
            x = '10h00'
            return datetime.strptime(x,"%Hh%M").time()
        elif re.match('. +[0-9]{2}h[0-9]{2}',x):
            x = x.split('h')
            return atetime.strptime(x[0],"%Hh%M").time()
        elif re.match('[0-9]{2}h[0-9]{2}',x):
            return datetime.strptime(x,"%Hh%M").time()
        
        else : 
            x = '00h00'
            return datetime.strptime(x,"%Hh%M").time()
    except ValueError as e:
        x='00h00'
        return datetime.strptime(x,"%Hh%M").time()
        pass
    except TypeError as e:
        x='00h00'
        return datetime.strptime(x,"%Hh%M").time()
        pass

