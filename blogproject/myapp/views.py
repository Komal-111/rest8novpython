from django.shortcuts import render
from .forms import blogForm,updateForm
from .models import blog
from datetime import datetime




# Create your views here.
def index (request):
 
 if request.method=='POST':
    blog=blogForm(request.POST)
    if blog.is_valid():
       blog.save()
       print("Your data has been saved!")
    else:
        print(blog.errors)
 return render(request,'index.html')

def update(request,id):
     
    current_time = datetime.now().time()  
    cid=blog.objects.get(id=id)
      
    if request.method=='POST':
        updateuser=updateForm(request.POST)
        if updateuser.is_valid():
            updateuser=updateForm(request.POST,instance=cid)
            updateuser.save()
            print("Your blog has been updated.....")
           
        else:
            print(updateuser.errors)
    return render(request,'update.html',{'user':blog.objects.get(id=id)})




