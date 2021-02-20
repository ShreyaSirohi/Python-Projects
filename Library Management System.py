'''This is a simple Library Management System (LMS).
I have created a class Library which has attributes books and name (Library's name).
Then you have four options: Issue book, Return book, Give book, Delete book
You will get the instructions as you use the program. There will be many updates in it in
future, but this is it for now.
Hope you enjoy it!
Shreya Sirohi
19th October, 2020'''


class Library:

    def __init__(self, books, name):
        self.books = books
        self.name = name
        self.booksdata = {}
        self.secretkey1 = 'oh wait...'
        self.secretkey2 = 'it is a secret!'

    def displaybooks(self):
        print(f"Welcome to {self.name}... We have the following {len(self.books)} books in our library:")

        a = 0
        while a <= len(self.books) - 1:
            print(f"{a + 1}: {self.books[a]}")
            a += 1

    def actiontoperform(self):
        a = 1
        while a == 1:
            ask = input(
                "What do you wanna do...'i' Issue book, 'r' Return book, 'g' Give a book to library, 'd' Delete a book, 'b' Book-User Database, 'l' List of Books, 'q' Quit: ")
            if ask == 'i':
                self.issuebook()
            elif ask == 'r':
                self.returnbook()
            elif ask == 'g':
                self.givebook()
            elif ask == 'd':
                self.deletebook()
            elif ask == 'b':
                self.userbookinfo()
            elif ask == 'l':
                self.displaybooks()
            elif ask == 'q':
                print("Thank you!")
                quit()

    def issuebook(self):
        username = input('Enter your name: ')
        bookname = input(f"Name the book you wanna take, {username}: ")
        if bookname in self.books:
            if bookname not in self.booksdata:
                self.booksdata[bookname] = username
                print(f"OK {username}...Here is your book '{bookname}'")
            else:
                print(f'This book has already been taken by {self.booksdata[bookname]}')
        else:
            print(f"Sorry...we don't have this book in our library.")

    def returnbook(self):
        name = input("Enter your name: ")
        bookname = input('Enter the book name: ')
        print(f"OK {name}...you have given your book '{bookname}' back to the library")
        del self.booksdata[bookname]

    def givebook(self):
        name = input("Enter your name: ")
        bookname = input('Enter the book name: ')
        self.books.append(bookname)

    def deletebook(self):
        name = input("Enter your name: ")
        askkey = input('Enter the secret key: ')
        if askkey == self.secretkey1:
            bookname = input('Name the book you wanna delete: ')
            self.books.remove(bookname)
        else:
            print('Wrong key!')

    def userbookinfo(self):
        askkey = input('Enter the secret key: ')
        if askkey == self.secretkey2:
            print(self.booksdata)
        else:
            print('Wrong key!')


Shreya = Library(['A Christmas Carol', 'Oliver Twist', 'The Secret Garden',
                  'Great Expectations', 'Harry Potter', 'Sherlock Holmes', 'A Tale of Two Cities'], "Shreya's Library")

Shreya.displaybooks()
Shreya.actiontoperform()
