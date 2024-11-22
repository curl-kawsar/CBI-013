from django.contrib import admin

# Register your models here.
from .models import Problem, TestCase, Submission, Contest, BlogTutorial

admin.site.register(Problem)
admin.site.register(TestCase)
admin.site.register(Submission)
admin.site.register(Contest)
admin.site.register(BlogTutorial)