from django import forms
from .models import UserDetail

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['address', 'city', 'country', 'college_attended', 'grades_percentage', 'parents_income', 'first_choice_faculty', 'second_choice_faculty', 'third_choice_faculty', 'achievements']