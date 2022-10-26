from Book import*

book_one=Book("My First Library","something","something","07-02-2015")
book_two=Book("House Plants","something","something","01-01-2020")
book_three=Book("My 1 2 3","something","something","31-09-2022")
book_four=Book("None","something","something","19-11-2009")

bookOne=book_one.printInfo()
bookTwo=book_two.printInfo()
bookThree=book_three.printInfo()
bookFour=book_four.printInfo()

book_list=[bookOne,bookTwo,bookThree,bookFour]

print(book_list)