from django import forms

class ResetPasswordForm(forms.Form):
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        fields=['password', 'password2']