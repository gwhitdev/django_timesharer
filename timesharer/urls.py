from django.urls import path
from . import views

app_name = 'timesharer'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('volunteer/create/', views.CreateVolunteer.as_view(), name='create_volunteer'),
    path('organisation/create/', views.CreateOrganisation.as_view(), name='create_organisation'),
    path('organisation/<int:pk>/', views.OrganisationDetail.as_view(), name='organisation_detail'),
    path('opportunity/<int:pk>/', views.OpportunityDetail.as_view(), name='opportunity_detail'),
    path('opportunity/create/', views.CreateOpportunity.as_view(), name='create_opportunity'),
]