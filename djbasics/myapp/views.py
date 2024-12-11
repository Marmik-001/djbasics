from django.shortcuts import render
from django.http import HttpResponse

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