from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Event(models.Model):
	event_title = models.CharField(max_length=200)
	event_description = models.TextField(u'Notes', help_text=u'Notes', blank=True, null=True, default="Notes")
	event_start_time = models.DateTimeField("starting time", default=datetime.now)
	event_end_time = models.DateTimeField("ending time", default=datetime.now)

	@property
	def get_html_url(self):
		url = reverse('main:event_edit', args=(self.id,))
		return f'<a href="{url}"> {self.event_title} </a>'