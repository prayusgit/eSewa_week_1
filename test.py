import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysqlkoID@1"
)

mycursor = mydb.cursor()

mycursor.execute("use week_1")
mycursor.execute("INSERT INTO User VALUES (1, 'hello', 'hello', 1000)")

mydb.commit()


