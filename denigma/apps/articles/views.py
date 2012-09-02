from django.shortcuts import render_to_response
from django.template import RequestContext

from blog.models import Post


def view(request, title):
    """Viewing article by title."""
    post = Post.objects.get(title=title.replace('_', ' ')) # Deslugify.
    return render_to_response('articles/view.html', {'post': post},
                              context_instance=RequestContext(request))
