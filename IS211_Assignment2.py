#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import urllib.request
import logging
import datetime


# In[13]:


def downloadData(url):
    """Downloads the data"""
    return url

   


# In[ ]:


def main(url):
    print(f"Running main with URL = {url}...")


# In[52]:


import urllib.request

with urllib.request.urlopen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv') as response:
    html = response.read()
   
    


# In[53]:


html


# In[54]:


print(html)


# In[55]:


html.decode('utf-8')


# In[56]:


print(html.decode('utf-8'))


# In[39]:


html


# In[42]:


print(html.decode('utf-8'))


# In[6]:


def processData(file_content):
    for line in file:
        person_bd = {ID: (name, birthday)}
        return person_bd
    print(person_bd)


# In[16]:


import datetime

birthday = datetime.datetime.strptime('28/06/1985', '%d/%m/%Y')
print(birthday)


# In[4]:


import logging
my_logger = logging.getLogger('Assignment2')


logging.error('Error processing line #<linenum> for ID #<id>')


# In[14]:



def displayPerson(id, personData):
    if id:
        print(personData)
    else:
        print('No user found with that id')
    


# In[1]:


def main(url):
    print(f"Running main with URL = {url}...")


# In[5]:


import argparse
if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv",
                        type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    try:
        birthday = datetime.strptime('11/11/19895', '%d%m%y')
    except FormatError as e:
        print(error)                                 
                                     
    logging.error('Error processing line #<linenum> for ID #<id>')


# In[ ]:




