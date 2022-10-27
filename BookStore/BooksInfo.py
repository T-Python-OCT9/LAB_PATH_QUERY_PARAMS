
class Book:

    def __init__(self ,title:str ,description:str , author:str ,  publish_date:int ) -> None:

        self.title = title
        self.description = description
        self.author = author
        self.publish_date=publish_date

    def book_info(self):
        return f"The book Title {self.title} , Book description {self.description} ,author {self.author} , and publish in {self.publish_date}"


book1 = Book("OverStory" , "....." , " Nathaniel Rich" , 2019)
book2 = Book("Silent Patient" , "...." , "Alex Michaelides" , 2019)
book3 = Book("Verity" , "...." , "Colleen Hoover" , 2022)
book4 = Book("the 5 second Rule" , "...." , "Mel Robbins" , 2022)
book5 = Book("Power of now" , "....." , "Eckhart Tolle" ,2001)

