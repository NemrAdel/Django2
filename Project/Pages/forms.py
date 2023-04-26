from django import forms
class Ticket(forms.Form):
    F_name=forms.CharField(max_length=20)
    L_name=forms.CharField(max_length=20)
    age=forms.IntegerField()
    idd=forms.IntegerField()
    phone=forms.IntegerField()
    