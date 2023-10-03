from django.urls import path

import web.views as webviews

urlpatterns = [
    path('', webviews.homepage, name='homepage'),
    path('delete/<int:id>', webviews.deleteentry, name='deleteentry'),
]
