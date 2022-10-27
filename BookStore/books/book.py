class Book():
    
    def __init__(self, title,description,author,publish_date) -> None:
        self.title = title
        self.description = description
        self.author = author
        self.publish_date = publish_date
    
    def all_info(self):
        return (f" Book name: {self.title} \n Brief about book: {self.description} \n Book Author: {self.author} \n Published in: {self.publish_date}")

b1 = Book("Learn Python in 1 day .", "Presented in a to-the-point and concise style to cater to the busy individual etc..","Jamie Chan .","2015")
b2 = Book("The recursion book of Recursion!.", "course on recursive programming using Python and JavaScript.","Ai sweigat .","2022/Aug/16")
b3 = Book("Clean Code .", "Even bad code can function. But if code isnt clean it can bring a development organization to its knees. ","Robert Cecil Martin .","2008/Aug/1")
b4 = Book("Fluent Python .", " With this hands-on guide, you ll learn how to write effective, idiomatic Python code by leveraging its best and possibly most neglected features .", "Luciano Ramalho .","2015/Jul/24")
b5 = Book("Think like a programmer .", "Programming isn’t just about syntax and assembling code—it’s about problem solving, and all good programmers must think creatively to solve problems ."," V. Anton Sparul .", "2012/Augest")

book1 = b1.all_info()
book2 = b2.all_info()
book3 = b3.all_info()
book4 = b4.all_info()
book5 = b5.all_info()

books_list = [book1, book2, book3, book4, book5]

