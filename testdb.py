import mysql.connector

conn=mysql.connector.connect(user="abc",password="rajesh",host="localhost",database="testcompany")

mycursor=conn.cursor()

mycursor.execute("Drop table if exists Employee")

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         SALARY FLOAT )"""

mycursor.execute(sql)

print("Table created successfully")

insertsql=""" insert into employee(First_Name,
              Last_Name,Salary)
              Values('Minal','T','14000')"""

try:
    mycursor.execute(insertsql)
    print("Record Inserted Successfully")
    conn.commit()
except:
    conn.rollback()
    print("Record Rolled Back")


    



