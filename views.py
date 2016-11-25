from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Course

class IndexView(generic.ListView):
    template_name = 'coursemanager/index.html'
    context_object_name = 'latest_courses_list'

    def get_queryset(self):
        """Return the last five published courses."""
        return Course.objects.order_by('-course_date_created')[:5]


class DetailView(generic.DetailView):
    model = Course
    template_name = 'coursemanager/detail.html'
