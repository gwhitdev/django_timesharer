from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from timesharer.models import Volunteer, Organisation, Opportunity
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@login_required
def index(request):
    user = request.user
    try:
        volunteer = Volunteer.objects.get(created_by=user.pk)
        
    except:
        volunteer = 'No volunteer'

    if volunteer != 'No volunteer':
        opportunites = volunteer.opportunity_set.all()

    capitalised_name = user.username.capitalize()
    context = {
        'volunteer':volunteer,
        'capitalised_name':capitalised_name,
        'opportunities':opportunites
    }
    return render(request, 'user_profile/index.html', context)


