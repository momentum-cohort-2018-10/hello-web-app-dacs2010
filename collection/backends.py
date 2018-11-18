from registration.views import RegistrationView


# so this is a subclass, gonna rewrite portion
class MyRegistrationView(RegistrationView):
    success_url = 'registration_create_thing'


# class MyRegistrationView(RegistrationView):
#     def get_success_url(user):
#         return success_url = 'registration_create_thing'
