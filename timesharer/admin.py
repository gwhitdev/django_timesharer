from django.contrib import admin
from .models import Volunteer, Opportunity, Organisation
# Register your models here.

class OpportunitiesInLine(admin.StackedInline):
    model = Opportunity
    extra = 1
    classes = {'collapse'}

class OrganisationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['name','created_at']}),
        ('Organisation details',    {'fields': ['location','is_live','tags']})
    ]
    inlines = [OpportunitiesInLine]

admin.site.register(Volunteer)
admin.site.register(Opportunity)
admin.site.register(Organisation, OrganisationAdmin)
