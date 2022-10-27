from datetime import date
class book :

    def __init__(self, title : str, description : str, author: str, publish_date: date) -> None:
        
        self.__title = title
        self.__description = description
        self.__author = author
        self.__publish_date = publish_date

    
    def describe(self):
        return f"title : {self.getTitle()}, Description: {self.getDescription()}, Author: {self.getAuthor()}, publish date: {self.getPublishDate()}"

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title
    
    def getDescription(self):
        return self.__description

    def getAuthor(self):
        return self.__author

    def getPublishDate(self):
        return self.__publish_date

        
    
