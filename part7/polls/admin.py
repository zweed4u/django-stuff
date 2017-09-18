from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	# Order of fileds as seen on http://127.0.0.1:8000/admin/polls/question/1/change/
	# Date published then question text, reorder elements to see difference in position
	#fields = ['pub_date', 'question_text']
	# Now splitting the form into fieldsets
	fieldsets = [
		(None, {'fields':['question_text']}),
		('Date information', {
			'fields':['pub_date'],
			'classes':['collapse']
		})
	]
	inlines = [ChoiceInline]
	list_display = ('question_text','pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)

# Inefficient way of adding choices - do it when we create a question - see above
#admin.site.register(Choice)
