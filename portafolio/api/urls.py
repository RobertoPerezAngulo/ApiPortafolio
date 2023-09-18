from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'register',views.RegisterViewSet)
router.register(r'project',views.ProjectViewSet)
router.register(r'denuncia',views.DenunciaViewSet)
router.register(r'about',views.AboutViewSet)

urlpatterns = [
    path('',include(router.urls))
]