from django.urls import path
from .views import *

urlpatterns = [
    path('', catalog_page),
    path('add_comment/', add_comment_page, name='add_comment_page'),
    path('thanks/', thanks_page, name="thanks_page"),

]