from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import SimpleRouter

from hotel.views import *

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="vladimir27goncharov@icloud.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = SimpleRouter()
router.register(r'admins', AdminAPIView)
router.register(r'rooms', RoomAPIView)
router.register(r'guests', GuestAPIView)
router.register(r'staff', StaffAPIView)
router.register(r'cleaning', CleaningAPIView)
router.register(r'upload-room-picture', UploadRoomPicture)
router.register(r'upload-files', UploadFiles)


urlpatterns = [
    path('', include(router.urls)),
    path('rooms/type/<int:type>/', RoomTypeFilterView.as_view()),
    path('rooms/floor/<int:fl_g>/<int:fl_l>/', RoomFloorsFilterView.as_view()),
    path('rooms/floor-room-type/<int:floor>/<int:type>/', RoomFloorRoomTypeFilterView.as_view()),
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]