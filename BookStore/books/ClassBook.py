'''
Note : Create a calss to represent a book, the book should have the follwoing attributes :

Class Book
title
description
author
publish_date

Create several books , add them to a books list to accomplish this project.

'''



from sqlite3 import Date

class BookClass:
    def __init__(self, title, description, author, publish_date ) -> None:
        self.title = title
        self.description = description
        self.author = author
        self.publish_date = publish_date

    def printBookDetails(self):
        print(f"Title \t\t\t Description \t\t\t Author \t\t\t Publish Date")
        return f"{self.title}\t\t\t{self.description}\t\t\t{self.author}\t\t\t{self.publish_date}"
        return (f"<center>Title:{self.title}<br> Description:{self.description}<br>Author:{self.author}<br>Publish Date:{self.publish_date}<br></ceenter>")

ز = BookClass("Secrets of The Millionaire Mind", "Develop a culture of financial freedom among people", "T.Harv Eker", "2005")
bk2 = BookClass("Out of The Maze", "Develop innovative ideas for self-development", "Spencer Johnson", "1998")
bk3 = BookClass("Atomic Habits", "atomic habits book", "James Clear", "2018")

book1 = bk1.printBookDetails()
book2 = bk2.printBookDetails()
book3 = bk3.printBookDetails()
book3 = bk3.printBookDetails()

books = [book1, book2, book3]
