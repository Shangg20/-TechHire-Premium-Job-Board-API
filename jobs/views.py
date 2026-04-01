from rest_framework import generics, filters 
from django_filters.rest_framework import DjangoFilterBackend
from .models import JobPosting
from .serializers import JobPostingSerializer
from rest_framework.permissions import AllowAny

class JobPostingList(generics.ListAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['location']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

class JobPostingDetail(generics.RetrieveAPIView):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [AllowAny]

    