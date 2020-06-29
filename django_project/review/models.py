from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    lecturer = models.CharField(max_length=200, default='Mr. John Doe')
    
    def average_rating(self):
        return self.post_set.aggregate(Avg('rating'))['rating__avg']
        
    def __str__(self):
        return self.name

class Post(models.Model):
	RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

	title = models.CharField(max_length = 100)
	course = models.ForeignKey('Course', on_delete = models.DO_NOTHING)
	content = models.TextField()
	date_posted = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	rating = models.IntegerField(choices=RATING_CHOICES, default=5)

	def __str__(self):
		return self.title

