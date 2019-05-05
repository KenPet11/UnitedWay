from django.db import models
from datetime import datetime
from django.urls import reverse
from django.core.validators import RegexValidator
from django import forms

# Create your models here.
class Event(models.Model):
	event_title = models.CharField(max_length=200)
	event_description = models.TextField(u'Description', blank=True, null=True, default="Please describe your event.")
	event_start_time = models.DateTimeField(u'Start Time', default=datetime.now)
	event_end_time = models.DateTimeField(u"End time", default=datetime.now)
	event_location = models.CharField(max_length=200, null=True, blank=True)
	event_coordinator = models.CharField(max_length=200)
	event_organization = models.CharField(max_length=200)
	event_contact_email = models.EmailField(max_length=200)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	event_contact_phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	event_link = models.URLField(max_length=200, null=True, blank=True)

	@property
	def get_html_url(self):
		url = reverse('main:event_signup', args=(self.id,))
		return f'<a href="{url}"> {self.event_title} </a>'

	def __str__(self):
		return self.event_title


class Signup(models.Model):
	event_name = models.CharField(max_length=200)
	e_description = models.TextField(u'Description', blank=True, null=True)
	e_start_time = models.CharField(u'Start Time', max_length=200, blank=True, null=True)
	e_end_time = models.CharField(u"End time", max_length=200, blank=True, null=True)
	e_location = models.CharField(u'Location', max_length=200, null=True, blank=True)
	e_coordinator = models.CharField(u'Cordinator', max_length=200, blank=True, null=True)
	e_organization = models.CharField(u'Organization', max_length=200, blank=True, null=True)
	e_contact_email = models.CharField(u'Contact Email', max_length=200, blank=True, null=True)
	e_contact_phone = models.CharField(u'Contact Phone', max_length=17, blank=True) # validators should be a list
	e_link = models.CharField(u'Event Link', max_length=200, null=True, blank=True)

	volunteer_name = models.CharField(max_length=200)
	volunteer_email = models.CharField(max_length=200)
	volunteer_phone = models.CharField(max_length=50, blank=True, null=True)
	volunteer_notes = models.TextField(u'Notes', blank=True, null=True, default="Please leave any other information you would like us to know.")

	@property
	def get_html_url(self):
		url = reverse('main:event_signup', args=(self.id,))
		return f'<a href="{url}"> {self.event_name} </a>'

	def __str__(self):
		return self.event_name + " " + self.volunteer_name