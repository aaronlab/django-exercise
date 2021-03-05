from django.contrib import admin

from polls.models import Question, Choice

admin.register(Question)
admin.register(Choice)
