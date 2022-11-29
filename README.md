# Proyecto2022INGWEB

Nota en el archivo URL.PY del principal, verificar el INCLUDE:


urlpatterns = [
    path("admin/", admin.site.urls),
    path('',templateView),
    path('portofolio-details/', portfolioView),
    path('',include('Apps.Modelo.sub_url')),
    path('api-token-auth/',views.obtain_auth_token,name='api-token-auth'),
]

Que redireccione a las carpetas APPS MODELO y el archivo SUB_URL.PY
