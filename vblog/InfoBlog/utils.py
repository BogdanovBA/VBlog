from django.db.models import Count

from .models import *


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context