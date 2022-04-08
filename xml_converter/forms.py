from django import forms


class UploadXMLForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    file = forms.FileField()