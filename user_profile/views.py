from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from timesharer.models import Volunteer, Organisation, Opportunity
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import datetime
from django.utils import timezone

@login_required
def index(request):
    user = request.user
    
    try:
        volunteer = Volunteer.objects.get(created_by=user.pk)
        
    except:
        volunteer = 'No volunteer'

    if volunteer != 'No volunteer':
        opportunities = volunteer.opportunity_set.all()

    if volunteer == 'No volunteer':
        opportunities = { 'zero': 1 }

    live_volunteer = volunteer.is_live

    capitalised_name = user.first_name.capitalize()

    context = {
        'volunteer':volunteer,
        'opportunities':opportunities,
        'capitalised_name':capitalised_name,
        'live_volunteer': live_volunteer
    }
    return render(request, 'user_profile/index.html', context)




