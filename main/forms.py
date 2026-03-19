from django import forms
# Create your models here.


class UploadFileForm(forms.Form):
    file = forms.FileField()