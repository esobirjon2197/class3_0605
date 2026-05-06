
# 5-m
class Book:
    def __init__(self, title, author, pages, code):
        self.title = title
        self.author = author
        self._pages = pages
        self.__code = code
        self.current = 0
        self.mark = 0

    def read(self, pages):
        self.current += pages

    def bookmark(self, page):
        self.mark = page

    def info(self):
        print(f"Reading {self.current} pages")
        print(f"Bookmark at {self.mark}")


b1 = Book("Python", "Ali", 200, "ABC123")

b1.read(10)
b1.bookmark(50)
b1.info()


# 6-m
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password
        self.status = None

    def login(self, pw):
        self.status = (pw == self.__password)

    def change_password(self, old, new):
        if old == self.__password:
            self.__password = new
            self.status = "Password changed"
        else:
            self.status = False

    def info(self):
        print(self.status)


u1 = User("ali", "ali@gmail.com", "1234")

u1.login("1234")
u1.info()

u1.change_password("1234", "5678")
u1.info()

u1.login("1111")
u1.info()
