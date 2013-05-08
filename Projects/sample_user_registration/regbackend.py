import profile

def user_created(sender, user, request, **kwargs):
	form = profile.UserRegistrationForm(request.POST)
	data = profile.Profile(user=user)		
	data.city_id = form.data["city"]
	data.save()
	
from registration.signals import user_registered
user_registered.connect(user_created)
	