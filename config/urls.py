from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),
    path('chat/', include('chat.urls')),
    path('blog/', include('blog.urls')),
    path('social/', include('social.urls')),
    path('booking/', include('booking.urls'))
]
