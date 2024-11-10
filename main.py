import sqlite3
import time
import psutil
#create a sqlite database(memdb) and define a table into the database(memory)
conn=sqlite3.connect('memdb')
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS memory(
       timestamp INT,
       total INT,
       available INT,
       used INT        
)""")
conn.commit()
conn.close()
#get the memory information(total,available, used) by  psutil library and write them in database
while True: 
     timestamp=int(time.time())
     svmem =psutil.virtual_memory()
     total= svmem.total//1000000  
     available= svmem.available//1000000
     used= svmem.used//1000000
     conn=sqlite3.connect('memdb')
     cursor=conn.cursor()
     cursor.execute("INSERT INTO memory VALUES(?, ?, ?, ?);", (timestamp, total, available, used))
     conn.commit()
     conn.close()  
 #save the memory information in the database every 60 seconds 
     time.sleep(60)