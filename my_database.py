
import pymysql as p

import pypyodbc as odbc




def connect():
    DRIVER = 'SQL Server'
    database = 'Library'
    Server = 'LAPTOP-Q9O8INGS\SQLEXPRESS'
    username = 'your_username'
    password = 'your_password'
    Port = 'myport'

    return odbc.connect(f'''DRIVER={DRIVER};
                        Server={Server};
                        Database={database};
                        Port={Port}''')





#----insert member
def insert_member(member_data):
    con = connect()
    cur = con.cursor()
    # sql_1 = "ALTER TABLE Books AUTO_INCREMENT = 1"
    # cur.execute(sql_1)
    # con.commit()
    sql1 = "INSERT INTO Member (Member_Name, Book_id, Fees) VALUES (?, ?, ?)"
    cur.execute(sql1,member_data)
    sql2 = "Update All_books set is_issued=1 where Book_id=?"
    cur.execute(sql2,(member_data[1],))
    con.commit()
    cur.close()
    con.close()
 

#---insert book from API
def insert_book_from_api(book_data_tuple):
    con = connect()
    cur = con.cursor()
    sql = '''INSERT INTO All_books (Title, Authors, Average_Rating, 
                                    ISBN, ISBN13, Language_Code, Num_Pages, 
                                    Ratings_Count, Text_Reviews_Count, Publication_Date, 
                                    Publisher) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cur.execute(sql, book_data_tuple)
    # data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    # return data



#--- all books details
def sel_all_books():
    con = connect()
    cur = con.cursor()
    sql = 'select * from All_books where is_deleted=0 and is_issued=0'
    cur.execute(sql)
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return data


#--- all member details
def sel_all_members():
    con = connect()
    cur = con.cursor()
    sql = 'select * from Member'
    cur.execute(sql)
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return data


#---edit books
def edit_book(Book_id):
    con = connect()
    cur = con.cursor()
    sql = 'select * from All_books where Book_id=?'
    cur.execute(sql,(Book_id,))
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return data


#---update books
def update_book(t):
    con = connect()
    cur = con.cursor()
    sql = '''update All_books set 
             title=?, Language_code=?,
             Publisher=? where Book_id=?'''
    cur.execute(sql,t)
    con.commit()
    cur.close()
    con.close()


# edit memeber
def edit_member(member_id):
    con = connect()
    cur = con.cursor()
    sql = 'SELECT * FROM member WHERE member_id=?'
    cur.execute(sql, (member_id,))
    data = cur.fetchall()
    cur.close()
    con.close()
    return data

# update member
def update_member(t):
    con = connect()
    cur = con.cursor()
    sql = '''UPDATE member SET 
             Member_Name=?, Book_id=?,
             Fees=? WHERE Member_Id=?'''
    cur.execute(sql, t)
    con.commit()
    cur.close()
    con.close()



# delete book
def delete_book(id):
    con = connect()
    cur = con.cursor()
    sql = '''update All_books set 
             is_deleted=1 where Book_id=?'''
    cur.execute(sql,(id,))
    con.commit()
    cur.close()
    con.close()


# Delete a book record by Book_id
def delete_member(member_id,book_id):
    con = connect()
    cur = con.cursor()
    sql = 'DELETE FROM member WHERE member_id=?'
    cur.execute(sql, (member_id,))
    sql2 = "Update All_books set is_issued=0 where Book_id=?"
    cur.execute(sql2,(book_id,))
    con.commit()
    cur.close()
    con.close()




#---------------------------------------------[User]------------------------------------------------------------------------------------


def insert_user(t):
    con = connect()
    cur = con.cursor()
    sql = "insert into info values(?,?,?,?)"
    cur.execute(sql,t)
    con.commit()
    cur.close()
    con.close()


def user_update_pass(t):                                          
    con = connect()
    cur = con.cursor()
    sql = "update info set password=? where email=?"
    cur.execute(sql,t)
    con.commit()
    cur.close()
    con.close() 


def user_log_check(email):
    con = connect()
    cur = con.cursor()
    sql = 'select email,password from info where email=?'
    cur.execute(sql,(email,))
    data = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    return data  

