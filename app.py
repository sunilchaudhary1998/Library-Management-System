
from flask import *
from my_database import *

import requests        
from datetime import datetime


app = Flask(__name__)


#-----------------[book data]---------------------------------------------------------------------------

d = {}
c = {}
auth = dict()                      # note :-  about, not, yes pe (nai dala hai pop method)




#----Authentication
@app.route("/logout_drug")                # note :-  about, not, yes pe (nai dala hai pop method)
def logout_drug():
   try:
      auth.pop("l")
      return redirect("/")
   except:
      return redirect("/")



#----home   (main page before)
@app.route('/')                                         
def main():
   return render_template('main.html')

#---
# #----about (medico kundli)
# @app.route('/about')
# def about():
#        return render_template('about.html')
#---
  


#----index (home off app)
@app.route('/index')
def home():
      return render_template('home.html')



#----det   for books
@app.route('/all_book_details')                                      
def all_book_details():
   a = sel_all_books()
   return render_template('all_book_details.html',book_list=a)


#----det   for members
@app.route('/all_member_details')                                      
def all_member_details():
   a = sel_all_members()
   return render_template('all_member_details.html',member_list=a)


#----no
@app.route('/not')                                   
def nott():
   return render_template('not.html')         


#----reg drug (adding new book in reg page)
@app.route('/book_reg')                                      
def drug_reg():
   return render_template('book_reg.html')  


#----reg member (adding new member in reg page)
@app.route('/member_reg')                                      
def member_reg():
   return render_template('member_reg.html')  



#-----------------------------[insert]---------------------------------------------------

#----member insert
@app.route('/member_insert', methods=['POST'])
def member_insert():
    Member_Name = request.form['Member_Name']
    Book_id = int(request.form['Book_id'])  
    Fees = float(request.form['Fees'])  
    member_data = (Member_Name, Book_id, Fees)
    insert_member(member_data)  
    return redirect('/all_member_details')



#---manual insert of book details
@app.route('/book_insert', methods=['POST'])
def book_insert():
    
   title = request.form['title']
   authors = request.form['authors']
   average_rating = float(request.form['average_rating'])
   isbn = request.form['isbn']
   isbn13 = request.form['isbn13']
   language_code = request.form['language_code']
   num_pages = int(request.form['num_pages'])
   ratings_count = int(request.form['ratings_count'])
   text_reviews_count = int(request.form['text_reviews_count'])
   publication_date = request.form['publication_date']
   publisher = request.form['publisher']

   book_data_tuple = (title, authors, average_rating, isbn, isbn13, language_code, num_pages,
               ratings_count, text_reviews_count, publication_date, publisher)

   insert_book(book_data_tuple)

   return redirect('/all_book_details')  





#--- from api book insert  
@app.route('/import_books', methods=['POST'])
def import_books():
    
    api_url = "https://frappe.io/api/method/frappe-library?page=2&title=and"  
    response = requests.get(api_url)
    data = response.json()["message"]  

    for book_data in data:  
        title = book_data.get("title", "")[:100]  
        authors = book_data.get("authors", "")
        average_rating = float(book_data.get("average_rating", 0.0))
        isbn = book_data.get("isbn", '')
        isbn13 = book_data.get("isbn13", '')
        language_code = book_data.get("language_code", "")
        num_pages = int(book_data.get("num_pages", 0))  
        ratings_count = int(book_data.get("ratings_count", 0))
        text_reviews_count = int(book_data.get("text_reviews_count", 0))
        publication_date = datetime.strptime(book_data.get("publication_date", "01/01/1900"), "%m/%d/%Y")
        publisher = book_data.get("publisher", "")
        
        book_data_tuple = (
            title,
            authors,
            average_rating,
            isbn,
            isbn13,
            language_code,
            num_pages,
            ratings_count,
            text_reviews_count,
            publication_date,
            publisher
        )

        insert_book_from_api(book_data_tuple)  
    
    return redirect('/all_book_details')

    


#-----------------------[check / single info fetch]----------------------------------------------------

#----particular drug chaeck page
@app.route("/single_book_info_check")                                  
def single_book_info_check():
   return render_template("single_book_info_check.html")



#----particular drug details full
@app.route("/single_book_info")                                  
def single_book_info():
    if "i" in d:
        x = sel_single_book(d["i"])
        return render_template("single_book_info.html", ic=x)
    


#----particular book  [with details]
@app.route("/single_book_data_check", methods=["post"])
def single_book_data_check():
    title = request.form["title"]
    t = title
    t1 = check_book_avail(title)
    if t1 is not None:  
        if t in t1:
            d["i"] = t  
            return redirect("/single_book_info")  
    else:
        return redirect("/not")



#---------------[edit / update]----------------------------------------------------------------------


#----book edit
@app.route("/book_edit")                                  
def book_edit():
   Book_id = request.args.get("id")
   data = edit_book(Book_id)
   return render_template("book_edit.html",x=data)



#----book update
@app.route("/book_update",methods=['post'])                
def book_update():
   Book_id = request.form['Book_id']
   Book_title = request.form['Book_title']
   Language_code = request.form['Language_code']
   Publisher = request.form['Publisher']  
   t = (Book_title,Language_code,Publisher,Book_id)
   update_book(t)
   return redirect("/all_book_details")



#----member edit
@app.route("/member_edit")                                  
def member_edit():
   member_id = request.args.get("id")
   data = edit_member(member_id)
   return render_template("member_edit.html",x=data)


#----member update
@app.route("/member_update", methods=['POST'])
def member_update():
    Member_Id = request.form['Member_Id']
    Member_Name = request.form['Member_Name']
    Book_id = request.form['Book_id']
    Fees = request.form['Fees']
    member_data = (Member_Name, Book_id, Fees, Member_Id)
    update_member(member_data)  

    return redirect("/all_member_details")


#-----------------------------------[delete] or [issue]-----------------------------------------------

#----book delete
@app.route("/book_delete")                             
def drug_delete():
   id = request.args.get("id")
   delete_book(id)
   return redirect("/member_reg")

#----member delete
@app.route("/member_delete")                             
def member_delete():
   member_id = request.args.get("id")
   book_id = request.args.get("book_id")
   delete_member(member_id,book_id)
   return redirect("/all_member_details")




#----------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------[user login]----------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------


#----login4   for  user
@app.route('/user_login')                                   
def user_login():
   return render_template('user_login.html')   


#----register4   for user
@app.route('/user_reg')                                
def user_reg():
   return render_template('user_reg.html')      



#----register user
@app.route('/user_insert',methods=['post'])                
def user_insert():
   name = request.form['name']
   number = request.form['number']
   email = request.form['email']
   password = request.form['password']  
   t = (name,number,email,password)
   insert_user(t)
   return redirect('/user_login')



#----user login                                                        
@app.route('/check_user_login',methods=['post'])                   
def check_user_login():
   email = request.form['email']
   password = request.form['password']
   t = (email,password)
   t1 = user_log_check(email)
   if t in t1:
      return redirect("/index")
   else:
      return redirect('/')



#----forget4    for user
@app.route('/user_forget')                                  
def user_forget():
   return render_template('user_forget.html')


#----change forget password  
@app.route("/forget_user",methods=["post"])                             
def forget_user():
   email = request.form["email"]
   password = request.form["password"]
   t = (password,email)
   user_update_pass(t)
   return redirect("/user_login")



if __name__=='__main__':
   app.run(debug=True)
