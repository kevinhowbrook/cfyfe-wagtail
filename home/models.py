from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.core.models import Page
from django.shortcuts import render
from django.views.decorators.vary import vary_on_headers
from project.models import ProjectPage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random

class HomePage(Page):
    @property
    def projects(self):
        # Get list of projects
        projects = ProjectPage.objects.filter(
            live=True,
        )

        return projects

    @vary_on_headers('X-Requested-With')
    def serve(self, request):
        # Get Projects
        projects = list(self.projects.filter(show_on_front=1))
        # This gets a QuerySet of live children of the homepage with ``show_in_menus`` set
        
        random.shuffle(projects)
        # Pagination
        page = request.GET.get('page')
        paginator = Paginator(projects, 24)  # Show 12 events per page
        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            projects = paginator.page(1)
        except EmptyPage:
            projects = paginator.page(paginator.num_pages)


        return render(request, self.template, {
            'self': self,
            'projects': projects,
        })

    
