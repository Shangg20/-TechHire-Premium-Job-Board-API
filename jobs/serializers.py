from rest_framework import serializers
from .models import JobPosting, UserProfile

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        
        is_premium = (
            request and 
            request.user.is_authenticated and 
            hasattr(request.user, 'profile') and 
            request.user.profile.membership_tier == 'P'
        )

        if not is_premium:
            locked_msg = "🔒 Premium Feature"
            data['company_name'] = locked_msg
            data['salary_range'] = locked_msg
            data['application_link'] = locked_msg
            
        # THIS LINE IS THE FIX:
        return data