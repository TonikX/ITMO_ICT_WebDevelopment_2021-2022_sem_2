## Тесты на GET-запросы

Проверяют, проходят ли GET-запросы и соответствуют ли результаты значениям созданных внутри тестов объектов

    class GetBookTest(TestCase):

        @classmethod
        def setUpTestData(cls):
            Book.objects.create(title='s', authors='bb', publisher='pp', publication_year=2010, genre='Sci-Fi', 
            book_cypher='1234567890')
    
        def test_create_book(self):
            url = reverse('library_app:books', args=[1])
            data = {'id':1, 'title':'s', 'authors':'bb', 'publisher':'pp', 'publication_year':2010, 'genre':'Sci-Fi', 
            'book_cypher':'1234567890', 'book_hall': [], 'book_reader':[]}
            response = self.client.get(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['title'], data['title'])

    class GetReaderTest(TestCase):

        @classmethod
        def setUpTestData(cls):
            reader.objects.create(username='ya', password='20201211ty')
    
        def test_user_creation(self):
            url = reverse('library_app:readers', args=[1])
            data = {'id':1, 'username':'ya', 'password':'20201211ty'}
            response = self.client.get(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['password'], data['password'])
    
    class GetReaderBook(TestCase):

        @classmethod
        def setUpTestData(cls):
            read = reader.objects.create(username='ya', password='20201211ty')
            book = Book.objects.create(title='s', authors='bb', publisher='pp', publication_year=2010, genre='Sci-Fi', 
            book_cypher='1234567890')
            ReaderBook.objects.create(reader=read, book=book)
    
        def test_readerbook_creation(self):
            url = reverse('library_app:readerbook', args=[1])
            data = {'id':1, 'reader':1, 'book':1}
            response = self.client.get(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['reader']['id'], data['reader'])