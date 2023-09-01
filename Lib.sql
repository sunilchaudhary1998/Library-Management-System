# Just Run This file in sql server once and forget it:-


---data base 
create database Library
use Library

--------------------------------------------------------------------------------------------------------

---for login user data
---info Table
CREATE TABLE [info](
	[Name] [varchar](30),
	[Number] [bigint],
	[Email] [varchar](30),
	[Password] [varchar](30)
);

----------------------------------------------------------------------------------------------------------

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

--------------------------------------------------------------------------------------------------------------------
---ALL member who took books their details saved here
---Member
CREATE TABLE [Member](
	[Member_Id] [int] IDENTITY(1,1),
	[Member_Name] [varchar](100),
	[Book_id] [int],
	[Fees] [decimal](10, 2)
	);
----------------------------------------------------------------------------------------------------------------
