
# coding: utf-8

# In[1]:

import pandas as pd
import unicodedata


# In[2]:

xl=pd.ExcelFile('C:\Users\Deepak Kumar\Desktop/naukri.xlsx')
companies=pd.ExcelFile('C:\Users\Deepak Kumar\Desktop/india fortune 500.xlsx')
companies_data=companies.parse('India')
comanies_table=pd.DataFrame(companies_data)


# In[3]:

df=xl.parse('Sheet1')
data=pd.DataFrame(df)

data[u'currentorganisation'].count()


# In[4]:

comanies_table[u'Company'].count()


# In[5]:

lista=[]
newtable=data
counter=0
for each in comanies_table[u'Company']:
    for all in data[u'currentorganisation']:
        if each.split(" ")[0] == str(all).split(" ")[0]:
            lista.append(all)
        
            
            


# In[6]:

set(lista)


# In[7]:

numset=[]
for each in data[u'currentorganisation']:
    if each in set(lista):
        numset.append(1)
    else:
        numset.append(0)
            


# In[8]:

data['organisation level']=numset


# In[9]:

data


# In[10]:

#IBM NOT IN TOP 500 ??
#KILL THE BEAST.
#ACCENTURE NOT IN BOTH LIST
#ERNST AND YOUNG ?
#citibank not in top 500 ?


# In[11]:

degree_list=[]
for all in data[u'degree']:
    degree_list.append(all)


# In[12]:

set(degree_list)


# In[13]:

main_degree_list=['B.Sc (Computers) ','B.Sc (Computers)  ','B.Sc (Statistics)  ','B.Tech/B.E. (Computer Science) ','B.Tech/B.E. (Computer Science)  ','B.Tech/B.E. (Computers) ','B.Tech/B.E. (Electrical) ','B.Tech/B.E. (Electrical)  ','B.Tech/B.E. (Electronics/Telecommunication) ','B.Tech/B.E. (Electronics/Telecommunication)  ','B.Tech/B.E. (Information Technology) ','B.Tech/B.E. (Information Technology)  ','BCA (Computers) ','BCA (Computers)  ','BCA (JAVA)  ','BCS (Computer Science) ','BCS (Computer Science)  ','BE (Computer Science) ','Bsc Tech (Electronics and Telecom) ','Bsc Tech (Electronics and Telecom)  ','M.Sc (Software Systems) ','M.Sc (Software Systems)  ','Msc (Computer Science) ']


# In[14]:

degree_set=[]
for each in data['degree']:
    if str(each) in main_degree_list:
        degree_set.append(1)
    else:
        degree_set.append(0)


# In[15]:

degree_set
data['degree_level']=degree_set


# In[16]:

data['degree'][6]


# In[17]:

data['degree'][7]


# In[ ]:




# In[18]:

emp=[]
college=data['college']
for each in college:
    if each in emp:
        emp.append('yes')
    else:
        emp.append(each)
        


# In[19]:

university=pd.ExcelFile('C:\Users\Deepak Kumar\Desktop/topuniv.xlsx')


# In[20]:

univ_data=university.parse('Sheet1')


# In[21]:

univ_data=pd.DataFrame(univ_data)


# In[22]:



univ_data


# In[23]:

col_list=[]
for each in univ_data[u'University']:
    for all in data[u'college']:
        if all.strip(" ") == each.strip(" "):
            col_list.append(all)
            
            
            


# In[24]:

len(col_list)
newlist=[]
for each in data[u'college']:
    if each in col_list:
        newlist.append(1)
    else:
        newlist.append(0)

    


# In[25]:

len(newlist)


# In[26]:

data[u'Undergrad college level']=newlist


# In[27]:

data


# In[28]:

skill_list=['C','C++','python','Hadoop','R','SQL','java','scala','HDFS','pig','hive','business intelligence','NoSQL','MYSQL','Hbase','sqoop']
skill_list=[x.lower() for x in skill_list]


# In[29]:

skill_list
for each in data[u'keyskills']:
    print each.lower().strip(" ")
    print "------------"


# In[48]:

skill_box=[]
for each in data[u'keyskills']:
    if set(skill_list) & set (each.lower()):
        skill_box.append(1)
    else:
        skill_box.append(0)
        


# In[52]:

data['skill_level']=skill_box
data


# In[54]:

writer=pd.ExcelWriter('C:\Users\Deepak Kumar\Desktop/cleanv2.xlsx')
data.to_excel(writer,'Sheet1')
writer.save()


# In[ ]:



