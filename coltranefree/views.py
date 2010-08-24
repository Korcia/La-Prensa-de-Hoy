#from django.shortcuts import get_object_or_404
#from django.views.generic.list_detail import object_list

#from coltrane.models import Category


#def category_detail(request, slug):
#    category = get_object_or_404(Category, slug=slug)
#    return object_list(request, queryset=category.live_entry_set(),
#                       extra_context={ 'category': category })
from django.contrib.auth.decorators import login_required
from django.views.generic.date_based import archive_index
#from django.views.decorators.csrf import csrf_exempt

@login_required
def limited_archive_index(*args, **kwargs):
    return archive_index(*args, **kwargs)
