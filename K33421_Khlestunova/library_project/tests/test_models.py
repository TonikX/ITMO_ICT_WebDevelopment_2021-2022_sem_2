from django.test import TestCase
from library_app.models import Book, Log, reader, Hall

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='s', authors='bb', publisher='pp', publication_year=2010, genre='Sci-Fi', 
            book_cypher='1234567890')
    
    def test_correct_title(self):
        book = Book.objects.get(id=1)
        name = book.title
        self.assertEquals(name, 's')
    
    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название')


class LogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Log.objects.create(deleted='aaa')
    

    def test_correct_del(self):
        log = Log.objects.get(id=1)
        deleted = log.deleted
        self.assertEquals(deleted,'aaa')

class ReaderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        reader.objects.create(username='dad', password='ddss11')
    
    def test_username_unique(self):
        read = reader.objects.get(id=1)
        field_unique = read._meta.get_field('username').unique
        self.assertEquals(field_unique,True)