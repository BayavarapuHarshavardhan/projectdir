from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        desc=request.POST['desc']

        c = Contact(name=name, phone = phone,email = email,desc=desc)
        c.save()
        with open("user_information.txt","w") as text:
             text1 = text.append((request.POST['name'])+"\n"+(request.POST['phone'])+"\n"+(request.POST['email']))
             
    return render(request,'contact.html')