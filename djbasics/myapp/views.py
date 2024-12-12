from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import Student , Faculty
from .forms import studentForm , facultyForm

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def aboutpage(request):
    return render(request, "about.html")

def contactpage(request):
    return render(request, "contact.html")

def formpage(request):
    return render(request, "myform.html")
    
def formprocess(request):
    
    name = request.POST['name']
    email = request.POST['email']
    return render(request , "formdata.html"  ,{"name":name , "email":email})

def marksform(request):
    return render(request , "marksform.html")

def resultprocess(request):
    print(request.POST)
    name = request.POST['name']
    maths = int(request.POST['maths'])
    sci = int(request.POST['sci'])
    eng = int(request.POST['eng'])
    avg = int((maths + sci + eng) / 3)
    grade = ''
    if(avg > 90):
        grade = 'A'
    elif(avg > 70):
        grade = 'B'
    else:
        grade='FAIL'
    return render(request, "result.html" , {"name":name , "maths":maths , "sci":sci , "eng":eng , "avg":avg , 'grade':grade})



def addStudent(request):
    if(request.method == "POST"):
        form = studentForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect(addStudent)

    elif(request.method == "GET"):
        context = {'form':studentForm()}
        return render(request, 'addStudent.html' , context)
    


def displayStudetData(request):
    dbdata = Student.objects.all()
    context = {'mydata' : dbdata}
    return render(request , 'displayStudetData.html' , context)



def addFaculty(request):
    if(request.method == "POST"):
        form = facultyForm(request.POST)
        
        if(form.is_valid()):
            form.save()
            return redirect(displayFacultyData)
        else:
            print(form)
            return render(request , 'addFacultyForm.html' , {"form":form} )

    elif(request.method == "GET"):
        context = {'form':facultyForm()}
        return render(request, 'addFacultyForm.html' , context)
    
    

def displayFacultyData(request):
    dbdata = Faculty.objects.all()
    context = {'mydata' : dbdata}
    return render(request , 'displayFacultyData.html' , context)



