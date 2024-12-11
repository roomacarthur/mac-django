from django.contrib import admin
from django.urls import path, include 
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),
    path('chat/', include('chat.urls')),
    path('blog/', include('blog.urls')),
    path('social/', include('social.urls')),
    path('booking/', include('booking.urls'))
] + debug_toolbar_urls()
