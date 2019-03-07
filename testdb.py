import mysql.connector

conn=mysql.connector.connect(user="root",password="root123",host="localhost",database="testcompany")

mycursor=conn.cursor()

mycursor.execute("Drop table if exists EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         SALARY FLOAT )"""

mycursor.execute(sql)

print("Table created successfully")

insertsql=""" insert into EMPLOYEE(First_Name,
              Last_Name,Salary)
              Values('Minal','T','14000')"""

try:
    mycursor.execute(insertsql)
    print("Record Inserted Successfully")
    conn.commit()
except:
    conn.rollback()
    print("Record Rolled Back")


selectsql=""" Select * from EMPLOYEE """

mycursor.execute(selectsql)

result=mycursor.fetchone()

print(result[0])
print(result[1])
print(result[2])
    



