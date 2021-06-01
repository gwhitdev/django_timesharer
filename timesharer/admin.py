from django.contrib import admin
from .models import Volunteer, Opportunity, Organisation
# Register your models here.

class OpportunitiesInLine(admin.StackedInline):
    model = Opportunity
    extra = 0
    classes = {'collapse'}

class OrganisationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['name','created_at','owned_by']}),
        ('Organisation details',    {'fields': ['location','description','is_live','tags']})
    ]
    inlines = [OpportunitiesInLine]

## Opportunities
class VolunteersInLine(admin.StackedInline):
    model = Volunteer
    extra = 0
    classes = {'collapse'}

class OpportunityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'description','location', 'owned_by', 'is_live', 'tags', 'created_at']}),
    ]
    inlines=[VolunteersInLine]

admin.site.register(Volunteer)
admin.site.register(Opportunity, OpportunityAdmin)
admin.site.register(Organisation, OrganisationAdmin)
