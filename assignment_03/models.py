from django.db import models

class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='problems')

    def __str__(self):
        return self.title
    
class TestCase(models.Model):
    input = models.TextField()
    output = models.TextField()
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='test_cases')

    def __str__(self):
        return self.problem.title + ' - ' + str(self.id)

class Submission(models.Model):
    code = models.TextField()
    status = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='submissions')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='submissions')

    def __str__(self):
        return self.user.username + ' - ' + self.problem.title
    
class Contest(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='contests')
    problems = models.ManyToManyField(Problem, related_name='contests')

    def __str__(self):
        return self.name
    
class BlogTutorial(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='blogs_tutorials')
    
    def __str__(self):
        return self.title