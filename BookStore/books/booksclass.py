class book :

    def __init__(self,title,description,author,publish_date) -> None:
        self.title = title 
        self.description = description
        self.author = author
        self.publish_date = publish_date

    def printBookDetails(self):
        print(f"Title \t\t\t Description \t\t\t Author \t\t\t Publish Date")
        return f"\ntitle :{self.title}\ndescription : {self.description}\nauthor : {self.author}\npublish date : {self.publish_date}\n"    

