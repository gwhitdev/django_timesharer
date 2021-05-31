from timesharer.models import Opportunity

class Opportunity_Service:
    def __init__(self, opportunity_id):
        self.opportunity = Opportunity.objects.get(pk=opportunity_id)
    
    def make_live(self):
        opportunity = self.opportunity
        opportunity.is_live = True
        opportunity.save()
        return opportunity

    def make_not_live(self):
        opportunity = self.opportunity
        opportunity.is_live = False
        opportunity.save()
        return opportunity

