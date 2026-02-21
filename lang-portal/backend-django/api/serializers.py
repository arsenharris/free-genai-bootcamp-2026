from rest_framework import serializers
from .models import Word, Group, StudySession, StudyActivity, WordReviewItem


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'kanji', 'romaji', 'english', 'parts']


class GroupSerializer(serializers.ModelSerializer):
    words_count = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'name', 'words_count']

    def get_words_count(self, obj):
        return obj.words.count()


class WordReviewItemSerializer(serializers.ModelSerializer):
    word = WordSerializer(read_only=True, source='word')

    class Meta:
        model = WordReviewItem
        fields = ['id', 'word', 'correct', 'created_at']


class StudySessionSerializer(serializers.ModelSerializer):
    word_review_items = WordReviewItemSerializer(many=True, read_only=True)

    class Meta:
        model = StudySession
        fields = ['id', 'group_id', 'study_activity_id', 'created_at', 'word_review_items']


class StudyActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyActivity
        fields = ['id', 'group_id', 'created_at']
