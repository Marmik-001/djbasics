from django.forms import ModelForm
from .models import Student , Faculty

class studentForm(ModelForm):
    class Meta:
        model = Student
        field = ["studentName" ,"studentMobile", "studentEmail", "studentPassword"]
        exclude = []


class facultyForm(ModelForm):
    class Meta:
        model = Faculty
        field = ["facultyName" ,"facultyMobile" ,"facultyDepartment"]
        exclude = ["facultyRegistrationDate"]