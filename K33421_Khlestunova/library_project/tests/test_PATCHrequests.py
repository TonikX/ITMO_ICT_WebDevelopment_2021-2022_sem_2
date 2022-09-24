from django.test import TestCase
from django.urls import reverse
from rest_framework import status
import json
from library_app.models import Book, reader, Log

class PatchBookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='s', authors='bb', publisher='pp', publication_year=2010, genre='Sci-Fi', 
            book_cypher='1234567890')
    
    def test_patch_book(self):
        url = reverse('library_app:bookedit', args=[1])
        data = json.dumps({'title':'l'})
        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'l')

class PatchLogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Log.objects.create(deleted='lskss')
    
    def test_patch_reader_book(self):
        url = reverse('library_app:logedit', args=[1])
        data = json.dumps({'deleted':'222 Gff'})
        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['deleted'], '222 Gff')

class PatchReaderTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        reader.objects.create(username='username', password='badpassword')
    
    def test_patch_reader(self):
        url = reverse('library_app:readeredit', args=[1])
        data = json.dumps({'password':'goodpassword'})
        response = self.client.patch(url, data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['password'], 'goodpassword')