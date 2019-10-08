from django.urls import path, include
from . import views as v
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'languages', v.LanguageView)

urlpatterns = [
    path('', include(router.urls))
]