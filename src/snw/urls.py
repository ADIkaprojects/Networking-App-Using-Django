from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_view, undefined

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-view'),
    path('accounts/', include ('allauth.urls')),
    path('profiles/',  include("profiles.urls", namespace='profiles')),
    path('posts/',  include("posts.urls", namespace='posts')),
    path('undefined/', undefined , name='posts'),
]


urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)