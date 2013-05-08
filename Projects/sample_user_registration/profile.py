from django import forms
from models import Profile, City
import strings
from registration.forms import RegistrationForm

class ProfileForm(forms.Form):  
  
    city = forms.ModelChoiceField(queryset=City.objects, label=strings.city, empty_label=strings.notDefined)
    
    def save(self, user):
        try:
            data = user.get_profile()
        except:
            data = Profile(user=user)
        data.city = self.cleaned_data["city"]
        data.save()
        
class UserRegistrationForm(RegistrationForm):
    city = forms.ModelChoiceField(queryset=City.objects, label=strings.city, empty_label=strings.notDefined)