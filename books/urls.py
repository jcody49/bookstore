from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import BookListView, BookDetailView

app_name = 'books'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', BookListView.as_view(), name='book-list'),
    path('list/<pk>', BookDetailView.as_view(), name='detail'),     # <pk> parameter indicates the primary key of the object. 
    path('', include('sales.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
