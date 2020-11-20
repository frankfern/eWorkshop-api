from django import forms

class BaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for item in self.fields:
            self.fields[item].widget.attrs.update({
                'class': 'form-control'
            })
