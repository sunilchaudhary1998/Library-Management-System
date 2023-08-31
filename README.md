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

1) to use this app click on library app option.
2) then user login screen will come login over there by using details, if dont have user data in dba then register, if forget password reset it.
3) after login it will redirect to home page of app.
4) there is button in home page to navigate to all details of books.
5) in all details book there is function to import all books from API.
6) in action option there function to edit details of books
7) when click on issue book function that book will delete from all details screen and a pop will come you need to write details of memeber to whom u will issue bookand this book details will get into all member screen thus one book have been issued to member.
8) member details funtion in navigation bar to see all member details.
9) when you click on delete option in member details screen menans that book has been returned by member to libray so that member detail will deleted from this screen and that book id details will again can see from all books details screen.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
__Data Base Configuration :-__     -----------(make sure you use Microsoft sql server for data storage)

---__for login user data__
---__info Table__

CREATE TABLE [info](
	[Name] [varchar](30),
	[Number] [bigint],
	[Email] [varchar](30),
	[Password] [varchar](30)
);



---__ALL books data will store here from APi__
---__All_books__

CREATE TABLE [All_books](
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



---__ALL member who took books their details saved here__
---__Member__

CREATE TABLE [Member](
	[Member_Id] [int] IDENTITY(1,1),
	[Member_Name] [varchar](100),
	[Book_id] [int],
	[Fees] [decimal](10, 2)
	);

-----------------------------------------------------------------------------------------------------------------------------------------------------------------



__[ Initial Screen of Library Management APP ]__

1) To use this app click on library app option.

<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/605aa269-d596-48f1-8267-7decc36cfc1a">



-----------------------------------------------------------------------------------------------------------------------------------------------------------------

__[ User Login SCreen ]__

1) Then user login screen will come
2) login over there by using details
3) if you dont have an account then register,
4) if you forgot password you can reset it.

<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/11e39f01-8ac1-44da-beff-5e9c8cb501c4">

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

__[ Home page of app ]__

1) After login You will redirect to home page of app.
2) There is a button in home page to navigate to all details page.

<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/66978171-5426-462f-8ffc-23509e911ec5">

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

__[ all books details SCreen ]__

1) in all book details page there is a button to import all books from API.
2) in action button there is a function to edit details of books.

<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/264051de-d46c-40ea-86d3-262b9e88b70a">


-----------------------------------------------------------------------------------------------------------------------------------------------------------------

__[Pop Up Screen]__

1) when click on issue book button book will get deleted from all book details screen and a pop will come
2) you need to fill a form to whom you want issue this book
3) details will get into all member screen thus one book have been issued to member.
4) thus that book will get deleted from this screen
5) click on member details button in navigation bar to see all member details. to whom book has been issued.

<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/576d6483-cc86-4112-9a00-e8bc532e5662">


------------------------------------------------------------------------------------------------------------------------------------------------------------------

__[ all member details SCreen ]__
<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/b6885c33-8af1-4ccf-a44e-09082a9df6e3">

1) when you click on delete option in member details screen record will delete this means that book has been returned by member to libray.
3) so that member details will get deleted from this screen.
4) And now that book id details will again can see from all books details screen that means book has been arrived at Libray again.


