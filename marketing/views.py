from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from laprensadehoy.settings import CURRENT_PATH
import os

ROBOTS_PATH = os.path.join(CURRENT_PATH, 'marketing/robots.txt')

def robots(request):
    """ view for robots.txt file """
    return HttpResponse(open(ROBOTS_PATH).read(), 'text/plain')
