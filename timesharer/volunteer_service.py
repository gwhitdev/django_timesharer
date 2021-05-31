from timesharer.models import Volunteer

class Volunteer_Service:
    def __init__(self, volunteer_id):
        self.volunteer = Volunteer.objects.get(pk=volunteer_id)

    def make_not_live(self):
        volunteer = self.volunteer
        volunteer.is_live = False
        volunteer.save()
        return volunteer

    def make_live(self):
        volunteer = self.volunteer
        volunteer.is_live = True
        volunteer.save()
        return volunteer
