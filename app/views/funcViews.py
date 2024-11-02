from app.models import Student
from django.shortcuts import render
def homePage(request):
    students = Student.objects.all()
    
    context = {
        'students': students,
        'message': 'Function Based View'
    }
    
    return render(request, 'home.html', context)