class Books:

    def __init__(self,name: str,discription: str,author: str,publish_date: str)-> None:
        self.name = name
        self.discription = discription
        self.author = author 
        self.publish_date= publish_date


    def describe(self):
        return f'The Book Name Is: {self.name}, Discription: {self.discription}, Publish Date: {self.publish_date}, Author: {self.author}'