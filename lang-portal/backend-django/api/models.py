from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Word(models.Model):
    kanji = models.CharField(max_length=200)
    romaji = models.CharField(max_length=200, blank=True)
    english = models.CharField(max_length=400, blank=True)
    parts = models.JSONField(default=list, blank=True)
    groups = models.ManyToManyField(Group, through='WordGroup', related_name='words')

    def __str__(self):
        return self.kanji or self.english


class WordGroup(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class StudyActivity(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class StudySession(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    study_activity = models.ForeignKey(StudyActivity, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class WordReviewItem(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    study_session = models.ForeignKey(StudySession, on_delete=models.CASCADE, related_name='word_review_items')
    correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
