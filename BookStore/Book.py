class Book:
   
    def __init__(self,title:str, description, author:str, publish_date:str) -> None:
        self.title=title
        self.description=description
        self.author=author
        self.publish_date=publish_date



    def printInfo(self):

        return f"\ntitle :{self.title}\ndescription : {self.description}\nauthor : {self.author}\npublish date : {self.publish_date}\n"