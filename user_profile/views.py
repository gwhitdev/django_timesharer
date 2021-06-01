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
        opportunities = Opportunity.objects.filter(pk=volunteer.pk)
        live_volunteer = volunteer.is_live
        print(volunteer)

    if volunteer == 'No volunteer':
        volunteer = {'error': 'No volunteer'}
        opportunities = {'error':'No opportunities'}
        live_volunteer = {'error': 'No volunteer'}
        print(volunteer)

    

    capitalised_name = user.first_name.capitalize()

    context = {
        'volunteer':volunteer,
        'opportunities':opportunities,
        'capitalised_name':capitalised_name,
        'live_volunteer': live_volunteer
    }
    return render(request, 'user_profile/index.html', context)




