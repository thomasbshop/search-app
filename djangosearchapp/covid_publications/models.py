from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250,	unique_for_date='reference')
	authors = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publication_posts')
	abstract = models.TextField()
	published_year = models.CharField(max_length=250)
	published_month = models.CharField(max_length=250)
	journal = models.CharField(max_length=250)
	volume = models.CharField(max_length=250)
	issue = models.CharField(max_length=250)
	published_date = models.DateTimeField(default=timezone.now)
	pages = models.CharField(max_length=250)
	accession_number = models.CharField(max_length=250)
	doi = models.CharField(max_length=250)
	reference = models.CharField(max_length=250)
	covidence_harsh = models.CharField(max_length=250)
	study = models.CharField(max_length=250)
	tags = models.TextField()
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
	notes = models.TextField()

	class Meta:
		ordering = ('-reference',)

	def __str__(self):
		return self.study


