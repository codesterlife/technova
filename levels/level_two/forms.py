from django import forms

class Hexahue(forms.Form):
    answer = forms.CharField(label="answer", help_text="answer should be in the format: TEVA{answer}", required=True)