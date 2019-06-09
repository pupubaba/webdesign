from django import forms
from .models import Notice,Free,Tip

class NoticeForm(forms.ModelForm):
    
    class Meta:
        model = Notice
        fields = ("title","text")

class FreeForm(forms.ModelForm):
    
    class Meta:
        model = Free
        fields = ("title","text")

class TipForm(forms.ModelForm):
    
    class Meta:
        model = Tip
        fields = ("title","text")