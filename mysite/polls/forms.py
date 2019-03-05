from django import forms
from django.forms import ValidationError
from .models import Question
from datetime import datetime
from django.utils import timezone
from datetime import date
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["question_text", "pub_date"]
        
    def clean_question_text(self):
        question_text = self.cleaned_data["question_text"]
        if not question_text.endswith("?"):
            raise ValidationError("Question endswith '?'")
        return question_text

    def clean_pub_date(self):
        pub_date=self.cleaned_data["pub_date"]
        now = timezone.now()
        if now < pub_date:
            raise ValidationError("please enter today date")
        return pub_date



