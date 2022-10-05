import sqlite3


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn=sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn

#  ====insert data==========
def insert_data(conn,data):
    cursor =conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 
         criminals(Case_id INTEGER NOT NULL PRIMARY KEY,Criminal_No TEXT NOT NULL,criminaltype TEXT,
        Criminal_Name TEXT,nickname TEXT,fathername TEXT,arrestdate TEXT,datecrime TEXT,criminaladdress TEXT,criminalage TEXT,criminaloccupuation TEXT,birthmark TEXT,
        criminalgender TEXT,criminalwanted TEXT)""")
   
    sql='''INSERT INTO criminals(Criminal_No ,criminaltype,Criminal_Name ,nickname ,fathername ,arrestdate ,datecrime ,criminaladdress ,criminalage,criminaloccupuation ,birthmark 
        ,criminalgender,criminalwanted)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)'''

    cursor.execute(sql,data)
    
    conn.commit()
    return cursor.lastrowid
# ================update===================
def update_data(conn,data,colu):
    cursor = conn.cursor()
    sql=f'''UPDATE criminals SET Criminal_No = ? ,criminaltype =?,Criminal_Name=? ,nickname =? ,
     fathername =?,arrestdate =? ,datecrime =?,criminaladdress =?,criminalage =?,criminaloccupuation =? ,
    birthmark =?,criminalgender =?,criminalwanted =? WHERE  Case_id ={colu}'''

    cursor.execute(sql,data)
    conn.commit()
    return cursor.lastrowid

# ==================Delete data ============
def delete_data(conn,condi):
    cursor = conn.cursor()
    sql=f'''DELETE  FROM criminals WHERE id={condi}'''

    cursor.execute(sql)
    conn.commit()
    return cursor.lastrowid

# =======get data==============
def get_data(conn):
    try:
        cursor =conn.cursor()
        
        sql='''SELECT * FROM criminals'''

        cursor.execute(sql)
        my_data = cursor.fetchall()

        conn.commit()
        return my_data
    except Exception as e:
        print(e)
   

# ====================search =================
def search_data(conn,col_name,s_for):
    cursor =conn.cursor()
    sql=f'''SELECT * FROM criminals WHERE {col_name} = '%{s_for}%' '''

    cursor.execute(sql)
    my_data =cursor.fetchall()
    conn.commit()
    return my_data