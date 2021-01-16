from django import template
from urllib.parse import urlencode



register = template.Library()

@register.simple_tag
def url_replace(request, field, value):
    """ Metóda, ktorá zmení, resp. pridá zvolený GET parameter a jeho hodnotu do URL """

    parameters = request.GET.copy()
    parameters[field] = value
    return parameters.urlencode()

