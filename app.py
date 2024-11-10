from flask import Flask , jsonify 
import sqlite3

app= Flask(__name__)

@app.route('/<int:num>',methods = ['GET'])
def index(num): 
#connect to database(memdb) and fetche all result rows
    conn=sqlite3.connect('memdb')
    query = conn.execute('SELECT * FROM memory')
    data=query.fetchall()
    m=[]
    if num<=len(data):
     b=len(data)+1
     a=len(data)-num
#add num rows in m and return m    
     for itm in data[a:b]:
       m.append({
        'Time': itm[0],
        'Total':itm[1] ,
        'free':itm[2],
        'used':itm[3]
      })
     return jsonify(m)
    else:
      return('The number is too large!')

    
       


if __name__=="__main__":
  app.run(debug=True)