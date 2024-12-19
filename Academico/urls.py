from django.urls import path
from .views import *

urlpatterns = [
    path('', home,name='inicio'),
    path('registroCurso/',registroCurso,name='registroCurso'),
    path('eliminarCurso/<codigo>',eliminarCurso,name='eliminarCurso'),
    path('edicionCurso/<codigo>',edicionCurso,name='edicionCurso'),
    path('editarCurso/',editarCurso,name='editarCurso'),
    path('signup/',signup,name='signup'),
    path('signout/',signout,name='signout'),
    path('signin/',signin,name='signin'),
]