from django import forms

licenses = (('GPL','GPL'),('LGPL','LGPL'))

class Creat_project_form(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget = forms.widgets.Textarea)
    license = forms.ChoiceField(widget = forms.widgets.Select, choices = licenses)
    site = forms.URLField()
