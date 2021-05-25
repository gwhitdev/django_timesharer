from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from .models import Volunteer, Opportunity, Organisation

class IndexView(TemplateView):
    template_name = 'timesharer/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organisations'] = Organisation.objects.all()
        context['opportunities'] = Opportunity.objects.all()
        return context

class CreateOpportunity(CreateView):
    model = Opportunity
    template_name = 'timesharer/forms/create_opportunity.html'
    fields = ['title','is_live','owned_by']

class CreateVolunteer(LoginRequiredMixin, CreateView):
    model = Volunteer
    template_name = 'timesharer/forms/create_volunteer.html'
    fields = ['name', 'location', 'opted_in', 'created_at', 'updated_at', 'is_live', 'applied_to']
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class CreateOrganisation(CreateView):
    model = Organisation
    template_name = 'timesharer/forms/create_organisation.html'
    fields = ['name', 'location', 'is_live']

class OpportunityDetail(generic.DetailView):
    model = Opportunity
    template_name = 'timesharer/opportunity_detail.html'

class OrganisationDetail(generic.DetailView):
    model = Organisation
    template_name = 'timesharer/organisation_detail.html'

