from django.http import HttpResponse
from django.shortcuts import render
from visits.models import Pagevisits

def home_page(request, *args, **kwargs):
    qs = Pagevisits.objects.all()
    page_qs = Pagevisits.objects.filter(path=request.path)

    my_title = 'My Page'
    my_context = {
        "page_title": my_title,
        "page_visits_count": page_qs.count(),
        "percentage": (page_qs.count() * 100.0) / qs.count(),
        "total_visit_count": qs.count()
    }
    html_template = 'home.html'
    Pagevisits.objects.create(path=request.path)
    return render(request, html_template, my_context)

    # return HttpResponse("<h1> hello Wordld </h1>")