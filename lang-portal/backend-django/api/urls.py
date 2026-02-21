from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('dashboard/last_study_session', views.last_study_session, name='last-study-session'),
    path('dashboard/study_progress', views.study_progress, name='study-progress'),
    path('dashboard/quick-stats', views.quick_stats, name='quick-stats'),

    path('study-activities', views.create_study_activity, name='create_activity'),
    path('study-activities/<int:pk>', views.study_activity_detail, name='study-activity-detail'),
    path('study-activities/<int:pk>/study_sessions', views.study_sessions_list, name='study-activity-sessions'),

    path('words', views.words_list, name='words-list'),
    path('words/<int:pk>', views.word_detail, name='word-detail'),

    path('groups', views.groups_list, name='groups-list'),
    path('groups/<int:pk>', views.group_detail, name='group-detail'),
    path('groups/<int:pk>/words', views.group_words, name='group-words'),
    path('groups/<int:pk>/study_sessions', views.study_sessions_list, name='group-study-sessions'),

    path('study_sessions', views.study_sessions_list, name='study-sessions-list'),
    path('study_sessions/<int:pk>', views.study_session_detail, name='study-session-detail'),
    path('study_sessions/<int:pk>/words', views.study_session_words, name='study-session-words'),

    path('reset_history', views.reset_history, name='reset-history'),
    path('full_reset', views.full_reset, name='full-reset'),
    path('study_ses/correct', views.mark_correct, name='mark-correct'),
]
