from django.urls import path
from .views import dashboard, project_timeline, chart_data

urlpatterns = [
    path('', dashboard, name='dashboard'),
    # path('project-timeline/', project_timeline, name='project_timeline'),
    path('chart-data/', chart_data, name='chart_data'), 
]