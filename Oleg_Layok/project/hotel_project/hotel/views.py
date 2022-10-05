from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.filters import OrderingFilter, SearchFilter, BaseFilterBackend
from django_filters import filters, RangeFilter, DateFromToRangeFilter, ModelMultipleChoiceFilter, NumberFilter, \
    ChoiceFilter, MultipleChoiceFilter
from hotel.models import *
from hotel.serializers import *


class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.num_pages,
            'page': self.page.number,
            'results': data
        })


class AdminAPIView(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAdminUser]


class RoomFilter(FilterSet):
    price = RangeFilter()
    number = RangeFilter()
    type = MultipleChoiceFilter(
        choices=Room.ROOM_TYPE
    )
    class Meta:
        model = Room
        fields = ['price', 'number','type']


class RoomAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = RoomFilter
    filterset_fields = ['price','number','type']
    search_fields = ['number']
    ordering_fields = ['number', 'price']
    pagination_class = CustomPagination

class RoomTypeFilterView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(type=self.kwargs['type'])
        return queryset


class RoomFloorRoomTypeFilterView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.all()
        if not self.request.user.is_anonymous:
            queryset = queryset.filter(floor=self.kwargs['floor'], type=self.kwargs['type'])
        return queryset


class RoomFloorsFilterView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    
    def get_queryset(self):
        queryset = self.queryset.filter(floor__gte=self.kwargs['fl_g'], floor__lte=self.kwargs['fl_l'])
        return queryset


class StaffAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class GuestFilter(FilterSet):
    check_in_date = DateFromToRangeFilter()
    check_out_date = DateFromToRangeFilter()

    class Meta:
        model = Guest
        fields = ['check_in_date','check_out_date']


class GuestAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GuestSerializer
    queryset = Guest.objects.all().order_by('id')

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = GuestFilter
    filterset_fields = ['check_in_date','check_out_date']
    search_fields = ['name','passport_number']
    ordering_fields = ['check_in_date','check_out_date']
    pagination_class = CustomPagination


class CleaningAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CleaningSerializer
    queryset = Cleaning.objects.all()
    pagination_class = CustomPagination

    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ['room__number','staff__name']
    search_fields = ['date_time', "room__number", 'staff__name']
    ordering_fields = ['date_time']
    ordering = ['date_time']


class UploadRoomPicture(viewsets.ViewSet):
    queryset = RoomPicture.objects.all()
    serializer_class = RoomPictureSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        file_uploaded = request.FILES.get('file_uploaded')
        room = request.POST.get('room')
        content_type = file_uploaded.content_type
        file_name = file_uploaded.name
        file_size = file_uploaded.size
        serializer = self.serializer_class(data={"file": file_uploaded, "room": room, "file_size": file_size})
        serializer.is_valid()
        serializer.save(file_name=file_name)
        response = f"POST API and you have uploaded a {content_type} file {file_name}"
        return Response(response)


class UploadFiles(viewsets.ViewSet):
    queryset = RoomPicture.objects.all()
    serializer_class = FileUploadsSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        files = request.FILES.getlist('file')
        file_serializers = []
        for file in files:
            print(file)

            serializer = self.serializer_class(data={"file": file})
            try:
                serializer.is_valid(raise_exception=True)
                file_serializers.append(serializer)
            except ValidationError as err:
                return HttpResponseBadRequest(err)

        for serializer in file_serializers:
            serializer.save()
        response = f"POST API and you have uploaded files"
        return Response(response)
