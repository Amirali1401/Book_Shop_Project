from django import forms

class AddToBooktCartForm(forms.Form):

    QUANTITY_CHOICES = [(str(i),i) for i in range(1,31)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES , coerce=int)
    inplace = forms.BooleanField(required=False , widget = forms.HiddenInput)