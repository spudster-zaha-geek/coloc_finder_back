from api import views
from django.urls import path

urlpatterns = [
    path('create', views.CreateAnnonceAPIView.as_view(), name='create_annonce'),
    path('', views.ListAnnonceAPIView.as_view(), name='list_annonce'),
    path('conditions/create', views.CreateConditionColocationView.as_view(), name='create_condition_colocation'),
    path('conditions', views.ListConditionColocationView.as_view(), name='list_condition_colocation'),
    path('<int:id>', views.AnnoceDetailsView.as_view(), name='details_annonce'),
]