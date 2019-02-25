class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        adress.email = address
        return "former {} email has been change to {}".format(self.email,adress.mail)

    def __repr__(self):
        return "User {}, email: {}, books read : {}".format(self.name,self.email,int(len(self.books)))


    def __eq__(self, other_user):
        if isinstance(other, self.__class__):
            return self.email == other_user.email and self.name == other_user.name
        return False
    
    def __ne__(self, other_user):
        return self.email != other_user.email or self.name != other_user.name
    
    def read_book(self, book, rating=None):
        self.book = book
        self.books[book] = rating
        
    def get_average_rating(self):
        average = 0
        for rating in self.books.values():
            average += rating
            average = average / len(self.books)
        return average
        
a = User()
User_Init_method = a.__init__()
User_Read_Book_method = a.read_book()


        
        
    
class Book(object):
    def __init__(self ,title ,isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self,new_isbn):
        self.new_isbn = new_isbn
        return "former {} email has been change to {}".format(int(self.isbn),int(self.new_isbn))
    
    def add_rating(self,rating):
        self.rating = rating
        if self.rating >= 0 and self.rating <= 4:
            self.rating += rating
        else:
            return "Invalid Rating"
    
    def __eq__(self, other_book):
        if isinstance(other, self.__class__):
            return self.title == other_book.title and self.isbn == other_book.isbn
        return False
    
    def __ne__(self, other):
        return self.title != other_book.title or self.isbn != other_book.isbn
    
    def get_average_rating(self):
        average = 0
        for rating in self.ratings:
            average += rating
            average = average / len(self.ratings)
        return average
    
    def __hash__(self):
        return hash((self.title, self.isbn))

b = Book(self.title, self.isbn)
Book_Add_Rating_method = b.add_rating()
    

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title,isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{} by {}".format(self.title,self.author)

    
class Non_Fiction(book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title,isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{}, a {level} manual on {}".format(self.title,self.level,self.subject)
    
    

    
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
        
    def create_book(self, title, isbn):
        self.title = title
        self.isbn = isbn
        New_Book = Book(self.title, self.isbn)
        return New_Book
    
    def create_novel(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        New_Fiction = Fiction(self.title, self.author, self.isbn)
        return New_Fiction
    
    def create_non_fiction(self, title, subject, level, isbn):
        self.title = title
        self.subject =subject
        self.level = level
        self.isbn = isbn
        New_Non_Fiction = Non_Fiction(self.title, self.subject, self.level, self.isbn)
        return New_Non_Fiction
    
    def add_book_to_user(self, book, email, rating=None):
        self.book = book
        self.email = email
        Email_from_User = User_Init_method(email)
        for email in Email_from_User:
            if add_book_to_user(email) != Email_from_User:
                return "No user using that email {}!".format(self.email)
            else:
                User_Read_Book_method(book, rating)
                Book_Add_Rating_method(book, rating)    
 


    def add_user(self, name, email, user_books=None):
        self.name = name
        self.email = email
        self.user = (name, email)
        if not user_books == None:
            for self.user in user_books:
                TomeRater.add_book_to_user(self.user)                
                
    def print_catalog(self):
        for keys in self.books:
            print(keys)
    
    def print_users(self):
        for user in self.users:
            print(user)
            
    def most_read_book(self):
        book_value = []
        for book in self.books:
            book_value.append(self.books.values())
            book_value.append(self.books.values())
        return max(book_value)
    
    def highest_rated_book(self):
        highest_average = []
        for book in self.books:
            highest_average.append(book.get_average_rating(self.books[book]))
        return max(highest_average)
    
    def most_positive_user(self):
        best_plus_user = []
        for user in self.users:
            best_plus_user.append(user.get_average_rating(self.users[user]))
        return max(best_plus_user)
    
    def __iter__(self):
        return iter(self.users)
            



        
        
        
        

        
    
    
    
    
    
    
    
    
    
    