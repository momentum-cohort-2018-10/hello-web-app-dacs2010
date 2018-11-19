from registration.backends.simple.views import RegistrationView


# so this is a subclass, gonna rewrite portion
class MyRegistrationView(RegistrationView):
    success_url = 'registration_create_thing'
