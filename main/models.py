from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Performance(models.Model):
    title = models.CharField(max_length=100)
    age_limit = models.IntegerField(default=0)
    description = models.TextField()
    photo = models.ImageField(upload_to='performances_photos/', default='performances_photos/default.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='name')  # Указываем поле 'name' для представления объекта категории

    def __str__(self):
        return f"{self.title} (ID категории: {self.category_id})"


from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})
