from django.urls import path

from listing.views import ProjectDetails



urlpatterns = [
    path('<slug:slug>/', ProjectDetails.as_view(),name='projects'),
]