from django.core.management.base import BaseCommand
from ad_dashboard.models import AdCampaign

class Command(BaseCommand):
    help = 'Load dummy ad campaign data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        AdCampaign.objects.all().delete()

        # Create dummy data
        campaigns = [
            AdCampaign(name='Campaign 1', impressions=1000, clicks=100, conversions=10, cost=50),
            AdCampaign(name='Campaign 2', impressions=2000, clicks=200, conversions=20, cost=100),
            AdCampaign(name='Campaign 3', impressions=1500, clicks=150, conversions=15, cost=75),
            AdCampaign(name='Campaign 5', impressions=1030, clicks=80, conversions=10, cost=50),
            AdCampaign(name='Campaign 6', impressions=2000, clicks=200, conversions=20, cost=100),
            AdCampaign(name='Campaign 7', impressions=1830, clicks=150, conversions=15, cost=75),
            AdCampaign(name='Campaign 8', impressions=3210, clicks=300, conversions=30, cost=150),
        ]
        AdCampaign.objects.bulk_create(campaigns)

        self.stdout.write(self.style.SUCCESS('Dummy data loaded successfully'))