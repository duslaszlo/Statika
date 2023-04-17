import sqlite3

con = sqlite3.connect('vazdata.db')
cur = con.cursor()
con1 = sqlite3.connect('statika.db')
cur1 = con1.cursor()

sql = 'select azonosito,count(*) as db from vazrud group by azonosito'

# res = cur.execute(sql)

for row in cur.execute(sql):
    print(str(row[0])+' '+str(row[1]))

#sql = 'select nev from szelveny order by nev'
#for row in cur1.execute(sql):
#    print(str(row[0]))

sql = 'select * from projectek '
print(sql)

sorszam = 0
for row in cur1.execute(sql):
    print('id:'+str(sorszam)+' adat:'+str(row[0])+' '+str(row[1]))
    sorszam = sorszam + 1