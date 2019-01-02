from django.views.generic.detail import DetailView

from listing.models import Project

class ProjectDetails(DetailView):
    model = Project
