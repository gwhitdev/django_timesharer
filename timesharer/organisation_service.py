from timesharer.models import Organisation

class Organisation_Service:
    def __init__(self, organisation_id):
        self.organisation = Organisation.objects.get(pk=organisation_id)
    
    def make_live(self):
        organisation = self.organisation
        organisation.is_live = True
        organisation.save()
        return organisation
    
    def make_not_live(self):
        organisation = self.organisation
        organisation.is_live = False
        organisation.save()
        return organisation
