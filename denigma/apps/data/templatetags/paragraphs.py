"""Provides a template tag  extract the first paragraph of a text."""
from django import template


register = template.Library()


@register.filter()
def paraone(text, num=0):
    """Splits a text by two next-line (separation of paragraph)
    and returns the defined element (paragraph) which is by default
    the first occurrence.

    It also retains the last element which is often the update link."""
    paragraphs = text.replace('\r', '').split('\n\n')
    return paragraphs[num]+paragraphs[-1]

@register.filter()
def firstpara(text):
    """Returns the first paragraph of a string."""
    return text.replace('\r', '').split('\n\n')[0]
