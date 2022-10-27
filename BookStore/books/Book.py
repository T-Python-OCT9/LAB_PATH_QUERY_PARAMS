from turtle import title



class Book() :


    def __init__(self , title ,description, author ,publish_date  ) -> None:
        self.title = title
        self.description =description
        self.author = author
        self.publish_date= publish_date

    def print_info(self):
        print(f" This is a brif about the {self.title} , \n this this the Description : \n {self.description} \n , The book was published on {self.publish_date} , By {self.author}")



Object_1 = Book("Harry Potter" , "This global bestseller took the world by storm. So, if you haven’t read J.K. Rowling’s Harry Potter, now may be the time. Join Harry Potter and his schoolmates as this must-read book transports you deep into a world of magic and monsters." , "J.K. Rowling", "1990" )
Object_2 = Book("Harry Potter" , "This global bestseller took the world by storm. So, if you haven’t read J.K. Rowling’s Harry Potter, now may be the time. Join Harry Potter and his schoolmates as this must-read book transports you deep into a world of magic and monsters." , "J.K. Rowling", "1990" )
Object_3 = Book("Harry Potter" , "This global bestseller took the world by storm. So, if you haven’t read J.K. Rowling’s Harry Potter, now may be the time. Join Harry Potter and his schoolmates as this must-read book transports you deep into a world of magic and monsters." , "J.K. Rowling", "1990" )
Object_4 = Book("Harry Potter" , "This global bestseller took the world by storm. So, if you haven’t read J.K. Rowling’s Harry Potter, now may be the time. Join Harry Potter and his schoolmates as this must-read book transports you deep into a world of magic and monsters." , "J.K. Rowling", "1990" )


Book_1= Object_1.print_info()
Book_2= Object_2.print_info()
Book_3= Object_3.print_info()
Book_4= Object_4.print_info()


list_book = [Book_1,Book_2,Book_3,Book_4]
print(list_book)