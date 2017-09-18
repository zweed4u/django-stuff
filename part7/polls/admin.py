from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
	# Order of fileds as seen on http://127.0.0.1:8000/admin/polls/question/1/change/
	# Date published then question text, reorder elements to see difference in position
	fields = ['pub_date', 'question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
