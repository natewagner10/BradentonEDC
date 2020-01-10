import psycopg2
import csv
import sys

conn = psycopg2.connect("dbname=edc user=nwagner")
cur = conn.cursor()


matches = open(sys.argv[1], 'w')
#problems = open(sys.argv[2], 'w')
recordwriterM = csv.writer(matches, dialect='unix',quoting=csv.QUOTE_MINIMAL)
#recordwriterP = csv.writer(problems, dialect='unix',quoting=csv.QUOTE_MINIMAL)


# function to clean the results from a query:
def clean(i):
    holder = []
    for x in range(0, len(i) ):
        holder.append(i[x][0])
    return holder


# get list all of all current companies:
query = "select companyname from current;"
cur.execute(query)
comps = cur.fetchall()

comps = clean(comps)


def businessLookup(name, beg = 0, end = 5):
    string1 = "select substring(" + "'" + name + "', " + str(beg) + ", " + str(end) + ");"
    cur.execute(string1)
    busName = cur.fetchall() 
    

    query = "select companyname, address1, keyid from hoovers where companyname ilike '%" + busName[0][0] + "%';" 
    cur.execute(query)
    info = cur.fetchall()
    return info
  


def getInfo(name):
    info = businessLookup(str(name))
    beg = 0
    end = len(name)

    if len(info) == 0:
        for x in range(0, len(name)):
            #beg += 1
            end -= 1
            info = businessLookup(name, beg, end)
            if len(info) != 0:
                break

    if len(info) == 1:
        companynameH = info[0][0]
        addressH = info[0][1]
        keyid = info[0][2]
        return name, companynameH, addressH, keyid

    if len(info) > 1:
        problems = []
        problems.append(name)    
        companynameH = "BROKE"
        addressH = "BROKE"
        keyid = "BROKE"
        return name, companynameH, addressH, keyid     



getAllNames = "select companyname from current;"
cur.execute(getAllNames)
currentNames = cur.fetchall()


for name in clean(currentNames):
    if "'" in name:
        name = name.replace("'", "")
    row = []
    companynameC, companynameH, addressH, keyid = getInfo(name)
    if companynameH != 'BROKE':
        row.append([companynameC, companynameH, addressH, keyid])
        recordwriterM.writerow(row)
    else:
        continue
    





























