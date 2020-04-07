from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class ReferenceManager(models.Manager):
	def get_queryset(self):
		return super(ReferenceManager,
			self).get_queryset().filter(abstract__isnull=False)


class Post(models.Model):
	
	title = models.TextField(max_length=500, null=True, blank=True)
	slug = models.SlugField(max_length=500,	unique_for_date='reference', null=True, blank=True)
	authors = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publication_posts', null=True, blank=True)
	abstract = models.TextField(null=True, blank=True)
	published_year = models.CharField(max_length=500, null=True, blank=True)
	published_month = models.CharField(max_length=500, null=True, blank=True)
	journal = models.CharField(max_length=500, null=True, blank=True)
	volume = models.CharField(max_length=500, null=True, blank=True)
	issue = models.CharField(max_length=500, null=True, blank=True)
	published_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
	pages = models.CharField(max_length=500, null=True, blank=True)
	accession_number = models.CharField(max_length=500, null=True, blank=True)
	doi = models.CharField(max_length=500, null=True, blank=True)
	reference = models.CharField(max_length=500, null=True, blank=True)
	covidence_harsh = models.CharField(max_length=500, null=True, blank=True)
	study = models.CharField(max_length=500, null=True, blank=True)
	tags = models.TextField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ('-reference',)

	def __str__(self):
		return self.study

	objects = models.Manager() # The default manager.
	has_abstract = ReferenceManager() # Our custom manager.

	def get_absolute_url(self):
		return reverse('covid_publications:post_detail',
			args=[
				self.study,
				self.slug])
