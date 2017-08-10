#/bin/python3

# get current timestamp to database
# $date "+%Y-%m-%d %H:%M:%S"

# tshark
# sudo tshark -te -i enp0s3 -f "src 10.0.2.15" -T fields -e frame.time_epoch -e ip.dst


import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="puzzle",  # your password
                     db="ip_database")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

cur.execute("SELECT * FROM ip_table")

rows = cur.fetchall()

print (rows)

"""for row in rows:
    for col in row:
        print ("%s," % col)
    print ("\n")

db.close()
"""
