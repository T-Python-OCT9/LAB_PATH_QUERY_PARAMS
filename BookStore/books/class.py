class Book:
    def __init__(self,title :str ,description :str ,author :str , publish_date : str) -> None:
        self.title=title
        self.description=description
        self.author=author
        self.publish_date=publish_date


book1=Book("The Great Gatsby","The Great Gatsby is a story told by Nick Carraway, who was once Gatsby's neighbor, and he tells the story sometime after 1922, when the incidents that fill the book take place. As the story opens, Nick has just moved from the Midwest to West Egg, Long Island, seeking his fortune as a bond salesman..","F. Scott Fitzgerald","April 1925")
book2=Book("Anna Karenina by Leo Tolstoy","  ","Greta Garbo","1878")

books_list = [book1.title,book2.title]
books=[book1,book2]