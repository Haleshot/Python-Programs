import mysql.connector as c
con = c.connect(host = "localhost", user = "root", passwd = "Haleshot@2003", database = "firstmysqldatabase")
if con.is_connected():
    print("Successfully Connected...")
