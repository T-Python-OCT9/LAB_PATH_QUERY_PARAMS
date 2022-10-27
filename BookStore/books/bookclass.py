class Book:
    def __init__(self , title :str , description:str , author:str ,publish_date:str) -> None:
        self.titel=title
        self.description=description
        self.author=author
        self.publish_date=publish_date


book1=Book("The Secret" , "The book speaks of the low of attraction" , "Ronda Byrne" ,"2006")
book2=Book("Ulysses" , "Is a novel " , "James Joyce" , "1922")
book3=Book("Beauty and the Beast" , "Children stories about a girl","Gabrielle Suzanne" ,"1740")

book_list=[book1.titel,book2.titel,book3.titel]
books=[book1,book2,book3]
