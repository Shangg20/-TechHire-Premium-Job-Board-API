from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    MEMBERSHIP_CHOICES = [
        ('B', 'Basic'),
        ('P', 'Premium'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    membership_tier = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='B')
    
    def __str__(self):
        return f"{self.user.username} - {self.get_membership_tier_display()}"

class JobPosting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100)
    application_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} at {self.company_name}"
    

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
