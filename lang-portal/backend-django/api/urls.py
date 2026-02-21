from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root),
    path('dashboard/last_study_session', views.last_study_session),
    path('dashboard/study_progress', views.study_progress),
    path('dashboard/quick-stats', views.quick_stats),

    path('study-activities', views.create_study_activity, name='create_activity'),
    path('study-activities/<int:pk>', views.study_activity_detail),
    path('study-activities/<int:pk>/study_sessions', views.study_sessions_list),

    path('words', views.words_list),
    path('words/<int:pk>', views.word_detail),

    path('groups', views.groups_list),
    path('groups/<int:pk>', views.group_detail),
    path('groups/<int:pk>/words', views.group_words),
    path('groups/<int:pk>/study_sessions', views.study_sessions_list),

    path('study_sessions', views.study_sessions_list),
    path('study_sessions/<int:pk>', views.study_session_detail),
    path('study_sessions/<int:pk>/words', views.study_session_words),

    path('reset_history', views.reset_history),
    path('full_reset', views.full_reset),
    path('study_ses/correct', views.mark_correct),
]
