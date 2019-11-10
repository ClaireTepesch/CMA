#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Connecting to database test 
import json
import sqlite3

sqlite_file = '/Users/Claire/Downloads/cma-artworks.db'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
conn.close()


# In[2]:


# Get tablenames
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
table_names = []

res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
    #print(name[0])
    table_names.append(str(name[0]))
    
for name in table_names:
    print(name)


# In[3]:


#Print fetch data

def sql_fetch(table_name):
 
    selection = str('SELECT * FROM '+ table_name)
    print(selection)
    c.execute(selection)
 
    rows = c.fetchall()
 
    for row in rows:
 
        print(row)

for name in table_names:
    sql_fetch(name) 


# In[4]:


import json
artworksList = []

#DATA ORGANIZATION
#artwork
selection = str('SELECT * FROM artwork')
print(selection)
c.execute(selection)
rows = c.fetchall()

print("\nPrinting each artwork")
for row in rows:
    artPiece = []
    ID = row[0]
    print("ID ", row[0] )
    artPiece.append(ID)
    #DEPARTMENT
    selection2 = str('SELECT * FROM artwork__department')
    c.execute(selection2)
    rows2 = c.fetchall()
    for row2 in rows2:
        if ID == row2[0]:
            deptID = row2[1]
            #print(deptID)
            selection4 = str('SELECT * FROM department')
            c.execute(selection4)
            rows4 = c.fetchall()
            for row4 in rows4:
                if deptID == row4[0]:
                    print("DEPT = ", row4[1])
                    deptName = row4[1]
                    artPiece.append(deptName)
    #CREATOR           
    selection3 = str('SELECT * FROM artwork__creator')
    #print("here")
    c.execute(selection3)
    rows3 = c.fetchall()
    for row3 in rows3:
        if ID == row3[0]:
            creatorID = row3[1]
            #print("CREATOR ID: ", row3[1])
            selection5 = str('SELECT * FROM creator')
            c.execute(selection5)
            rows5 = c.fetchall()
            for row5 in rows5:
                if creatorID == row5[0]:
                    print("CREATOR = ", row5[2]) 
                    creatorName = row5[2]
                    artPiece.append(creatorName)
                    break
    #select artwork again
    selection = str('SELECT * FROM artwork')
    c.execute(selection)
    print("Year = ", row[1])
    yearName = row[1]
    artPiece.append(yearName)
    print("Name  = ", row[2])
    artName = row[2]
    artPiece.append(artName)
    print("Other info  = ", row[3], "\n")
    otherName = row[3]
    artPiece.append(otherName)
    artworksList.append(artPiece)
    

f= open("outputfile.txt","w+")
x = json.dumps(artworksList)

with open('data.txt', 'w') as outfile:
    json.dump(x, outfile)
    


# In[5]:


print(artworksList)


# In[ ]:




