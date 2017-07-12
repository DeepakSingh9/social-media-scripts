
# coding: utf-8

# In[4]:

import pandas as pd


# In[5]:

xl=pd.ExcelFile('C:\Users\Deepak Kumar\Desktop/Clear_data.xlsx')
df=xl.parse('Sheet2')
data=pd.DataFrame(df)


# In[6]:

data


# In[37]:

data.columns
alist=[]
blist=[]


# In[38]:

for a,b,c,d,e in zip(data[u'Degree Level'],data[u'Field of Study_Sorted'],data[u'Type of Institute'],data[u'skill_level'],data[u'Experience'] ):
    if ([a,b,c,d]==[0,1,0,1] and e>=24) or ([a,b,c,d,e]==[1,1,0,1,0]) or ([a,b,c,d,e]==[1,1,1,1,0]):
        alist.append('ABDE')
    elif ([a,c,d]==[0,0,2] and (b==1 or b==2) and e>=24) or ([a,c,d,e]==[1,0,2,0] and (b==1 or b==2)) or ([a,c,d,e]==[1,1,2,0] and (b==1 or b==2)):
        alist.append('ABDA')
    elif ([a,b,c,d]==[1,1,0,1] and e>=24) or ([a,b,c,d]==[2,1,0,1] and e>=12) or ([a,b,c,d]==[1,1,1,1] and e>=12) or ([a,b,c,d,e]==[2,1,1,1,0]):
        alist.append('SBDE')
    elif ([a,c,d]==[1,0,2] and (b==1 or b==2) and e>=24) or ([a,c,d]==[2,0,2] and (b==1 or b==2) and e>=12) or ([a,c,d]==[1,1,2] and (b==1 or b==2) and e>=12) or ([a,c,d,e]==[2,1,2,0] and (b==1 or b==2)):
        alist.append('SBDA')
    else:
        alist.append('Not Available')
    


# In[39]:

for a,b,c,d,e in zip(data[u'Degree Level'],data[u'Field of Study_Sorted'],data[u'Type of Institute'],data[u'Skill Level_analyst'],data[u'Experience'] ):
    if ([a,b,c,d]==[0,1,0,1] and e>=24) or ([a,b,c,d,e]==[1,1,0,1,0]) or ([a,b,c,d,e]==[1,1,1,1,0]):
        blist.append('ABDE')
    elif ([a,c,d]==[0,0,2] and (b==1 or b==2) and e>=24) or ([a,c,d,e]==[1,0,2,0] and (b==1 or b==2)) or ([a,c,d,e]==[1,1,2,0] and (b==1 or b==2)):
        blist.append('ABDA')
    elif ([a,b,c,d]==[1,1,0,1] and e>=24) or ([a,b,c,d]==[2,1,0,1] and e>=12) or ([a,b,c,d]==[1,1,1,1] and e>=12) or ([a,b,c,d,e]==[2,1,1,1,0]):
        blist.append('SBDE')
    elif ([a,c,d]==[1,0,2] and (b==1 or b==2) and e>=24) or ([a,c,d]==[2,0,2] and (b==1 or b==2) and e>=12) or ([a,c,d]==[1,1,2] and (b==1 or b==2) and e>=12) or ([a,c,d,e]==[2,1,2,0] and (b==1 or b==2)):
        blist.append('SBDA')
    else:
        blist.append('Not Available')
    


# In[41]:

data['course_engineer_new']=alist


# In[42]:

data['course_analyst_new']=blist


# In[43]:

writer=pd.ExcelWriter('C:\Users\Deepak Kumar\Desktop/courseallonew.xlsx')
data.to_excel(writer,'Sheet1')
writer.save()


# In[ ]:



