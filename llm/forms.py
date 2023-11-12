from django import forms

class GPTForm(forms.Form):
    user_input = forms.CharField(
        label='Enter your text',
        max_length=1000,
    widget=forms.TextInput(attrs={"id":"myInput", 'class': 'input-group__input', 'placeholder': 'Ask ChatGpt'})
    )
