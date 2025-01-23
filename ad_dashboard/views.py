from django.shortcuts import render
from .models import AdCampaign, Project
import pandas as pd
import plotly.express as px
from plotly.offline import plot
from django.http import JsonResponse

def dashboard(request):
    campaigns = AdCampaign.objects.all()
    return render(request, 'dashboard.html', {'campaigns': campaigns})

def project_timeline(request):
    projects = Project.objects.all()
    data = [{
        'Project': project.name,
        'Start': project.start_date,
        'Finish': project.finish_date,
        'Responsible': project.responsible.username
    } for project in projects]

    df = pd.DataFrame(data)
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Project", color="Responsible")
    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")

    return render(request, 'project_timeline.html', {'plot_div': gantt_plot})

from django.shortcuts import render

def campaign_data_view(request):
    # Sample data for campaigns
    campaigns = {
        'Campaign A': {'impressions': 1000, 'conversions': 200, 'clicks': 150},
        'Campaign B': {'impressions': 1500, 'conversions': 300, 'clicks': 250},
        'Campaign C': {'impressions': 2000, 'conversions': 400, 'clicks': 350},
    }

    impressions = [data['impressions'] for data in campaigns.values()]
    conversions = [data['conversions'] for data in campaigns.values()]
    clicks = [data['clicks'] for data in campaigns.values()]
    campaign_names = list(campaigns.keys())

    context = {
        'impressions': impressions,
        'conversions': conversions,
        'clicks': clicks,
        'campaign_names': campaign_names,
    }
    return render(request, 'your_template.html', context)

def chart_data(request):
    # Sample data for the chart
    campaigns = AdCampaign.objects.all()
    
    # Prepare data for the chart
    labels = [campaign.name for campaign in campaigns]
    impressions = [campaign.impressions for campaign in campaigns]
    clicks = [campaign.clicks for campaign in campaigns]
    conversions = [campaign.conversions for campaign in campaigns]

    data = {
        'labels': labels,
        'impressions': impressions,
        'clicks': clicks,
        'conversions': conversions,
    }
    
    return JsonResponse(data)
