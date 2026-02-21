from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import StudySession, StudyActivity, Word, Group, WordReviewItem
from .serializers import (
    StudySessionSerializer,
    WordSerializer,
    GroupSerializer,
    StudyActivitySerializer,
    WordReviewItemSerializer,
)


@api_view(['GET'])
def api_root(request):
    return Response({
        'endpoints': {
            'last_study_session': '/api/dashboard/last_study_session',
            'study_progress': '/api/dashboard/study_progress',
            'quick_stats': '/api/dashboard/quick-stats',
            'study_activities_create': '/api/study-activities (POST)',
            'study_activities': '/api/study-activities/<id>',
            'words_list': '/api/words',
            'word_detail': '/api/words/<id>',
            'groups': '/api/groups',
            'group_words': '/api/groups/<id>/words',
            'study_sessions': '/api/study_sessions',
            'study_session_words': '/api/study_sessions/<id>/words',
            'reset_history': '/api/reset_history (POST)',
            'full_reset': '/api/full_reset (POST)',
            'mark_correct': '/api/study_ses/correct (POST)'
        }
    })


@api_view(['GET'])
def last_study_session(request):
    session = StudySession.objects.order_by('-created_at').first()
    if not session:
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    return Response(StudySessionSerializer(session).data)


@api_view(['GET'])
def study_progress(request):
    total_sessions = StudySession.objects.count()
    total_words = Word.objects.count()
    correct = WordReviewItem.objects.filter(correct=True).count()
    total_reviews = WordReviewItem.objects.count() or 1
    accuracy = round((correct / total_reviews) * 100, 1)
    return Response({
        'total_sessions': total_sessions,
        'total_words_practiced': total_words,
        'overall_accuracy_percent': accuracy,
    })


@api_view(['GET'])
def quick_stats(request):
    # minimal quick stats
    return Response({'today_sessions': 0, 'today_correct': 0, 'today_incorrect': 0, 'next_review_count': 0})


def paginate_qs(request, qs, per_page=100):
    page = int(request.GET.get('page', 1))
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page)
    return page_obj


@api_view(['GET'])
def words_list(request):
    qs = Word.objects.all().order_by('id')
    page_obj = paginate_qs(request, qs, per_page=100)
    return Response({
        'page': page_obj.number,
        'per_page': page_obj.paginator.per_page,
        'total': page_obj.paginator.count,
        'items': WordSerializer(page_obj.object_list, many=True).data,
    })


@api_view(['GET'])
def word_detail(request, pk):
    w = get_object_or_404(Word, pk=pk)
    return Response(WordSerializer(w).data)


@api_view(['GET'])
def groups_list(request):
    qs = Group.objects.all().order_by('id')
    return Response({'groups': GroupSerializer(qs, many=True).data})


@api_view(['GET'])
def group_detail(request, pk):
    g = get_object_or_404(Group, pk=pk)
    data = GroupSerializer(g).data
    return Response(data)


@api_view(['GET'])
def group_words(request, pk):
    g = get_object_or_404(Group, pk=pk)
    qs = g.words.all().order_by('id')
    page_obj = paginate_qs(request, qs, per_page=100)
    return Response({
        'group_id': g.id,
        'page': page_obj.number,
        'per_page': page_obj.paginator.per_page,
        'items': WordSerializer(page_obj.object_list, many=True).data,
    })


@api_view(['GET'])
def study_sessions_list(request):
    qs = StudySession.objects.all().order_by('-created_at')
    page_obj = paginate_qs(request, qs, per_page=100)
    items = [
        { 'id': s.id, 'group_id': s.group_id, 'created_at': s.created_at } for s in page_obj.object_list
    ]
    return Response({ 'page': page_obj.number, 'per_page': page_obj.paginator.per_page, 'total': page_obj.paginator.count, 'items': items })


@api_view(['GET'])
def study_session_detail(request, pk):
    s = get_object_or_404(StudySession, pk=pk)
    return Response(StudySessionSerializer(s).data)


@api_view(['GET'])
def study_session_words(request, pk):
    s = get_object_or_404(StudySession, pk=pk)
    words = [wr.word for wr in s.word_review_items.select_related('word').all()]
    return Response({ 'study_session_id': s.id, 'words': WordSerializer(words, many=True).data })


@api_view(['POST'])
def create_study_activity(request):
    group_id = request.data.get('group_id')
    if not group_id:
        return Response({'error': 'group_id required'}, status=status.HTTP_400_BAD_REQUEST)
    group = get_object_or_404(Group, pk=group_id)
    act = StudyActivity.objects.create(group=group)
    return Response(StudyActivitySerializer(act).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def study_activity_detail(request, pk):
    act = get_object_or_404(StudyActivity, pk=pk)
    sessions = StudySession.objects.filter(study_activity=act).order_by('-created_at')
    data = StudyActivitySerializer(act).data
    data['study_sessions'] = [ { 'id': s.id, 'created_at': s.created_at } for s in sessions ]
    return Response(data)


@api_view(['POST'])
def reset_history(request):
    WordReviewItem.objects.all().delete()
    StudySession.objects.all().delete()
    StudyActivity.objects.all().delete()
    return Response({ 'status': 'ok', 'message': 'history reset' })


@api_view(['POST'])
def full_reset(request):
    WordReviewItem.objects.all().delete()
    StudySession.objects.all().delete()
    StudyActivity.objects.all().delete()
    Group.objects.all().delete()
    Word.objects.all().delete()
    return Response({ 'status': 'ok', 'message': 'full reset completed' })


@api_view(['POST'])
def mark_correct(request):
    # expects study_session_id, word_id, correct
    sid = request.data.get('study_session_id')
    wid = request.data.get('word_id')
    corr = request.data.get('correct')
    if sid is None or wid is None:
        return Response({'error': 'study_session_id and word_id required'}, status=status.HTTP_400_BAD_REQUEST)
    session = get_object_or_404(StudySession, pk=sid)
    word = get_object_or_404(Word, pk=wid)
    wri, created = WordReviewItem.objects.get_or_create(study_session=session, word=word, defaults={'correct': bool(corr)})
    if not created:
        wri.correct = bool(corr)
        wri.save()
    return Response(WordReviewItemSerializer(wri).data)
