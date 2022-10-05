import json

from django.test import TestCase
from rest_framework import status
from django.urls import reverse

from hotel.models import Room, Guest, Staff

class RoomModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Room.objects.create(number='1', type=1, price = 1, floor = 1).cleaners.set(Staff.objects.filter())

    def test_number_label(self):
        room = Room.objects.get()
        field_label = room._meta.get_field('number').verbose_name
        self.assertEquals(field_label, 'Room Number')

    def test_floor_label(self):
        room = Room.objects.get()
        field_label = room._meta.get_field('floor').verbose_name
        self.assertEquals(field_label, 'Floor Number')

    def test_price_label(self):
        room = Room.objects.get()
        field_label = room._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'Price')

    def test_room_type_label(self):
        room = Room.objects.get()
        field_label = room._meta.get_field('type').verbose_name
        self.assertEquals(field_label, 'Room Type')

    def test_get_room(self):
        url = reverse('room-detail', args=[1])
        
        data = {"number": '1', "type": '1', "price": 1, "floor": 1, 'cleaners': []}
        
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.json(), data)
        

    def test_post_room(self):
        url = reverse('room-list')
        
        data = {"number": '2', "type": '1', "price": 1, "floor": 1, 'cleaners': []}
        
        response = self.client.post(url, data, format='json')

       
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)
        

    def test_put_room(self):
        url = reverse('room-detail', args=[1])
        
        data = {"number": '1', "type": '2', "price": 1, "floor": 1, 'cleaners': []}
       
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)
        


class GuestModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Room.objects.create(number=1, type=1, price = 1, floor = 1).cleaners.set(Staff.objects.filter())
        Guest.objects.create(passport_number = '123456', name = 'Oleg', surname = 'Layok', middlename = 'Vladimirovich', from_location = 'Russia', room = Room.objects.get())

    def test_name_label(self):
        guest = Guest.objects.get(id=1)
        field_label = guest._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Guest Name')

    def test_surname_label(self):
        guest = Guest.objects.get(id=1)
        field_label = guest._meta.get_field('surname').verbose_name
        self.assertEquals(field_label, 'Guest Surname')

    def test_name_label(self):
        guest = Guest.objects.get(id=1)
        field_label = guest._meta.get_field('middlename').verbose_name
        self.assertEquals(field_label, 'Guest Middlename')

    def test_passport_number_label(self):
        guest = Guest.objects.get(id=1)
        field_label = guest._meta.get_field('passport_number').verbose_name
        self.assertEquals(field_label, 'Passport Number')

    def test_from_location_label(self):
        guest = Guest.objects.get(id=1)
        field_label = guest._meta.get_field('from_location').verbose_name
        self.assertEquals(field_label, 'Guest Location')    

    def test_check_in_date_label(self):
        guest = Guest.objects.get(id=1)
        field_label = guest._meta.get_field('check_in_date').verbose_name
        self.assertEquals(field_label, 'Guest Check-in Date')

    def test_check_out_date_label(self):
        guest = Guest.objects.get(id=1)
        field_label = guest._meta.get_field('check_out_date').verbose_name
        self.assertEquals(field_label, 'Guest Check-out Date')

    def test_prev_check_out_date_label(self):
        guest = Guest.objects.get(id=1)
        field_label = guest._meta.get_field('prev_check_out_date').verbose_name
        self.assertEquals(field_label, 'Previous Guest Check-out Date')

    def test_get_guest(self):
        url = reverse('guest-detail', args=[1])
        
        data = {'id':1, 'passport_number':'123456', 'name':'Oleg', 'surname':'Layok', 'middlename':'Vladimirovich', 'from_location':'Russia', 'check_in_date': '2022-10-02', 'check_out_date': '2022-10-02', 'prev_check_out_date': '2022-10-02', 'room':'1'}
        
        response = self.client.get(url, format='json')

        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.json(), data)
        

    def test_post_guest(self):
        url = reverse('guest-list')
        
        data = {'id':2,'passport_number':'546412', 'name':'Oleg', 'surname':'Layok', 'middlename':'Vladimirovich', 'from_location':'Russia', 'check_in_date': '2022-10-02', 'check_out_date': '2022-10-02', 'prev_check_out_date': '2022-10-02', 'room':'1'}

        
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)
        

    def test_put_guest(self):
        url = reverse('guest-detail', args=[1])
        
        data = {'id':1,'passport_number':'654321', 'name':'Oleg', 'surname':'Layok', 'middlename':'Olegovich', 'from_location':'England',  'check_in_date': '2022-10-02', 'check_out_date': '2022-11-02', 'prev_check_out_date': '2022-10-02', 'room':'1'}

        response = self.client.put(url, data=data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)

    def test_delete_guest(self):
        url = reverse('guest-detail', args=[1])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
        


class StaffModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Staff.objects.create(name="Ivan", phone='+79765776789')

    def test_name_label(self):
        staff = Staff.objects.get(id=1)
        field_label = staff._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Staff Full Name')

    def test_phone_label(self):
        staff = Staff.objects.get(id=1)
        field_label = staff._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'Staff Phone Number')

    def test_get_staff(self):
        url = reverse('staff-detail', args=[1])
        

        data = {"id": 1, "name": "Ivan", "phone": "+79765776789"}
        
        response = self.client.get(url, format='json')

        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.json(), data)
        

    def test_post_staff(self):
        url = reverse('staff-list')
        data = {"id": 2, "name": "Oleg", "phone": "+75555555555"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), data)

    def test_put_staff(self):
        url = reverse('staff-detail', args=[1])
        data = {"id": 1, "name": "Irena", "phone": "+79765776789"}
        response = self.client.put(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)