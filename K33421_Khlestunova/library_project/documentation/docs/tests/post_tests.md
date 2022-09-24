## Тесты POST-запросов

    class PostReaderTest(TestCase):
    
        def test_post_reader(self):
            url = reverse('library_app:readercreate')
            data = {'username':'coco', 'password':'1202dda'}
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data['username'], data['username'])
    

    class PostBookTest(TestCase):

        def test_post_book(self):
            url = reverse('library_app:bookcreate')
            data = {'title':'s', 'authors':'bb', 'publisher':'pp', 'publication_year':2010, 'genre':'Sci-Fi', 
            'book_cypher':'1234567890', 'book_hall': [], 'book_reader':[]}
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data['title'], data['title'])

    class PostTakeOutTest(TestCase):

        @classmethod
        def setUpTestData(cls):
            Book.objects.create(title='s', authors='bb', publisher='pp', publication_year=2010, genre='Sci-Fi', 
            book_cypher='1234567890')
            reader.objects.create(username='coco', password='1202dda')
    
        def test_post_takeout(self):
            url = reverse('library_app:takeoutcreate')
            data = {'book':1, 'reader':1}
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(response.data['reader'], data['reader'])
