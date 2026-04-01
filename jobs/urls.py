from django.urls import path
from .views import JobPostingList, JobPostingDetail

urlpatterns = [
    path('jobs/', JobPostingList.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobPostingDetail.as_view(), name='job-detail'),
]