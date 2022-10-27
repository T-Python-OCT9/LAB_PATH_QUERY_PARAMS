from django.db import models
class Book:
    def __init__(self, title: str, description: str, author: str, publish_date: str) -> None:
        self.title = title
        self.description = description
        self.author = author
        self.publish_date = publish_date

first_book = Book("The Godfather", " The aging patriarch of an organized crime dynasty in postwar New York City transfers control of his clandestine empire to his reluctant youngest son."," Francis Ford Coppola", " 14 March 1972")
second_book = Book("Scent of a Woman"," A prep school student needing money agrees to babysit a blind man, but the job is not at all what he anticipated.","Martin Brest","	23 December 1992")
thierd_book = Book("Forrest Gump"," The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart."," Winston Groom"," 23 June 1994")
books_list = [first_book, second_book, thierd_book]
# Create your models here.
