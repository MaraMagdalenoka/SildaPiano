from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Vārds', max_length=50, required=True, help_text='*')
    last_name = forms.CharField(label='Uzvārds', max_length=50, required=True, help_text='*')
    email = forms.EmailField(label='E-pasts', max_length=110, required=True, help_text='*')
    phone_num = forms.CharField(label='Telefona numurs', max_length=100, required=True, help_text='*')
    birth_date = forms.DateField(label='Dzimšanas diena', required=False, help_text=
    'GGGG-MM-DD Ja gribi labāk iepazīties un saņemt par vienu dzimšanas dienas apveikumu vairāk! :)')
    description = forms.CharField(label='Tavs raksturojums', max_length=1000, required=False,
                                  help_text='Pastāsti man par sevi, ja vēlies! :)')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_num',
                  'birth_date', 'description', 'password1', 'password2')

