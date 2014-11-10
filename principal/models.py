# encoding=utf-8
from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField(max_length=50)
	birth_date = models.DateField(blank=True, null=True)
	slug = models.SlugField(blank=True, null=True)

	def __unicode__(self):
		return '%s' % self.name

	def adults(self):
		if self.age > 18:
			return True
		else:
			return False
	adults.boolean = True
	adults.short_description = 'Es adulto'

	def color(self):
		if self.age > 18:
			return "<b style='color:green;'>Aprobado</b>"
		else:
			return "<b style='color:red;'>Desaprobado</b>"
	color.allow_tags = True


class Category(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name


class Entry(models.Model):
	author = models.ForeignKey(Author)
	category = models.ManyToManyField(Category)
	title = models.CharField(max_length=100)
	content = models.TextField()
	published = models.BooleanField(default = False)

	def __unicode__(self):
		return '%s' % self.title

	def get_age(self):
		return self.author.age

