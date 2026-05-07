from django.shortcuts import render, get_object_or_404
from .models import Project


def project_list(request):
    projects = Project.objects.prefetch_related('technologies').all()
    featured = projects.filter(featured=True)
    return render(request, 'projects/list.html', {
        'projects': projects,
        'featured': featured,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/detail.html', {'project': project})
