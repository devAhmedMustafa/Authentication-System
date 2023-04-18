from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class NewUser(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

    def save(self, commit=False):
        user = super(NewUser, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user