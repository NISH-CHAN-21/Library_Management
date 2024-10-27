import mysql.connector as mysql

lib=mysql.connect(
    host="localhost",
    user="root",
    password="NISHchan@21"
)

cur=lib.cursor()
# cur.execute("CREATE DATABASE LIBRARY")
cur.execute("USE LIBRARY")
# cur.execute("CREATE TABLE BOOKS(BID varchar(10) PRIMARY KEY, BNAME VARCHAR(50))")


class library:
    
    def __init__(self,bid,bname):
        self.bname=bname
        self.bid=bid
        
        
    def insert(self):
        sql= f"INSERT INTO BOOKS(BID,BNAME) VALUES(%s,%s)"
        value=(f"{self.bid}",f"{self.bname}")
        cur.execute(sql,value)
        lib.commit()
        print(cur.rowcount,"RECORD INSERTED.............")
    
    def delete(self):
        sql= f"DELETE FROM BOOKS WHERE BID=%s"
        value=(f"{self.bid}",)
        cur.execute(sql,value)
        lib.commit()
        print(cur.rowcount,"RECORD DELETED SUCCESSFULLY..............")
        
    def info(self):
        sql=(f"SELECT * FROM BOOKS WHERE BID=%s")
        value=(f"{self.bid}",)
        cur.execute(sql,value)
        print(("BOOK_ID","BOOK_NAME"))
        res=cur.fetchone()
        print(res)
        
    @staticmethod
    def all():
        cur.execute("SELECT COUNT(*) FROM BOOKS")
        res1=cur.fetchone()
        for y in res1:
            print("THERE ARE TOTAL OF",y,"BOOKS IN THE LIBRARY...........")
        sql=(f"SELECT * FROM BOOKS")
        cur.execute(sql)
        print(("BOOK_ID","BOOK_NAME"))       
        res=cur.fetchall()
        for i in res:
            print(i)
    

while(True):
    
    x=int(input("""                                       WELCOME TO OUR LIBRARY, WHAT WOULD YOU LIKE TO DO :
      
                                                            PLEASE ENTER :
      
                                        1 - ENTER A BOOK                  2 - REMOVE A BOOK
                                        3 - INFO ABOUT A BOOK             4 - NUMBER OF BOOKS
      """))

    if x==1:
        
        x1=input("ENTER BOOK ID: ")
        x2=input("ENTER BOOK NAME: ")
        a=library(x1,x2)
        a.insert()

    elif x==2:
        
        x1=input("ENTER BOOK ID TO DELETE: ")
        a=library(x1,None)
        a.delete()

    elif x==3:
        x1=input("ENTER BOOK ID TO SELECT: ")
        a=library(x1,None)
        a.info()
        
    elif x==4:        
        print(library.all())
    
    else:
        print("WRONG INPUT.........")
        
    z=int(input("""                                         WOULD YOU LIKE TO CONTINUE: 
                                                                
                                                                PLEASE ENTER: 
                                            
                                            0 - QUIT                       1 - CONTINUE
    """))
    
    if z==0:
        break
    elif z==1:
        continue
    else:
        print("WRONG INPUT.......... QUITTED.........")
        break
    
    
    
   
    
    
    



    



        
    
    


    


        