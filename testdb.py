import mysql.connector
# below are hre connection details
#conn=mysql.connector.connect(user="root",password="root123",host="localhost",database="testcompany")
conn=mysql.connector.connect(user="abc",password="rajesh",host="localhost",database="testcompany")

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

mycursor.execute(insertsql)

#mycursor=conn.cursor()

insertsql="""insert into EMPLOYEE(First_Name,Last_Name,Salary) \
                  Values('Rishita','T',25000)"""



try:
    mycursor.execute(insertsql)    
    print("Record Inserted Successfully")
    conn.commit()
except:
    conn.rollback()
    print("Record Rolled Back")


selectsql=""" Select * from EMPLOYEE """

mycursor.execute(selectsql)

result=mycursor.fetchall()

for rec in result:
    print("Name - %s %s, Salary - %d")%(rec[0], rec[1],rec[2])

    



