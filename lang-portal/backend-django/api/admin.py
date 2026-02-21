from django.contrib import admin
from .models import Word, Group, StudySession, StudyActivity, WordReviewItem

admin.site.register(Word)
admin.site.register(Group)
admin.site.register(StudyActivity)
admin.site.register(StudySession)
admin.site.register(WordReviewItem)
