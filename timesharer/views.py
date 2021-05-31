from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.base import TemplateView
from .models import Volunteer, Opportunity, Organisation
from taggit.models import Tag
from django.utils import timezone
from .volunteer_service import Volunteer_Service
from .organisation_service import Organisation_Service
from .opportunity_service import Opportunity_Service

def tagged_organisations(request, slug):
    lower_case_slug = slug.lower()
    tag = get_object_or_404(Tag, slug=lower_case_slug)
    organisations = Organisation.objects.filter(tags=tag)[:5]
    context = {
        'tag':tag,
        'organisations':organisations
    }
    return render(request, 'timesharer/tagged_organisations.html', context)

def tagged_opportunities(request, slug):
    lower_case_slug = slug.lower()
    tag = get_object_or_404(Tag, slug=lower_case_slug)
    opportunities = Opportunity.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'opportunities':opportunities
    }
    return render(request, 'timesharer/tagged_opportunities.html', context)

def amend_vol_live_status(request, volunteer_id):
    volunteer_service = Volunteer_Service(volunteer_id)
    volunteer = Volunteer.objects.get(pk=volunteer_id)
    if volunteer.is_live:
        volunteer_service.make_not_live()
        return redirect('user_profile:index')
    if volunteer.is_live == False:
        volunteer_service.make_live()
        return redirect('user_profile:index')

def amend_org_live_status(request, organisation_id):
    organisation_service = Organisation_Service(organisation_id)
    organisation = Organisation.objects.get(pk=organisation_id)
    if organisation.is_live:
        organisation_service.make_not_live()
        return redirect('timesharer:organisation_detail',organisation_id)
    if organisation.is_live == False:
        organisation_service.make_live()
        return redirect('timesharer:organisation_detail',organisation_id)

def amend_opp_live_status(request, opportunity_id):
    opportunity_service = Opportunity_Service(opportunity_id)
    opportunity = Opportunity.objects.get(pk=opportunity_id)
    if opportunity.is_live:
        opportunity_service.make_not_live()
        return redirect('timesharer:opportunity_detail', opportunity_id)
    if opportunity.is_live == False:
        opportunity_service.make_live()
        return redirect('timesharer:opportunity_detail', opportunity_id)


class IndexView(TemplateView):
    template_name = 'timesharer/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        public_volunteers = Volunteer.objects.filter(is_live=True).order_by('created_at')[:5]
        public_organisations = Organisation.objects.filter(is_live=True).order_by('-created_at')[:5]
        public_opportunities = Opportunity.objects.filter(is_live=True).order_by('-created_at')[:5]
        context['organisations'] = public_organisations
        context['opportunities'] = public_opportunities
        context['volunteers'] = public_volunteers
        return context

#OPPORTUNITY
class CreateOpportunity(LoginRequiredMixin,CreateView):
    model = Opportunity
    template_name = 'timesharer/opportunity/forms/create_opportunity.html'
    fields = ['title','is_live','owned_by']

class OpportunityDetail(LoginRequiredMixin,generic.DetailView):
    model = Opportunity
    template_name = 'timesharer/opportunity/opportunity_detail.html'

class DeleteOpportunity(LoginRequiredMixin,generic.DeleteView):
    template_name = 'timesharer/opportunity/forms/delete_volunteer.html'

class EditOpportunity(LoginRequiredMixin,generic.UpdateView):
    model = Opportunity
    template_name = 'timesharer/opportunity/forms/edit_opportunity.html'

#VOLUNTEER
class CreateVolunteer(LoginRequiredMixin,CreateView):
    model = Volunteer
    template_name = 'timesharer/volunteer/forms/create_volunteer.html'
    fields = ['name', 'location', 'opted_in', 'created_at', 'updated_at', 'is_live', 'applied_to']
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class VolunteerDetail(LoginRequiredMixin,generic.DetailView):
    model = Volunteer
    #recent = (updated_at - timezone.now()).seconds < 60
    template_name = 'timesharer/volunteer/volunteer_detail.html'

class DeleteVolunteer(LoginRequiredMixin,generic.DeleteView):
    template_name = 'timesharer/volunteer/forms/delete_volunteer.html'

class EditVolunteer(LoginRequiredMixin,generic.UpdateView):
    model = Volunteer
    template_name = 'timesharer/volunteer/forms/edit_volunteer.html'

#ORGANISATION
class CreateOrganisation(LoginRequiredMixin,CreateView):
    model = Organisation
    template_name = 'timesharer/organisation/forms/create_organisation.html'
    fields = ['name', 'location', 'is_live']

class OrganisationDetail(LoginRequiredMixin,generic.DetailView):
    model = Organisation
    template_name = 'timesharer/organisation/organisation_detail.html'

class DeleteOrganisation(LoginRequiredMixin,generic.DeleteView):
    template_name = 'timesharer/organisation/forms/delete_organisation.html'

class EditOrganisation(LoginRequiredMixin,generic.UpdateView):
    model = Organisation
    template_name = 'timesharer/organisation/forms/edit_organisation.html'

