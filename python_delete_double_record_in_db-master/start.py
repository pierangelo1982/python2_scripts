# coding=utf-8
#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","xxxxxx","testapp" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

## query for loop
sql = "select * from users"

# empty array where put unique email
a = []

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for res in results:
        # if same value already present in array, delete this record
        if res[2] in a:
            print "There can be only one (cit. Highlander)"
            query = "delete from users where id = '%i';" % res[0]
            cursor.execute(query)
            db.commit()
        a.append(res[2]) # pass email to array
except:
    print "problem problem problem"

print a

# disconnect from server
db.close()

