# Library-Management-System

[ Technology Used :- HTML, BootStrap, CSS, Python, FLask, JavaSCript, Microsoft SQL Server. ]

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
__Data Base Configuration :-__

---for login user data
---info Table

CREATE TABLE [info](
	[Name] [varchar](30),
	[Number] [bigint],
	[Email] [varchar](30),
	[Password] [varchar](30)
);



---ALL books data will store here from APi
---All_books

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



---ALL member who took books their details saved here
---Member

CREATE TABLE [Member](
	[Member_Id] [int] IDENTITY(1,1),
	[Member_Name] [varchar](100),
	[Book_id] [int],
	[Fees] [decimal](10, 2)
	);

-----------------------------------------------------------------------------------------------------------------------------------------------------------------



-----__[ Initial Screen of Library Management APP ]__----------
<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/605aa269-d596-48f1-8267-7decc36cfc1a">

<br><br><br>

-----__[ User Login SCreen ]__----------
<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/11e39f01-8ac1-44da-beff-5e9c8cb501c4">

<br><br><br>

-----__[ Home page of app ]__----------
<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/66978171-5426-462f-8ffc-23509e911ec5">

<br><br><br>

-----__[ all books details SCreen ]__----------
<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/82955c2e-b797-426f-81b5-6302ecb2586c">



<br><br><br>

-----__[ all member details SCreen ]__----------
<img width="960" alt="image" src="https://github.com/sunilchaudhary1998/Library-Management-System/assets/107506936/b6885c33-8af1-4ccf-a44e-09082a9df6e3">


<br><br><br>


