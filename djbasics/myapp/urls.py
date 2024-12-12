from django.urls import path
from . import views

urlpatterns = [
    path('' , views.homepage ),
    path('home' , views.homepage ),
    path('about' , views.aboutpage ),
    path('contact' , views.contactpage ),
    path('form' , views.formpage),
    path('formprocess' , views.formprocess),
    path('marks' , views.marksform),
    path('resultprocess' , views.resultprocess),
    path('add-student' , views.addStudent),
    path('data-display' , views.displayStudetData),
    path('add-faculty' , views.addFaculty),
    path('faculty-data-display' , views.displayFacultyData)
]