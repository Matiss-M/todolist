from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(
    widget=forms.TextInput(
        attrs={'type': 'text', 'name': 'text', 'placeholder': 'Enter your task'}))