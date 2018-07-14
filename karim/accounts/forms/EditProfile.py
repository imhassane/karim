from django import forms


class EditProfileForm(forms.Form):

    error_css_class = 'uk-form-error'
    required_css_class = 'uk-form-error'

    auto_id = True

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': "Ex: Malik",
        'required': 'false'
    }), required=False)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': "Ex: Ftissi"
    }), required=False)

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'uk-input uk-width-1-1',
        'placeholder': "Ex: monmail@gmail.com"
    }))

    avatar = forms.ImageField(widget=forms.FileInput(attrs={
       'class': 'uk-input uk-width-1-1' 
    }), error_messages={
        'required': "Veuillez choisir une image pour votre profil"
    })
