from django.shortcuts import render

# Create your views here.
def jinja_print(request):
    d={'a':200,'b':300}
    return render(request,'jinja_print.html',context=d)
