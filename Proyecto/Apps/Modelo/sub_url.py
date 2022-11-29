
from rest_framework import routers
from Apps.Modelo.api import PagoViewSet
from Apps.Modelo.api import LoginViewSet

router = routers.DefaultRouter()
router.register('api/proyecto',PagoViewSet,'proyecto')
router.register('api/login',LoginViewSet,'login')
urlpatterns= router.urls