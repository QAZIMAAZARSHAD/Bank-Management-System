import mysql.connector as a
con = a.connect(host="localhost", user="root", passwd="*******", database="bank")

def main():
     print("""
           1. Open New Account
           2. Deposit Amount
           3. Withdraw Amount
           4. Balance Enquiry
           5. Display Customer Details
           6. Close an Account
           """)
     choice = input("Enter Task No. : ")
     if(choice == '1'):
          openAcc()
     elif(choice == '2'):
          depoAmo()
     elif(choice == '3'):
          withAmo()
     elif(choice == '4'):
          balance()
     elif(choice == '5'):
          dispAcc()
     elif(choice == '6'):
          closeAcc()
     else:
          print("Wrong Input")
          main()
     
     
def openAcc():
     n = input("Enter Name : ")
     ac = input("Enter Account No. : ")
     db = input("Enter D.O.B (yyyy-mm-dd) : ")
     p = input("Enter Phone No. : ")
     ad = input("Enter Address : ")
     ob = int(input("Enter Opening Balance : "))
     data1 = (n,ac,db,p,ad,ob)
     data2 = (n,ac,ob)
     sql1 = 'insert into account values(%s,%s,%s,%s,%s,%s)'
     sql2 = 'insert into amount values(%s,%s,%s)'
     c = con.cursor()
     c.execute(sql1,data1)
     c.execute(sql2,data2)
     con.commit()
     print("Data Entered Successfully")
     main()

def depoAmo():
     am = int(input("Enter Amount : "))
     ac = input("Enter Account No. : ")
     a = 'select balance from amount where acno = %s'
     data = (ac,)
     c = con.cursor()
     c.execute(a,data)
     myresult = c.fetchone()
     tam = myresult[0] + am
     sql = 'update amount set balance = %s where acno = %s'
     d = (tam,ac)
     c.execute(sql,d)
     con.commit()
     main()

def withAmo():
     am = int(input("Enter Amount : "))
     ac = input("Enter Account No. : ")
     a = 'select balance from amount where acno = %s'
     data = (ac,)
     c = con.cursor()
     c.execute(a,data)
     myresult = c.fetchone()
     tam = myresult[0] - am
     sql = 'update amount set balance = %s where acno = %s'
     d = (tam,ac)
     c.execute(sql,d)
     con.commit()
     main()

def balance():
     ac = input("Enter Account No. : ")
     a = 'select balance from amount where acno = %s'
     data = (ac,)
     c = con.cursor()
     c.execute(a,data)
     myresult = c.fetchone()
     print("Balance Amount of Account: ",ac," is",myresult[0])
     main()

def dispAcc():
     ac = input("Enter Account No. : ")
     a = 'select * from amount where acno = %s'
     data = (ac,)
     c = con.cursor()
     c.execute(a,data)
     myresult = c.fetchone()
     for i in myresult:
          print(i,end=" ")
     main()

def closeAcc():
     ac = input("Enter Account No. : ")
     sql1 = 'delete from account where acno = %s'
     sql2 = 'delete from amount where acno = %s'
     data = (ac,)
     c = con.cursor()
     c.execute(sql1,data)
     c.execute(sql2,data)
     con.commit()
     main()
