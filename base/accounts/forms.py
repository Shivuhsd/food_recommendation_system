from django import forms

class UserRegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    confirm_password = forms.CharField(required=True)

    def match_password(self):
        if self.password != self.confirm_password:
            return False
        else:
            return True
        

class UserLoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    