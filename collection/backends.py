from registration.views import RegistrationView

# so this is a subclass, gonna rewrite portion
class MyRegistrationView(RegistrationView):
    def get_success_url(user):
        success_url = 'registration_create_thing'
        return success_url