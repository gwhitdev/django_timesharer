from django.urls import path, include
from . import views

app_name = 'timesharer'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('organisations/<slug>/', views.tagged_organisations, name='tagged_organisations'),
    path('opportunities/<slug>/', views.tagged_opportunities, name='tagged_opportunities'),
    path('volunteer/<int:pk>/', views.VolunteerDetail.as_view(), name='volunteer_detail'),
    path('volunteer/create/', views.CreateVolunteer.as_view(), name='create_volunteer'),
    path('volunteer/<int:pk>/edit', views.EditVolunteer.as_view(), name='edit_volunteer'),
    path('volunteer/<int:pk>/delete', views.DeleteVolunteer.as_view(), name='delete_volunteer'),
    path('organisation/<int:pk>/', views.OrganisationDetail.as_view(), name='organisation_detail'),
    path('organisation/create/', views.CreateOrganisation.as_view(), name='create_organisation'),
    path('organisation/<int:pk>/edit', views.EditOrganisation.as_view(), name='edit_organisation'),
    path('organisation/<int:pk>/delete', views.DeleteOrganisation.as_view(), name='delete_organisation'),
    path('opportunity/<int:pk>/', views.OpportunityDetail.as_view(), name='opportunity_detail'),
    path('opportunity/create/', views.CreateOpportunity.as_view(), name='create_opportunity'),
    path('opportunity/<int:pk>/delete', views.DeleteOpportunity.as_view(), name='delete_opportunity'),
    path('opportunity/<int:pk>/edit', views.EditOpportunity.as_view(), name='edit_opportunity'),
]