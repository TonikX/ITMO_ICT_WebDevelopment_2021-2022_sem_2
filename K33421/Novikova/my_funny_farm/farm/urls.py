from django.urls import path
from .views import *

app_name = "farm"

urlpatterns = [
    path('users/list/', UserListAPIView.as_view()),
    path('users/info/<int:pk>', UserInfoAPIView.as_view()),
    #path('users/create/', UserCreateAPIView.as_view()),

    path('chickens/list/', ChickenListAPIView.as_view()),
    path('chickens/info/<int:pk>', ChickenInfoAPIView.as_view(), name='chickens'),
    path('chickens/create/', ChickenCreateAPIView.as_view(), name='chicken_create'),

    path('workers/list/', WorkerListAPIView.as_view()),
    path('workers/info/<int:pk>', WorkerInfoAPIView.as_view(), name='workers'),
    path('workers/create/', WorkerCreateAPIView.as_view(), name='worker_create'),

    path('breeds/list/', BreedListAPIView.as_view()),
    path('breeds/info/<int:pk>', BreedInfoAPIView.as_view(), name='breed_patch'),
    path('breeds/create/', BreedCreateAPIView.as_view(), name='breed_create'),

    path('work/list/', WorkListAPIView.as_view()),
    path('work/info/<int:pk>', WorkInfoAPIView.as_view(), name='working_patch'),
    path('work/create/', WorkCreateAPIView.as_view()),

    path('cage/list/', CageListAPIView.as_view()),
    path('cage/info/<int:pk>', CageInfoAPIView.as_view()),
    path('cage/create/', CageCreateAPIView.as_view()),

    ##2.1.1
    path('chickens_with_breed/', ChickenBreedListAPIView.as_view(), name='chickens_breed'),
    path('chickens_with_breed_age/', ChickenBreedAgeListAPIView.as_view()),
    path('workers_with_position_salary/', WorkerPositionSalaryListAPIView.as_view()),

    ##2.1.2
    path('work_search_date_order/', WorkTypePositionSearchDateOrderListAPIView.as_view()),  #  check
    path('chicken_eggs_range/', ChickenEggListAPIView.as_view()),   #check

    ##2.3.1
    path('upload_worker_photo/', WorkerPhotoCreateView.as_view()),
    path('upload_worker_photos/', SeveralWorkerPhotosCreateView.as_view())

 ]
