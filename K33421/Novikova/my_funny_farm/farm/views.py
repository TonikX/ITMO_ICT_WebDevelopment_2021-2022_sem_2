from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView, Response
from rest_framework.permissions import IsAuthenticated
from .filters import *
from rest_framework import filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import CustomPagination


# Create your views here.
class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ChickenListAPIView(generics.ListAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = AllChickenRelatedSerializer
    queryset = Chicken.objects.all()
    pagination_class = CustomPagination


class ChickenInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chicken.objects.all()
    serializer_class = ChickenSerializer


class ChickenCreateAPIView(generics.CreateAPIView):
    serializer_class = ChickenSerializer
    queryset = Chicken.objects.all()


class WorkerListAPIView(generics.ListAPIView):
    serializer_class = AllWorkerRelatedSerializer
    queryset = Worker.objects.all()


class WorkerInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerCreateAPIView(generics.CreateAPIView):
    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class BreedListAPIView(generics.ListAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class BreedInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedCreateAPIView(generics.CreateAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class WorkListAPIView(generics.ListAPIView):
    serializer_class = WorkRelatedSerializer
    queryset = Working.objects.all()


class WorkInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Working.objects.all()
    serializer_class = WorkSerializer


class WorkCreateAPIView(generics.CreateAPIView):
    serializer_class = WorkSerializer
    queryset = Working.objects.all()


class CageListAPIView(generics.ListAPIView):
    serializer_class = CageSerializer
    queryset = Cage.objects.all()


class CageInfoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cage.objects.all()
    serializer_class = CageSerializer


class CageCreateAPIView(generics.CreateAPIView):
    serializer_class = CageSerializer
    queryset = Cage.objects.all()


##2.1.1##
class ChickenBreedListAPIView(generics.ListAPIView):
    serializer_class = AllChickenRelatedSerializer

    def get_queryset(self):
        queryset = Chicken.objects.all()
        breed = self.request.query_params.get('breed')
        if breed:
            queryset = queryset.filter(breed=breed)
        return queryset


class ChickenBreedAgeListAPIView(generics.ListAPIView):
    serializer_class = AllChickenRelatedSerializer

    def get_queryset(self):
        queryset = Chicken.objects.all()
        breed = self.request.query_params.get('breed')
        age = self.request.query_params.get('age')
        if breed:
            queryset = queryset.filter(breed=breed)
        if age:
            queryset = queryset.filter(age=age)
        return queryset


class WorkerPositionSalaryListAPIView(generics.ListAPIView):
    serializer_class = AllWorkerRelatedSerializer

    def get_queryset(self):
        queryset = Worker.objects.all()
        if self.request.user.is_authenticated:
            position = self.request.query_params.get('position')
            salary = self.request.query_params.get('salary')
            if position:
                queryset = queryset.filter(position=position)
            if salary:
                queryset = queryset.filter(salary=salary)
        return queryset


##2.1.2##
# class WorkDateOrderListAPIView(generics.ListAPIView):
#     queryset = Working.objects.all()
#     serializer_class = WorkRelatedSerializer
#     filter_backends = (filters.OrderingFilter,)
#     ordering_fields = 'work_date'
#
#
class WorkTypePositionSearchDateOrderListAPIView(generics.ListAPIView):
    queryset = Working.objects.all()
    serializer_class = WorkRelatedSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend)
    ordering_fields = ['work_date']
    filterset_fields = ['work_status']
    search_fields = ('work_type', 'name__position')  # search=med+cleaner
    pagination_class = CustomPagination


class ChickenEggListAPIView(generics.ListAPIView):
    queryset = Chicken.objects.all()
    serializer_class = AllChickenRelatedSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ChickenEggFilter
    pagination_class = CustomPagination


##2.3.1##
class WorkerPhotoCreateView(generics.CreateAPIView):
    queryset = WorkerPhoto.objects.all()
    serializer_class = WorkerPhotoSerializer


class SeveralWorkerPhotosCreateView(generics.CreateAPIView):
    queryset = WorkerPhoto.objects.all()
    serializer_class = WorkerPhotoSerializer

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('file')
        for file in files:
            worker_id = request.POST.get('worker')
            file = WorkerPhoto(
                worker=Worker.objects.get(id=worker_id), file=file)
            file.save()
        return Response(str(request.data), status=status.HTTP_201_CREATED)
