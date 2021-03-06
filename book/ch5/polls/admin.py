from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    # Change order to show
    # fields = ['pub_date', 'question_text']

    # Separate fields to show
    # fieldsets = [
    #     ('Question Statement', {'fields': ['question_text']}),
    #     ('Date Information', {'fields': ['pub_date']}),
    # ]

    # Collapse fields to show
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]

    # To show many FKs at the same time
    inlines = [ChoiceInline]

    # To show additional info
    list_display = ('question_text', 'pub_date')

    # To show filter options
    list_filter = ['pub_date']

    # To add search field
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
