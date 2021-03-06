"""Main view module.
A view is just a Python function that takes an HttpRequest as its parameter
and returns an instance of HttpResponse.
"""
from django.shortcuts import render
from django.db.models import Q

from data import get
from data.models import Entry
from blog.models import Post

from django import forms


class SearchForm(forms.Form):
   text = forms.CharField(label="") #label="Site-wide search")


def home(request, template='homepage.html'):
    """The root source of all Denigmas URLs.
    Renders a dynamic home site with altered content."""
    searchform = SearchForm() # Depricated?
    denigma_description = get("Denigma Description")
    denigma_rationality = get("Denigma Rationality")
    news = Entry.objects.filter(Q(tags__name='news') |
                                Q(categories__name='News')).order_by('-created', '-id').distinct()[:8]\
        or Post.objects.filter(tags__name='news').order_by('-created', '-id')[:8]
    research = get("Research")
    programming = get("Programming")
    design = get("Design")
    dashboard = get("Dashboard")
    ctx = {'searchform': searchform,
           'denigma_description': denigma_description,
           'denigma_rationality': denigma_rationality,
           'news': news,
           'dashboard':dashboard,
           'research': research,
           'programming': programming,
           'design': design}
    return render(request, template, ctx)

def search(request, term, template='search.html'):
    """Site-wide search functionality"""
    term = request.META['QUERY_STRING'].split('models=data&q=')[1]
    return render(request, template, {'term': term})

def google(request, term, template='google.html'):
    return render(request, template, term)

def content(request, template='content.html'):
    contents = get('Content'), get("Data App"), get("Denigma Blog"), get("Denigma's Wiki")
    return render(request, template, {'contents': contents})

def repository(request, template='repository.html'):
    """A biologist-friendly data repository."""
    entry = get('Biology of Aging Repository')

    return render(request, template, {'entry': entry})

