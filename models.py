from django.db import models

# Create your models here.
class user(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	zip=models.CharField(max_length=100);
	gender=models.CharField(max_length=100);
	age=models.CharField(max_length=100);
class urls(models.Model):
	url=models.CharField(max_length=1000);
	score=models.FloatField()
	
class tfidfsc(models.Model):
	url=models.CharField(max_length=1000);
	score=models.FloatField()
class lda(models.Model):
	url=models.CharField(max_length=1000);
	score=models.FloatField()
	
	