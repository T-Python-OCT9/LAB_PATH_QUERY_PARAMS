class BookClass:
    def __init__(self, title, description, author, publish_date ) -> None:
        self.title = title
        self.description = description
        self.author = author
        self.publish_date = publish_date
    
    def printBookDetails(self):
        return (f"<center>Title:{self.title}<br> Description:{self.description}<br>Author:{self.author}<br>Publish Date:{self.publish_date}<br></ceenter>")
    
bk1 = BookClass("Moonlight Cove", "Family and friends mean everything", "Sherryl Woods", "2017")
bk2 = BookClass("Moonlight", "Family is everything", "Sherryl Woofs", "2013")
bk3 = BookClass("Moonlight Cove", "friends mean everything", "Sherryl Wolds", "2016")

book1 = bk1.printBookDetails()
book2 = bk2.printBookDetails()
book3 = bk3.printBookDetails()

books = [book1, book2, book3]