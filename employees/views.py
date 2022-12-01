from django.views.generic import TemplateView, ListView, DetailView

from .mixins import AjaxViewMixin
from .models import Subdivision


class HeadTemplateView(TemplateView):
    template_name = 'employees/head.html'


class SubdivisionListView(ListView):
    model = Subdivision
    queryset = Subdivision.objects.all()

    template_name = 'employees/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super(SubdivisionListView, self).get_context_data()
        context_data['data'] = self.model.get_data()
        return context_data


class SubdivisionEmployeesAjaxListView(AjaxViewMixin, DetailView):
    model = Subdivision
    queryset = Subdivision.objects.all()

    template_name = 'employees/list.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.ajax_response(self.object.get_employees())
