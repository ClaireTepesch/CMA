#Data Transformation
import json
import sqlite3

#Connect to database
sqlite_file = '/cma-artworks.db'  #filepath to access the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
conn.close()

# Get tablenames and print for reference
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
table_names = [] #array for tablenames

res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
    table_names.append(str(name[0]))

#print all the table names
for name in table_names:
    print(name)


# Print all of the data for reference
def sql_fetch(table_name):
    selection = str('SELECT * FROM ' + table_name)
    print(selection)
    c.execute(selection)
    rows = c.fetchall()
    for row in rows:
        print(row)
for name in table_names: #iterate through table names
    sql_fetch(name)

#------------------------------------------------------
# DATA ORGANIZATION
artworksList = []
selection = str('SELECT * FROM artwork')
print(selection)
c.execute(selection)
rows = c.fetchall()

print("\nPrinting each artwork")
for row in rows: #iterate through the rows
    artPiece = [] #array to contain each artpiece
    ID = row[0]
    print("ID ", row[0])
    artPiece.append(ID)
    # DEPARTMENT RETRIEVAL
    selection2 = str('SELECT * FROM artwork__department')
    c.execute(selection2)
    rows2 = c.fetchall()
    for row2 in rows2: #connect department ID to correct department
        if ID == row2[0]:
            deptID = row2[1]
            # print(deptID)
            selection4 = str('SELECT * FROM department')
            c.execute(selection4)
            rows4 = c.fetchall()
            for row4 in rows4:
                if deptID == row4[0]:
                    print("DEPT = ", row4[1])
                    deptName = row4[1]
                    artPiece.append(deptName) # add the correct department name to the artpiece element of the list
    # CREATOR
    selection3 = str('SELECT * FROM artwork__creator')
    # print("here")
    c.execute(selection3)
    rows3 = c.fetchall()
    for row3 in rows3: # connect department ID to correct department
        if ID == row3[0]:
            creatorID = row3[1]
            # print("CREATOR ID: ", row3[1])
            selection5 = str('SELECT * FROM creator')
            c.execute(selection5)
            rows5 = c.fetchall()
            for row5 in rows5:
                if creatorID == row5[0]:
                    print("CREATOR = ", row5[2])
                    creatorName = row5[2]
                    artPiece.append(creatorName)
                    break
    # select artwork again
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
    artPiece.append(otherName) #add information to the artwork
    artworksList.append(artPiece) #append the artwork to the master list

#outputfile for the json
f = open("outputfile.json", "w+")
x = json.dumps(artworksList) #convert to json

#write the json to a file
with open('data.txt', 'w') as outfile:
    json.dump(x, outfile)

