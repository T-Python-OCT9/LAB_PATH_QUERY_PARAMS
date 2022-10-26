from django.db import models

# Create your models here.
class Book:
    def __init__(self, title: str, description: str, author: str, publish_date: str) -> None:
        self.title = title
        self.description = description
        self.author = author
        self.publish_date = publish_date



book1 = Book("Harry Potter and the Sorcerer's Stone", "Harry Potter has no idea how famous he is. That's because he's being raised by his miserable aunt and uncle who are terrified Harry will learn that he's really a wizard, just as his parents were.", 'J.K. Rowling', 'June 26, 1997')
book2 = Book("Animal Farm", "A farm is taken over by its overworked, mistreated animals. With flaming idealism and stirring slogans, they set out to create a paradise of progress, justice, and equality.", 'George Orwell, Russell Baker', 'August 17, 1945')
book3 = Book("The Book Thief", "It is 1939. Nazi Germany. The country is holding its breath. Death has never been busier, and will be busier still.", 'Markus Zusak', 'March 1, 2006')
book4 = Book("Romeo and Juliet", "In Romeo and Juliet, Shakespeare creates a violent world, in which two young people fall in love. It is not simply that their families disapprove; the Montagues and the Capulets are engaged in a blood feud.", 'William Shakespeare', 'January 1, 1597')
book5 = Book("The Giving Tree", "So begins a story of unforgettable perception, beautifully written and illustrated by the gifted and versatile Shel Silverstein.", 'Shel Silverstein', 'January 1, 1964')

books_list = [book1, book2, book3, book4, book5]
