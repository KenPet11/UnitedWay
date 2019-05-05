from django.forms import ModelForm
from django.forms import DateInput
from django.forms import CheckboxInput
from django.forms import EmailInput
from django.forms import URLInput
from main.models import Event
from main.models import Signup

class EventForm(ModelForm):
  class Meta:
    model = Event    
    fields = '__all__'
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'event_start_time': DateInput(attrs={'type': 'datetime-local'}, format=('%Y-%m-%dT%H:%M')),
      'event_end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'event_contact_email' : EmailInput(),
      'event_link' : URLInput(),
    }


  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['event_start_time'].input_formats = ('%Y-%m-%dT%H:%M',)

    self.fields['event_end_time'].input_formats = ('%Y-%m-%dT%H:%M',)

class SignupForm(ModelForm):
  class Meta:
    model = Signup
    fields = '__all__'


  def __init__(self, *args, **kwargs):
    super(SignupForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['event_name'].widget.attrs['readonly'] = True
    self.fields['e_description'].widget.attrs['readonly'] = True
    self.fields['e_start_time'].widget.attrs['readonly'] = True
    self.fields['e_end_time'].widget.attrs['readonly'] = True
    self.fields['e_location'].widget.attrs['readonly'] = True
    self.fields['e_coordinator'].widget.attrs['readonly'] = True
    self.fields['e_organization'].widget.attrs['readonly'] = True
    self.fields['e_contact_email'].widget.attrs['readonly'] = True
    self.fields['e_contact_phone'].widget.attrs['readonly'] = True
    self.fields['e_link'].widget.attrs['readonly'] = True