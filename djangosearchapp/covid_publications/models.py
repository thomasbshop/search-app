from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class YearManager(models.Manager):
	def get_queryset(self):
		return super(YearManager,
			self).get_queryset().filter(published_year='2020')


class Post(models.Model):
	
	title = models.TextField(max_length=500)
	slug = models.SlugField(max_length=250,	unique_for_date='reference')
	authors = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publication_posts')
	abstract = models.TextField()
	published_year = models.CharField(max_length=250)
	published_month = models.CharField(max_length=250)
	journal = models.CharField(max_length=500)
	volume = models.CharField(max_length=250)
	issue = models.CharField(max_length=250)
	published_date = models.DateTimeField(default=timezone.now)
	pages = models.CharField(max_length=250)
	accession_number = models.CharField(max_length=250)
	doi = models.CharField(max_length=250)
	reference = models.CharField(max_length=250)
	covidence_harsh = models.CharField(max_length=500)
	study = models.CharField(max_length=500)
	tags = models.TextField()
	notes = models.TextField()

	class Meta:
		ordering = ('-reference',)

	def __str__(self):
		return self.study

	objects = models.Manager() # The default manager.
	published = YearManager() # Our custom manager.
