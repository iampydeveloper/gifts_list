# gifts/forms.py
from django import forms
from .models import Gift, GiftItem

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['gift_text', 'gift_link', 'gift_image']
        widgets = {
            'gift_text': forms.TextInput(attrs={'placeholder': 'Enter gift text'}),
            'gift_link': forms.URLInput(attrs={'placeholder': 'Enter gift link'}),
        }

class GiftItemForm(forms.ModelForm):
    class Meta:
        model = GiftItem
        fields = ['name', 'link', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter gift name'}),
            'link': forms.URLInput(attrs={'placeholder': 'Enter gift URL'}),
        }