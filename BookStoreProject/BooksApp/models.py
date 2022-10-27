from django.db import models

# Create your models here.
class Book():
    def __init__(self, title : str ,description : str , author : str , publish_date : str) -> None:
        self.title = title
        self.description = description
        self.author = author
        self.publish_date = publish_date

