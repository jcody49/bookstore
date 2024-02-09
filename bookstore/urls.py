"""
URL configuration for bookstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from sales.views import home, records
# settings allows you to access the MEDIA_URL and MEDIA_ROOT variables that you need to add. 
from django.conf import settings
# static will provide access to the Django helper function static( )
from django.conf.urls.static import static

from .views import login_view, logout_view



urlpatterns = [
    path('admin/', admin.site.urls),
    # specify the name of your FBV
    path('', include('sales.urls')),
    path('books/', include('books.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('records/', records, name='records'),
]

# specifies the URL “/media/” that will trigger this media view (in this case, an image)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
