from django.urls import path
from . import views

app_name = 'covid_publications'
urlpatterns = [
		# post views
		path('', views.post_list, name='post_list'),
		path('<int:reference>/<int:publication_year>/<slug:post>/',
			views.post_detail,
			name='post_detail'),
	]