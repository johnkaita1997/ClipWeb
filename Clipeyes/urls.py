
from django.contrib import admin
from django.urls import path, include

api_version = 'api/v1/'

api_patterns = [
    # path(api_version + 'tokens/', include('tokens.api.urls')),
    path('', include('web.urls')),

]



urlpatterns = api_patterns + [
    path('admin/', admin.site.urls),
]