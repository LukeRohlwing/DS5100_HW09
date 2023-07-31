import pandas as pd

class BookLover:
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def add_book(self, book_name, rating):
        if len(self.book_list) == 0:
            new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
                })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        
        else:
            if book_name in self.book_list.book_name.unique():
                print('Book is already in the dataframe')
            else:
                new_book = pd.DataFrame({
                'book_name': [book_name], 
                'book_rating': [rating]
                })

                self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    
    def has_read(self, book_name):
        return book_name in self.book_list.book_name.unique()
    
    def num_books_read(self):
        self.num_books = len(self.book_list)
        return self.num_books
    
    def fav_books(self):
        favs = self.book_list.loc[self.book_list['book_rating'] > 3]
        return favs