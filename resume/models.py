from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # End date is optional
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    github_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Resume(models.Model):
    file = models.FileField(upload_to='res/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Resume uploaded on {self.uploaded_at}'