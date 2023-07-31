#coding=utf-8
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        person1 = BookLover('John', 'test.com', 'Romance')
        test_book = ('book1', 3)
        person1.add_book(*test_book)
        test_value = 'book1' in person1.book_list.book_name.unique()
        self.assertTrue(test_value, 'Book was not successfully added to book_list')
        # add a book and test if it is in `book_list`.

    def test_2_add_book(self):
        person2 = BookLover('John', 'test.com', 'Romance')
        test_book = ('book1', 3)
        person2.add_book(*test_book)
        person2.add_book(*test_book)
        
        duplicateRows = person2.book_list[person2.book_list.duplicated()]
        
        if len(duplicateRows) > 0:
            test_value = False
        else:
            test_value = True
        self.assertTrue(test_value, 'Book was added twice instead of only once')
        # add the same book twice. Test if it's in `book_list` only once.
                
    def test_3_has_read(self): 
        person3 = BookLover('John', 'test.com', 'Romance')
        test_book = ('book1', 3)
        person3.add_book(*test_book)
        
        test_value = person3.has_read('book1')
        
        self.assertTrue(test_value, 'Book was not marked as having been read')
        
        # pass a book in the list and test if the answer is `True`.
        
    def test_4_has_read(self): 
        person4 = BookLover('John', 'test.com', 'Romance')
        test_book = ('book1', 3)
        person4.add_book(*test_book)
        
        test_value = person4.has_read('book2')
        
        self.assertFalse(test_value, 'Book should not have been marked as read')  
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        
    def test_5_num_books_read(self): 
        person5= BookLover('John', 'test.com', 'Romance')
        test_book = ('book1', 3)
        test_book2 = ('book2', 1)
        test_book3 = ('book3', 5)
        
        person5.add_book(*test_book)
        person5.add_book(*test_book2)
        person5.add_book(*test_book3)
        
        expected = 3
        test_val = person5.num_books_read()
        self.assertEqual(test_val, expected, 'Number of books does not match expected')
        # add some books to the list, and test num_books matches expected.

    def test_6_fav_books(self):
        person6 = BookLover('John', 'test.com', 'Romance')
        test_book = ('book1', 3)
        test_book2 = ('book2', 1)
        test_book3 = ('book3', 5)
        test_book4 = ('book4', 4)
        
        person6.add_book(*test_book)
        person6.add_book(*test_book2)
        person6.add_book(*test_book3)
        person6.add_book(*test_book4)
        
        fav_test = person6.fav_books()
        
        test_val1 = len(fav_test[fav_test['book_rating'] <= 3])
        expected1 = 0
        
        test_val2 = len(fav_test[fav_test['book_rating'] > 3])
        expected2 = 2
        
        test = (test_val1, test_val2)
        expected = (expected1, expected2)
        
        self.assertEqual(test, expected, 'Favorite books dataframe do not all have rating > 3')
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)