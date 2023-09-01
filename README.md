# Library-Management-System

__Technology Used :-__ 

1) __Microsoft SQL Server__
2) __HTML__
3) __BootStrap__
4) __CSS__
5) __Python__
6) __FLask__
7) __JavaSCript__

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

1) To use this app click on library app option.
   
1) Then user login screen will come
2) login over there by using details
   
1) if you dont have an account then register,
2) if you forgot password you can reset it.

1) After login You will redirect to home page of app.
2) There is a button in home page to navigate to all details page.

1) in all book details page there is a button to import all books from API.
2) in action button there is a function to edit details of books.
   
1) when click on issue book button book will get deleted from all book details screen and a pop will come
2) you need to fill a form to whom you want issue this book
3) details will get into all member screen thus one book have been issued to member.
4) thus that book will get deleted from this screen
5) click on member details button in navigation bar to see all member details. to whom book has been issued.

1) when you click on delete option in member details screen record will delete this means that book has been returned by member to libray.
2) so that member details will get deleted from this screen.
3) And now that book id details will again can see from all books details screen that means book has been arrived at Libray again.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

~~~

Data Base Configuration :-     -----------(make sure you use Microsoft sql server for data storage)

---for login user data
---info Table

CREATE TABLE info
(
	[Name] [varchar](30),
	[Number] [bigint],
	[Email] [varchar](30),
	[Password] [varchar](30)
);

-----------------------------------------------------------------------------------------------------------

---ALL books data will store here from APi
---All_books

CREATE TABLE All_books
(
	[Book_id] [int] IDENTITY(1,1),
	[title] [varchar](100),
	[authors] [varchar](500),
	[average_rating] [decimal](10, 2),
	[isbn] [varchar](500),
	[isbn13] [varchar](500),
	[language_code] [varchar](50),
	[num_pages] [int],
	[ratings_count] [int],
	[text_reviews_count] [int],
	[publication_date] [date],
	[publisher] [varchar](100),
	[is_deleted] [int],
	[is_issued] [int] 
);

-----------------------------------------------------------------------------------------------------------

---ALL member who took books their details saved here
---Member

CREATE TABLE Member
(
	[Member_Id] [int] IDENTITY(1,1),
	[Member_Name] [varchar](100),
	[Book_id] [int],
	[Fees] [decimal](10, 2)
	);


~~~



~~~
[ Initial Screen of Library Management APP ]

1) To use this app click on library app option.
~~~

<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/87e6f83d-64e5-4bce-97d0-0d9b69db81cb">




-----------------------------------------------------------------------------------------------------------------------------------------------------------------
~~~
[ User Login SCreen ]

1) Then user login screen will come
2) login over there by using details
3) if you dont have an account then register,
4) if you forgot password you can reset it.
~~~

<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/11e39f01-8ac1-44da-beff-5e9c8cb501c4">

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

~~~
[ Home page of app ]

1) After login You will redirect to home page of app.
2) There is a button in home page to navigate to all details page.
~~~

<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/66978171-5426-462f-8ffc-23509e911ec5">

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
~~~
[ all books details Screen ]

1) in all book details page there is a button to import all books from API.
2) in action button there is a function to edit details of books.
3) There is a Add New Book Button by which we can enter new book into data base manually as like api button.
4) If any student come and ask for book we can check whether that book is available in our libray by Search Single Book Info button
~~~

<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/dde9e091-8cb9-4329-8fe7-282b34f1378e">



-----------------------------------------------------------------------------------------------------------------------------------------------------------------
~~~
[Pop Up Screen]


1) when click on issue book button book will get deleted from all book details screen and a pop will come
2) you need to fill a form to whom you want issue this book
3) details will get into all member screen thus one book have been issued to member.
4) thus that book will get deleted from this screen
5) click on member details button in navigation bar to see all member details. to whom book has been issued.
~~~

<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/576d6483-cc86-4112-9a00-e8bc532e5662">


------------------------------------------------------------------------------------------------------------------------------------------------------------------
~~~
[ all member details SCreen ]

1) when you click on delete option in member details screen record will delete this means that book has been returned by member to libray.
3) so that member details will get deleted from this screen.
4) And now that book id details will again can see from all books details screen that means book has been arrived at Libray again.
~~~
<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/b6885c33-8af1-4ccf-a44e-09082a9df6e3">

------------------------------------------------------------------------------------------------------------------------------------------------------------------
~~~
[ Single Book Info Check ]

1) If any student come and ask for book we can check whether that book is available in our libray by Search Single Book Info button
~~~
<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/cae2af1e-5589-4547-a915-956da184e42a">

~~~

___Note :- Type the Spelling of Book Properly to Search sown below___

~~~
<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/3b0ba8c9-f65b-4857-9562-f29c2dc28d75">

------------------------------------------------------------------------------------------------------------------------------------------------------------------
~~~
[ Single Book Information ]

1) Checking and Retrieving details related to any one book that is present in library or not
2) so that we can recomend to customer
~~~
<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/3eb268a2-ccbb-4dfa-afe4-308be8343943">

------------------------------------------------------------------------------------------------------------------------------------------------------------------


