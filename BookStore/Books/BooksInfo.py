class Book:
    kind = "object"
    def __init__(self,title:str,description:str,author:str,publish_date:int):
        self.title=title
        self.description=description
        self.author=author
        self.publish_date=publish_date

    def BooksInfo(self)-> str:
        return f"Here is the description for the book {self.title},{self.description}, {self.author} and the publish date is {self.publish_date}" 

no_longer_human = Book("No Longer Human", "is almost symbolic of the predicament of Japanese writers today. It is the story of a man orphaned from his fellows by their refusal to take him seriously. He is denied the f9 love of his father, and taken advantage of by his friends.", "By Osamu Dazai", 1958)

the_setting_sun = Book("The Setting Sun ", "The story centers on an aristocratic family in decline and crisis during the early years after World War II", "By Osamu Dazai", 1947)

harry_potter = Book("Harry Potter", " The novels chronicle the lives of a young wizard, Harry Potter, and his friends Hermione Granger and Ron Weasley, all of whom are students at Hogwarts School of Witchcraft and Wizardry.","J. K. Rowling",1997)

# to print the books atributte
no_longer_human1= no_longer_human.BooksInfo()
the_setting_sun2= the_setting_sun.BooksInfo()
harry_potter3= harry_potter.BooksInfo()

Books_list = [harry_potter,no_longer_human,the_setting_sun]