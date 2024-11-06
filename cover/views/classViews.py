from django.views.generic import ListView
from cover.models import Student

class StudentListView(ListView):
    """
    View to display a list of all students.
    """
    model = Student
    template_name = 'home.html' 
    context_object_name = 'students'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Class Based View'  # Additional context variable
        return context