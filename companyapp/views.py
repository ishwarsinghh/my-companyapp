from django.shortcuts import render

# Create your views here.
def postlist(request):
    return render(request,'companyapp/postlist.html',{})

